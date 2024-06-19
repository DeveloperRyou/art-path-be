from uuid import UUID

from sqlalchemy import JSON, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db.core import Base


class RouteTable(Base):
    __tablename__ = "routes"

    id: Mapped[UUID] = mapped_column(primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column(String(10))
    coordinates: Mapped[dict] = mapped_column(JSON)
    distance: Mapped[float] = mapped_column(Float)
