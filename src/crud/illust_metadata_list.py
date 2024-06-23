from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import uuid4

from src.schema.illust_metadata import IllustMetadataCreate
from src.model.illust_metadata import IllustMetadataTable


# 複数のレコードをまとめて登録する
# def create_illust_metadata_list(db: Session, illust_metadata_list: List[IllustMetadataCreate]):
#     try:
#         for illust_metadata in illust_metadata_list:
#             illust_metadata = IllustMetadataTable(
#                 id=uuid4(),
#                 name=illust_metadata.name,
#                 genre=illust_metadata.genre,
#                 original_image=illust_metadata.original_image,
#                 badge_image=illust_metadata.badge_image,
#                 contour_points=illust_metadata.contour_points
#             )
#             db.add(illust_metadata)
#         db.commit()
#         db.refresh(illust_metadata)
#     except:
#         db.rollback()
#         raise
#     return illust_metadata_list


# 全てのレコードのID,イラスト名,ジャンル,イラスト画像を取得
def get_all_illust_metadata_basic_info(db: Session):
    try:
        illust_metadata_basic_info = db.query(
            IllustMetadataTable.id, 
            IllustMetadataTable.name, 
            IllustMetadataTable.genre, 
            IllustMetadataTable.original_image
        ).all()
        if illust_metadata_basic_info is None:
            raise HTTPException(status_code=404, detail=f"Item not found")
    except:
        raise
    return illust_metadata_basic_info


# 全てのレコードのID,イラスト名,ジャンル,イラスト画像を取得
def get_all_illust_metadata(db: Session):
    try:
        illust_metadata = db.query(IllustMetadataTable).all()
        if illust_metadata is None:
            raise HTTPException(status_code=404, detail=f"Item not found")
    except:
        raise
    return illust_metadata