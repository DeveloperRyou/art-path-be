from uuid import UUID, uuid4

from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.model.record import RecordTable
from src.schema.record import RecordCreate, RecordUpdate

from src.model.illust_metadata import IllustMetadataTable


def create_record(db: Session, user_id: str, illust_metadata_id: UUID):
    try:
        badge = db.query(
            IllustMetadataTable.name,
            IllustMetadataTable.badge_image
        ).filter(IllustMetadataTable.id == illust_metadata_id).first()

        record = RecordTable(
            id=uuid4(),
            name=badge.name,
            profile_image=badge.badge_image,
            owner_id=user_id
        )
        db.add(record)
        db.commit()
        db.refresh(record)
    except:
        db.rollback()
        raise
    return record


def get_record_by_id(db: Session, record_id: UUID):
    try:
        record = db.query(RecordTable).filter(RecordTable.id == record_id ).one_or_none()
        if record is None:
            raise HTTPException(status_code=404, detail=f"Item not found")
    except:
        raise
    return record
    

def update_record(db: Session, record_id: UUID, record: RecordUpdate):
    try:
        _record = db.query(RecordTable).filter(RecordTable.id == record_id).first()
        _record.name = record.name
        _record.profile_image = record.profile_image
        db.commit()
    except:
        db.rollback()
        raise
    return _record


def delete_record(db: Session, record_id: UUID):
    try:
        db.query(RecordTable).filter(RecordTable.id == record_id).delete()
        db.commit()
    except:
        db.rollback()
        raise
    return