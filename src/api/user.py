from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.crud.user import create_user, delete_user, get_user, update_user
from src.model.db_core import get_session
from src.schema.user import UserCreate, UserResponse

router = APIRouter()


@router.post(
    "",
    operation_id="create_user",
    summary="Create User",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_dataset(
    user: UserCreate,
    db: Session = Depends(get_session),
):
    return create_user(db=db, user=user)


@router.get(
    "/{user_id}",
    operation_id="read_user",
    summary="Read User",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
)
def read_dataset(
    user_id: str,
    db: Session = Depends(get_session),
):
    return get_user(db=db, user_id=user_id)


@router.put(
    "/{user_id}",
    operation_id="update_user",
    summary="Update User",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
)
def update_dataset(
    user_id: str,
    user: UserCreate,
    db: Session = Depends(get_session),
):
    return update_user(db=db, user_id=user_id, user=user)


@router.delete(
    "/{user_id}",
    operation_id="delete_user",
    summary="Delete User",
    status_code=status.HTTP_202_ACCEPTED,
)
async def delete_dataset(
    user_id: str,
    db: Session = Depends(get_session),
):
    delete_user(db=db, user_id=user_id)
