"""M6 Reader — owner: Khoa Nguyễn — LDMS-008, LDMS-014.

Mint a time-limited MinIO Signed URL for a published document's EPUB, only
after RBAC has passed (Constitution Principle IV).
"""

import uuid

from sqlalchemy.orm import Session

from app.core.exceptions import ValidationError
from app.core.security import AuthenticatedUser
from app.core.storage import get_presigned_url
from app.schemas.document import ReaderContent
from app.services.document_service import ensure_readable, get_document

EPUB_URL_EXPIRES_SECONDS = 900


def get_reader_content(
    db: Session, document_id: uuid.UUID, user: AuthenticatedUser | None
) -> ReaderContent:
    document = ensure_readable(get_document(db, document_id), user)
    if document.status != "published":
        raise ValidationError("Tài liệu chưa được xuất bản.")
    if document.epub_object_key is None:
        raise ValidationError("Không tìm thấy bản đọc EPUB.")
    epub_url = get_presigned_url(document.epub_object_key, EPUB_URL_EXPIRES_SECONDS)
    return ReaderContent(
        document_id=document.id,
        title=document.title or document.original_filename,
        author=document.author,
        epub_url=epub_url,
        expires_in=EPUB_URL_EXPIRES_SECONDS,
    )
