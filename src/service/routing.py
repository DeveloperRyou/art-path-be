from uuid import UUID

import numpy as np
import requests
from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.schema.routing import RoutingResponse

# from src.crud.illust_metadata import get_illust_metadata_by_id


def generate_route(db: Session, latitude: float, longitude: float, illust_id: str):
    try:
        # illust = get_illust_metadata_by_id(db=db, illust_id=illust_id)
        # contour_points = illust.contour_points

        # with open("/Users/tatsuya/dev/lineyahoo/jupyter/main/contours.json", "r") as f:
        #     data = json.load(f)

        # contours = []

        # start_pos_lat = data["contours"][0][0]
        # start_pos_lng = data["contours"][0][1]

        # for jsn in data["contours"]:
        #     contours.append([jsn[0] - start_pos_lat, jsn[1] - start_pos_lng])

        # ひとまず
        contours = [
            [0.0, 0.0],
            [25.0, 26.33333333333333],
            [39.0, 52.33333333333333],
            [47.0, 71.33333333333333],
            [75.66666666666669, 135.66666666666669],
            [138.0, 130.33333333333331],
            [155.0, 135.33333333333331],
            [210.0, 88.33333333333333],
            [240.0, 72.33333333333333],
            [262.0, 63.33333333333333],
            [312.33333333333337, 56.33333333333333],
            [244.0, 124.83333333333333],
            [186.66666666666663, 163.0],
            [201.5, 229.83333333333331],
            [227.0, 218.33333333333331],
            [257.0, 208.33333333333331],
            [269.66666666666663, 237.33333333333331],
            [252.0, 261.3333333333333],
            [297.0, 243.33333333333331],
            [351.33333333333337, 230.33333333333331],
            [332.66666666666663, 337.3333333333333],
            [227.0, 354.8333333333333],
            [233.0, 381.3333333333333],
            [220.0, 389.3333333333333],
            [198.0, 469.8333333333333],
            [211.5, 497.8333333333333],
            [192.0, 499.3333333333333],
            [168.0, 489.3333333333333],
            [146.0, 477.3333333333333],
            [81.5, 476.8333333333333],
            [59.0, 491.3333333333333],
            [28.0, 499.8333333333333],
            [34.0, 460.8333333333333],
            [20.5, 438.8333333333333],
            [35.0, 336.8333333333333],
            [-50.75, 319.0833333333333],
            [-50.0, 287.3333333333333],
            [25.0, 276.3333333333333],
            [40.0, 275.3333333333333],
            [29.5, 256.8333333333333],
            [34.0, 169.83333333333331],
            [19.0, 141.33333333333331],
            [12.0, 124.33333333333333],
            [5.0, 102.33333333333333],
            [0.0, 0.0],
        ]

        latlngs = []

        contours_np = np.array(contours)

        max_values = np.max(contours_np, axis=0)
        min_values = np.min(contours_np, axis=0)

        s = 10  # 散歩距離
        a = max_values[1] - min_values[1]
        b = max_values[0] - min_values[0]
        x = s / (180 * (1.2 * a + b))

        # 緯度経度に変換
        for tour in contours:
            latlngs.append([latitude - tour[1] * x, longitude + tour[0] * x])

        # 経路探索
        points = []
        total_distance = 0.0
        for i in range(len(latlngs) - 1):
            url = "https://routing.openstreetmap.de/routed-foot/route/v1/walking/"

            way = f"{str(latlngs[i][1])},{str(latlngs[i][0])};{str(latlngs[i+1][1])},{str(latlngs[i+1][0])}"

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
