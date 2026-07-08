from sqlalchemy import ForeignKey, DateTime, String, func, Date
from .database import engine, SessionLocal
from datetime import date, datetime
from typing import List, Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

# Utilizamos DeclarativeBase de sqlalchemy de la última versión
class Base(DeclarativeBase):
    pass

# Tabla para guardar los volúmenes procesados
class ProcessedVolume(Base):
    __tablename__="processed_volume"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    processed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now())
    # Relación uno a muchos con el comic
    comics: Mapped[List["Comic"]] = relationship(
        back_populates="volume",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"ProcessedVolume(id={self.id!r}, title={self.title!r}, processed_at={self.processed_at!r})"

# Tabla para guardar los cómics
class Comic(Base):
    __tablename__="comic"
    id: Mapped[int] = mapped_column(primary_key=True)
    volume_id: Mapped[int] = mapped_column(
        ForeignKey("processed_volume.id", ondelete="CASCADE"), nullable=False)
    
    title: Mapped[str] = mapped_column(String(500), nullable=False)
    link: Mapped[str] = mapped_column(String(1000), nullable=False)

    release_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    cover_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    volume: Mapped["ProcessedVolume"] = relationship(back_populates="comics")

    def __repr__(self) -> str:
        return (
            f"Comic(id={self.id!r}, title={self.title!r}, "
            f"release_date={self.release_date!r}, cover_date={self.cover_date!r})"
        )