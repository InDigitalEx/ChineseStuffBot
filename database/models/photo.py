from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Photo(Base):
    __tablename__ = 'photo'

    id: Mapped[int] = mapped_column(primary_key=True)
    file_id: Mapped[str] = mapped_column(String(128))
    file_unique_id: Mapped[str] = mapped_column(String(128), unique=True)
