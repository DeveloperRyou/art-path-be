from uuid import UUID, uuid4

from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.model.illust_metadata import IllustMetadataTable
from src.schema.illust_metadata import IllustMetadataCreate, IllustMetadataUpdate


def create_illust_metadata(db: Session, illust_metadata: IllustMetadataCreate):
    try:
        illust_metadata = IllustMetadataTable(
            id=uuid4(),
            name=illust_metadata.name,
            genre=illust_metadata.genre,
            original_image=illust_metadata.original_image,
            badge_image=illust_metadata.badge_image,
            contour_points=illust_metadata.contour_points
        )
        db.add(illust_metadata)
        db.commit()
        db.refresh(illust_metadata)
    except:
        db.rollback()
        raise
    return illust_metadata


# IDから輪郭の相対座標を取得
def get_illust_metadata_contour(db: Session, illust_metadata_id: UUID):
    try:
        illust_metadata = db.query(
            IllustMetadataTable.id,
            IllustMetadataTable.contour_points
        ).filter(IllustMetadataTable.id == illust_metadata_id ).first()

        if illust_metadata is None:
            raise HTTPException(status_code=404, detail=f"Item not found")
    except:
        raise
    return illust_metadata


# IDからバッジ画像を取得
def get_illust_metadata_badge_image(db: Session, illust_metadata_id: UUID):
    try:
        illust_metadata = db.query(
            IllustMetadataTable.id,
            IllustMetadataTable.name,
            IllustMetadataTable.badge_image
        ).filter(IllustMetadataTable.id == illust_metadata_id).first()
        if illust_metadata is None:
            raise HTTPException(status_code=404, detail=f"Item not found")
    except:
        raise
    return illust_metadata
    

def update_illust_metadata(db: Session, illust_metadata_id: UUID, illust_metadata: IllustMetadataUpdate):
    try:
        _illust_metadata = db.query(IllustMetadataTable).filter(IllustMetadataTable.id == illust_metadata_id).first()
        _illust_metadata.name = illust_metadata.name
        _illust_metadata.genre = str(illust_metadata.genre),
        _illust_metadata.original_image = illust_metadata.original_image,
        _illust_metadata.badge_image = illust_metadata.badge_image,
        _illust_metadata.contour_points = illust_metadata.contour_points
        db.commit()
    except:
        db.rollback()
        raise
    return _illust_metadata


def delete_illust_metadata(db: Session, illust_metadata_id: UUID):
    try:
        db.query(IllustMetadataTable).filter(IllustMetadataTable.id == illust_metadata_id).delete()
        db.commit()
    except:
        db.rollback()
        raise
    return

