from uuid import UUID

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.core import Base


class UserTable(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True, autoincrement=False)
    username: Mapped[str] = mapped_column(String(10))
    profile_image: Mapped[str] = mapped_column(String(255))
