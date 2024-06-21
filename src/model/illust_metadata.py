from uuid import UUID
import enum

from sqlalchemy import String, JSON, Enum
from sqlalchemy.orm import Mapped, mapped_column

from src.model.db_core import Base


class GenreEnum(enum.Enum):
    Vehicle = "のりもの"
    Weather_Season = "天気・季節"
    Animal = "生き物"
    Prefectures = "都道府県"
    Sports = "スポーツ"
    Symbols = "記号"
    Other = "その他"



class IllustMetadataTable(Base):
    __tablename__ = "illust_metadata"

    id: Mapped[UUID] = mapped_column(primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column(String(20))
    genre: Mapped[GenreEnum] = mapped_column(Enum(GenreEnum))
    image: Mapped[str] = mapped_column(String(255))
    contour_points: Mapped[JSON] = mapped_column(JSON)
