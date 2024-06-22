from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.crud.illust_metadata_list import get_all_illust_metadata_basic_info
from src.model.db_core import get_session
from src.schema.illust_metadata import IllustMetadataBase

router = APIRouter()


@router.get(
    "",
    operation_id="read_illust_metadata_list_basic_info",
    summary="Read all IllustMetadata basic info",
    response_model=List[IllustMetadataBase],
    status_code=status.HTTP_200_OK,
)
def read_dataset(
    db: Session = Depends(get_session),
):
    return get_all_illust_metadata_basic_info(db=db)