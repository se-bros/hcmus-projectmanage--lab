"""M6 Reader — owner: Khoa Nguyễn — LDMS-008, LDMS-014, LDMS-019, LDMS-020.

Đọc EPUB qua MinIO Signed URL (15 phút), tùy chỉnh giao diện đọc, bookmark.
"""

from fastapi import APIRouter

from app.core.exceptions import NotFoundError
from app.fixtures.documents import DOCUMENT_CONTENTS
from app.schemas.document import DocumentContent

router = APIRouter(tags=["reader"])


@router.get("/reader/{document_id}", response_model=DocumentContent)
def read_document(document_id: str) -> DocumentContent:
    text = DOCUMENT_CONTENTS.get(document_id)
    if text is None:
        raise NotFoundError(f"Document '{document_id}' not found")
    return DocumentContent(document_id=document_id, text=text)
