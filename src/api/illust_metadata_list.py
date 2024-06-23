from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.crud.illust_metadata_list import (
    get_all_illust_metadata_basic_info,
    # create_illust_metadata_list,
    get_all_illust_metadata,
)
from src.model.db_core import get_session
from src.schema.illust_metadata import (
    IllustMetadataResponse,
    IllustMetadataCreate,
    IllustMetadataBasicInfoResponse,
)

router = APIRouter()


# @router.post(
#     "",
#     operation_id="create_illust_metadata",
#     summary="Create IllustMetadata",
#     response_model=List[IllustMetadataResponse],
#     status_code=status.HTTP_201_CREATED,
# )
# def create_dataset(
#     illust_metadata_list: List[IllustMetadataCreate],
#     db: Session = Depends(get_session),
# ):
#     return create_illust_metadata_list(db=db, illust_metadata_list=illust_metadata_list)


@router.get(
    "",
    operation_id="read_illust_metadata_list_basic_info",
    summary="Read all IllustMetadata basic info",
    response_model=List[IllustMetadataBasicInfoResponse],
    status_code=status.HTTP_200_OK,
)
def read_dataset(
    db: Session = Depends(get_session),
):
    return get_all_illust_metadata_basic_info(db=db)


@router.get(
    "/all",
    operation_id="read_illust_metadata",
    summary="Read all IllustMetadata",
    response_model=List[IllustMetadataResponse],
    status_code=status.HTTP_200_OK,
)
def read_dataset(
    db: Session = Depends(get_session),
):
    return get_all_illust_metadata(db=db)
