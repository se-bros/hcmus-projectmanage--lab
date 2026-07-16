"""M1 Documents & Storage — owner: Khoa Ngô (upload) / Khoa Nguyễn (list) — LDMS-002, LDMS-026.

Upload scan gốc lên MinIO, CRUD document, danh sách tài liệu.
"""

from fastapi import APIRouter

from app.fixtures.documents import DOCUMENTS
from app.schemas.document import DocumentSummary

router = APIRouter(prefix="/documents", tags=["documents"])


@router.get("", response_model=list[DocumentSummary])
def list_documents() -> list[DocumentSummary]:
    return DOCUMENTS
