import uuid

from sqlalchemy.orm import Session

from app.models.page import Page
from app.services.ocr_service import get_page


def get_document_page(db: Session, document_id: uuid.UUID, page_number: int) -> Page:
    return get_page(db, document_id, page_number)


def update_page_text(
    db: Session,
    document_id: uuid.UUID,
    page_number: int,
    text_content: str,
) -> Page:
    page = get_page(db, document_id, page_number)
    page.text_content = text_content
    db.commit()
    db.refresh(page)
    return page
