from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Index, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Highlight(Base):
    """LDMS-021 — vùng văn bản độc giả đánh dấu, kèm ghi chú tùy chọn.

    Cố ý KHÔNG có UniqueConstraint như bookmarks: một user có nhiều highlight
    trên cùng document, và hai highlight được phép chồng lấn hoặc trùng khít
    (FR-004).
    """

    __tablename__ = "highlights"
    __table_args__ = (Index("ix_highlights_document_user", "document_id", "user_sub"),)

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    document_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("documents.id", ondelete="CASCADE"), index=True
    )
    user_sub: Mapped[str] = mapped_column(String(255), index=True)
    cfi_range: Mapped[str] = mapped_column(Text)
    selected_text: Mapped[str] = mapped_column(Text)
    note: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
