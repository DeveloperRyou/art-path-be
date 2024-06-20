from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.crud.record import create_record, delete_record, get_record_by_id, update_record
from src.model.db_core import get_session
from src.schema.record import RecordCreate, RecordResponse

router = APIRouter()


@router.post(
    "/{user_id}",
    operation_id="create_record",
    summary="Create Record",
    response_model=RecordResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_dataset(
    record: RecordCreate,
    db: Session = Depends(get_session),
):
    return create_record(db=db, record=record)


@router.get(
    "/{record_id}",
    operation_id="read_record_by_id",
    summary="Read Record by ID",
    response_model=RecordResponse,
    status_code=status.HTTP_200_OK,
)
def read_dataset(
    record_id: UUID,
    db: Session = Depends(get_session),
):
    return get_record_by_id(db=db, record_id=record_id)


@router.put(
    "/{record_id}",
    operation_id="update_record",
    summary="Update Record",
    response_model=RecordResponse,
    status_code=status.HTTP_200_OK,
)
def update_dataset(
    record_id: UUID,
    record: RecordCreate,
    db: Session = Depends(get_session),
):
    return update_record(db=db, record_id=record_id, record=record)


@router.delete(
    "/{record_id}",
    operation_id="delete_record",
    summary="Delete Record",
    status_code=status.HTTP_202_ACCEPTED,
)
async def delete_dataset(
    record_id: UUID,
    db: Session = Depends(get_session),
):
    delete_record(db=db, record_id=record_id)
