from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.model.db_core import Base


class UserTable(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(30), primary_key=True, autoincrement=False)
    username: Mapped[str] = mapped_column(String(30))
    profile_image: Mapped[str] = mapped_column(String(255))
