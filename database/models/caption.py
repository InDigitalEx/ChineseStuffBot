from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Caption(Base):
    __tablename__ = 'caption'

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[Optional[str]] = mapped_column(String(256))
