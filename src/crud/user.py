from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.model.user import UserTable
from src.schema.user import UserCreate, UserUpdate


def create_user(db: Session, user: UserCreate):
    try:
        user = UserTable(
            id=user.id,
            username=user.username,
            profile_image=user.profile_image,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    except:
        db.rollback()
        raise
    return user


def get_user(db: Session, user_id: str):
    try:
        user = db.query(UserTable).filter(UserTable.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail=f"Item not found")
    except:
        raise
    return user


def update_user(db: Session, user_id: str, user: UserUpdate):
    try:
        _user = db.query(UserTable).filter(UserTable.id == user_id).first()
        _user.username = user.username
        _user.profile_image = user.profile_image
        db.commit()
    except:
        db.rollback()
        raise
    return _user


def delete_user(db: Session, user_id: str):
    try:
        db.query(UserTable).filter(UserTable.id == user_id).delete()
        db.commit()
    except:
        db.rollback()
        raise
    return
