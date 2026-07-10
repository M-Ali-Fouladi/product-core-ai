from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Store(Base):
    __tablename__ = "stores"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        index=True
    )

    slug: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        index=True
    )

    website: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    logo: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    active: Mapped[bool] = mapped_column(
        default=True
    )
