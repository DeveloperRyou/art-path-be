from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.model.db_core import get_session
from src.schema.routing import RoutingResponse
from src.service.routing import generate_route

router = APIRouter()


@router.post(
    "",
    operation_id="routing",
    summary="Generate route",
    response_model=list[RoutingResponse],
    status_code=status.HTTP_201_CREATED,
)
def routing(
    latitude: float,
    longitude: float,
    illust_id: str,
    db: Session = Depends(get_session),
):
    return generate_route(
        db=db, latitude=latitude, longitude=longitude, illust_id=illust_id
    )
