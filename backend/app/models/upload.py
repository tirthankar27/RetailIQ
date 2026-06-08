from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from app.database.base import Base


class Upload(Base):
    __tablename__ = "uploads"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    filename: Mapped[str] = mapped_column(
        String(255)
    )

    file_path: Mapped[str] = mapped_column(
        String(500)
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="uploaded"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )