from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from src.model.db_core import Base


class RecordTable(Base):
    __tablename__ = "records"

    id: Mapped[UUID] = mapped_column(primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column(String(10))
    profile_image: Mapped[str] = mapped_column(String(255))
    owner_id: Mapped[UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
