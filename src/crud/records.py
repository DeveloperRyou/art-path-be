from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.model.record import RecordTable


def get_records_by_owner_id(db: Session, owner_id: str):
    try:
        records = db.query(RecordTable).filter(RecordTable.owner_id == owner_id).all()
        if not records:
            raise HTTPException(status_code=404, detail=f"Item not found")
    except:
        raise 
    return records