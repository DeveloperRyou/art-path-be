from uuid import UUID

from sqlalchemy import String, JSON, Enum
from sqlalchemy.orm import Mapped, mapped_column

from src.model.db_core import Base
from src.enum.genre_enum import GenreEnum


class IllustMetadataTable(Base):
    __tablename__ = "illust_metadata"

    id: Mapped[UUID] = mapped_column(primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column(String(20))
    genre: Mapped[GenreEnum] = mapped_column(Enum(GenreEnum))
    original_image: Mapped[str] = mapped_column(String(255))
    badge_image: Mapped[str] = mapped_column(String(255))
    contour_points: Mapped[list] = mapped_column(JSON)
