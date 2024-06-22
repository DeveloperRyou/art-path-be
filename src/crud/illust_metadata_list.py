from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.model.illust_metadata import IllustMetadataTable


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