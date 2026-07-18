"""M6 Reader — owner: Khoa Nguyễn — LDMS-008, LDMS-014, LDMS-019, LDMS-020.

Đọc EPUB qua MinIO Signed URL (15 phút), tùy chỉnh giao diện đọc, bookmark.
"""

import uuid
from typing import Annotated

from fastapi import APIRouter, Depends

from app.api.dependencies import DbSession
from app.core.security import AuthenticatedUser, get_current_user, get_optional_user
from app.schemas.document import BookmarkDetail, BookmarkUpdate, ReaderContent
from app.services.bookmark_service import get_bookmark, save_bookmark
from app.services.reader_service import get_reader_content

router = APIRouter(prefix="/documents", tags=["reader"])


@router.get("/{document_id}/reader", response_model=ReaderContent)
def read_document(
    document_id: uuid.UUID,
    db: DbSession,
    user: Annotated[AuthenticatedUser | None, Depends(get_optional_user)],
) -> ReaderContent:
    return get_reader_content(db, document_id, user)


@router.get("/{document_id}/bookmark", response_model=BookmarkDetail)
def read_bookmark(
    document_id: uuid.UUID,
    db: DbSession,
    user: Annotated[AuthenticatedUser, Depends(get_current_user)],
) -> BookmarkDetail:
    bookmark = get_bookmark(db, document_id, user.sub)
    return BookmarkDetail(
        document_id=bookmark.document_id,
        location=bookmark.location,
        updated_at=bookmark.updated_at,
    )


@router.put("/{document_id}/bookmark", response_model=BookmarkDetail)
def write_bookmark(
    document_id: uuid.UUID,
    payload: BookmarkUpdate,
    db: DbSession,
    user: Annotated[AuthenticatedUser, Depends(get_current_user)],
) -> BookmarkDetail:
    bookmark = save_bookmark(db, document_id, user.sub, payload.location)
    return BookmarkDetail(
        document_id=bookmark.document_id,
        location=bookmark.location,
        updated_at=bookmark.updated_at,
    )
