"""M6 Reader — owner: Khoa Nguyễn — LDMS-020.

Lưu và khôi phục vị trí đọc dở theo cặp (document_id, user_sub). Mọi truy vấn
lọc theo user_sub lấy từ JWT của chính request nên bookmark không lẫn giữa các
user (FR-013).
"""

import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.exceptions import NotFoundError
from app.models.bookmark import Bookmark
from app.services.document_service import get_document


def get_bookmark(db: Session, document_id: uuid.UUID, user_sub: str) -> Bookmark:
    bookmark = db.scalar(
        select(Bookmark).where(Bookmark.document_id == document_id, Bookmark.user_sub == user_sub)
    )
    if bookmark is None:
        raise NotFoundError("No bookmark saved yet.")
    return bookmark


def save_bookmark(db: Session, document_id: uuid.UUID, user_sub: str, location: str) -> Bookmark:
    get_document(db, document_id)
    bookmark = db.scalar(
        select(Bookmark).where(Bookmark.document_id == document_id, Bookmark.user_sub == user_sub)
    )
    if bookmark is None:
        bookmark = Bookmark(document_id=document_id, user_sub=user_sub, location=location)
        db.add(bookmark)
    else:
        bookmark.location = location
    db.commit()
    db.refresh(bookmark)
    return bookmark
