from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.crud.records import get_records_by_owner_id
from src.model.db_core import get_session
from src.schema.record import RecordResponse

router = APIRouter()


@router.get(
    "/{owner_id}",
    operation_id="read_record_by_owner_id",
    summary="Read Record by Owner ID",
    response_model=List[RecordResponse],
    status_code=status.HTTP_200_OK,
)
def read_dataset(
    owner_id: str,
    db: Session = Depends(get_session),
):
    return get_records_by_owner_id(db=db, owner_id=owner_id)