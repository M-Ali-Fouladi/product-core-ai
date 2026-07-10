from datetime import datetime
from sqlalchemy import (
    String,
    DateTime,
    ForeignKey,
    Numeric,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import Base


class ProductSource(Base):
    __tablename__ = "product_sources"

    id: Mapped[int] = mapped_column(primary_key=True)

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id", ondelete="CASCADE"),
        index=True
    )

#    store: Mapped[str] = mapped_column(
#        String(50),
#        index=True
#    )
    store_id: Mapped[int] = mapped_column(
    ForeignKey("stores.id"),
    index=True
    )

    store = relationship("Store")

    external_id: Mapped[str] = mapped_column(
        String(255),
        index=True
    )

    url: Mapped[str] = mapped_column(
        String(2000)
    )

    currency: Mapped[str] = mapped_column(
        String(10)
    )

    last_price: Mapped[float | None] = mapped_column(
        Numeric(12, 2),
        nullable=True
    )

    last_sync: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    product = relationship("Product", back_populates="sources")
