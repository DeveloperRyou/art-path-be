from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.crud.illust_metadata import create_illust_metadata, delete_illust_metadata, get_illust_metadata_contour, get_illust_metadata_badge_image, update_illust_metadata
from src.model.db_core import get_session
from src.schema.illust_metadata import IllustMetadataCreate, IllustMetadataResponse

router = APIRouter()


@router.post(
    "",
    operation_id="create_illust_metadata",
    summary="Create IllustMetadata",
    response_model=IllustMetadataResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_dataset(
    illust_metadata: IllustMetadataCreate,
    db: Session = Depends(get_session),
):
    return create_illust_metadata(db=db, illust_metadata=illust_metadata)


@router.get(
    "/contour/{illust_metadata_id}",
    operation_id="read_illust_metadata_contour",
    summary="Read IllustMetadata Contour Points",
    response_model=IllustMetadataResponse,
    status_code=status.HTTP_200_OK,
)
def read_illust_metadata_contour(
    illust_metadata_id: UUID,
    db: Session = Depends(get_session),
):
    return get_illust_metadata_contour(db=db, illust_metadata_id=illust_metadata_id)


@router.get(
    "/badge_image/{illust_metadata_id}",
    operation_id="read_illust_metadata_badge_image",
    summary="Read IllustMetadata Badge Image",
    response_model=IllustMetadataResponse,
    status_code=status.HTTP_200_OK,
)
def read_illust_metadata_badge_image(
    illust_metadata_id: UUID,
    db: Session = Depends(get_session),
):
    return get_illust_metadata_badge_image(db=db, illust_metadata_id=illust_metadata_id)



@router.put(
    "/{illust_metadata_id}",
    operation_id="update_illust_metadata",
    summary="Update IllustMetadata",
    response_model=IllustMetadataResponse,
    status_code=status.HTTP_200_OK,
)
def update_dataset(
    illust_metadata_id: UUID,
    illust_metadata: IllustMetadataCreate,
    db: Session = Depends(get_session),
):
    return update_illust_metadata(db=db, illust_metadata_id=illust_metadata_id, illust_metadata=illust_metadata)


@router.delete(
    "/{illust_metadata_id}",
    operation_id="delete_illust_metadata",
    summary="Delete IllustMetadata",
    status_code=status.HTTP_202_ACCEPTED,
)
async def delete_dataset(
    illust_metadata_id: UUID,
    db: Session = Depends(get_session),
):
    delete_illust_metadata(db=db, illust_metadata_id=illust_metadata_id)
