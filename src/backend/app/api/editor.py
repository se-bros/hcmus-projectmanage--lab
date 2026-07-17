"""M3 Editor — owner: Thái — LDMS-005, LDMS-006, LDMS-017.

Đọc/sửa text theo trang, UI biên tập, split-screen (ảnh scan + text OCR).
"""

import uuid

from fastapi import APIRouter

from app.api.dependencies import DbSession
from app.schemas.document import PageDetail, PageTextUpdate
from app.services.editor_service import get_document_page, update_page_text

router = APIRouter(prefix="/documents", tags=["editor"])


@router.get("/{document_id}/pages/{page_number}", response_model=PageDetail)
def read_page(document_id: uuid.UUID, page_number: int, db: DbSession) -> PageDetail:
    page = get_document_page(db, document_id, page_number)
    return PageDetail(
        page_number=page.page_number,
        text_content=page.text_content,
        has_image=page.image_object_key is not None,
    )


@router.put("/{document_id}/pages/{page_number}", response_model=PageDetail)
def replace_page_text(
    document_id: uuid.UUID,
    page_number: int,
    payload: PageTextUpdate,
    db: DbSession,
) -> PageDetail:
    page = update_page_text(db, document_id, page_number, payload.text_content)
    return PageDetail(
        page_number=page.page_number,
        text_content=page.text_content,
        has_image=page.image_object_key is not None,
    )
