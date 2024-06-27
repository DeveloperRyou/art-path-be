import random
from uuid import UUID

import numpy as np
import requests
from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.crud.illust_metadata import get_illust_metadata_contour
from src.schema.routing import RoutingResponse


def generate_route(
    db: Session,
    latitude: float,
    longitude: float,
    illust_metadata_id: UUID,
    num_generation: int,
    distance: float,
):
    try:
        # 相対座標の取得
        illust_metadata = get_illust_metadata_contour(
            db=db, illust_metadata_id=illust_metadata_id
        )

        contours = []

        if num_generation == 0:
            start_pos_lat = illust_metadata[1][0]["latitude"]
            start_pos_lng = illust_metadata[1][0]["longitude"]

            for v in illust_metadata[1]:
                contours.append(
                    [v["latitude"] - start_pos_lat, v["longitude"] - start_pos_lng]
                )
        else:
            start_idx = 1
            if num_generation == 1:
                start_idx = int(len(illust_metadata[1]) / 2)
            elif num_generation == 2:
                start_idx = int(len(illust_metadata[1]) / 4)
            elif num_generation == 3:
                start_idx = int(len(illust_metadata[1]) * 3 / 4)
            else:
                start_idx = random.randrange(1, len(illust_metadata[1]) - 1)

            start_pos_lat = illust_metadata[1][start_idx]["latitude"]
            start_pos_lng = illust_metadata[1][start_idx]["longitude"]

            for i in range(start_idx, len(illust_metadata[1]) - 1):
                v = illust_metadata[1][i]
                contours.append(
                    [v["latitude"] - start_pos_lat, v["longitude"] - start_pos_lng]
                )

            for i in range(0, start_idx + 1):
                v = illust_metadata[1][i]
                contours.append(
                    [v["latitude"] - start_pos_lat, v["longitude"] - start_pos_lng]
                )

        latlngs = []

        contours_np = np.array(contours)

        max_values = np.max(contours_np, axis=0)
        min_values = np.min(contours_np, axis=0)

        s = distance  # 散歩距離
        a = max_values[1] - min_values[1]
        b = max_values[0] - min_values[0]
        x = s / (180 * (1.2 * a + b))

        # 緯度経度に変換
        for tour in contours:
            latlngs.append([latitude - tour[1] * x, longitude + tour[0] * x])

        # 経路探索
        points = []
        total_distance = 0.0
        url = "https://routing.openstreetmap.de/routed-foot/route/v1/walking/"
        way = ""
        for i in range(len(latlngs)):
            way += f"{str(latlngs[i][1])},{str(latlngs[i][0])};"

        way = way[:-1]
        url += way + "?geometries=geojson&overview=full"

        response = requests.get(url)

        # レスポンスを処理
        if response.status_code == 200:
            data = response.json()  # JSON形式のレスポンスを取得
        else:
            raise HTTPException(status_code=500, detail=f"OSRM API")

        for coordinate in data["routes"][0]["geometry"]["coordinates"]:
            points.append([coordinate[1], coordinate[0]])

        total_distance += data["routes"][0]["distance"] / 1000

        # 経路補正
        result = []
        i = 0
        tmp = None
        while i < len(points):
            if len(result) > 0 and points[i] == result[-1]:
                tmp = result[-1]
                result.pop(-1)
            elif len(result) > 1 and points[i] == result[-2]:
                tmp = result[-2]
                result.pop(-1)
                result.pop(-1)
            else:
                if tmp is not None:
                    result.append(tmp)
                    tmp = None
                result.append(points[i])

            i += 1

        arr = result
        routes = []
        i = 0
        tmp = None
        while i < len(arr):
            if len(routes) > 0 and arr[i] == routes[-1]:
                tmp = routes[-1]
                routes.pop(-1)
            elif len(routes) > 1 and arr[i] == routes[-2]:
                tmp = routes[-2]
                routes.pop(-1)
                routes.pop(-1)
            else:
                if tmp is not None:
                    routes.append(tmp)
                    tmp = None
                routes.append(arr[i])

            i += 1

        res = []
        for i, v in enumerate(routes, start=1):
            res.append(RoutingResponse(index=i, latitude=v[0], longitude=v[1]))

    except:
        raise
    return res
