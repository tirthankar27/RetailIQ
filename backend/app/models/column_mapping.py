from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.base import Base


class ColumnMapping(Base):
    __tablename__ = "column_mappings"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    upload_id: Mapped[int] = mapped_column(
        ForeignKey("uploads.id")
    )

    customer_column: Mapped[str] = mapped_column(
        String(100)
    )

    date_column: Mapped[str] = mapped_column(
        String(100)
    )

    quantity_column: Mapped[str] = mapped_column(
        String(100)
    )

    price_column: Mapped[str] = mapped_column(
        String(100)
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    product_column: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )