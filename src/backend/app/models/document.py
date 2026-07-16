from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.ocr_job import OcrJob
    from app.models.page import Page
    from app.models.publish_job import PublishJob


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    original_filename: Mapped[str] = mapped_column(String(255))
    object_key: Mapped[str] = mapped_column(String(512), unique=True)
    content_type: Mapped[str] = mapped_column(String(128))
    status: Mapped[str] = mapped_column(String(32), default="uploaded", server_default="uploaded")
    title: Mapped[str | None] = mapped_column(String(512), nullable=True)
    author: Mapped[str | None] = mapped_column(String(512), nullable=True)
    epub_object_key: Mapped[str | None] = mapped_column(String(512), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    ocr_jobs: Mapped[list[OcrJob]] = relationship(
        back_populates="document", cascade="all, delete-orphan"
    )
    pages: Mapped[list[Page]] = relationship(
        back_populates="document", cascade="all, delete-orphan"
    )
    publish_jobs: Mapped[list[PublishJob]] = relationship(
        back_populates="document", cascade="all, delete-orphan"
    )
