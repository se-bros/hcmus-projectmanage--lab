import uuid

from sqlalchemy.orm import Session

from app.core.exceptions import NotFoundError
from app.core.security import AuthenticatedUser, ensure_document_editable
from app.models.category import Category
from app.models.document import Document
from app.schemas.document import DocumentMetadataUpdate


def update_document_metadata(
    db: Session,
    document_id: uuid.UUID,
    payload: DocumentMetadataUpdate,
    user: AuthenticatedUser,
) -> Document:
    document = db.get(Document, document_id)
    if document is None:
        raise NotFoundError("Document not found.")
    ensure_document_editable(document.owner_id, user)
    if payload.category_id is not None and db.get(Category, payload.category_id) is None:
        raise NotFoundError("Category not found.")

    document.title = payload.title
    document.author = payload.author
    document.shelf_location = payload.shelf_location
    document.category_id = payload.category_id
    db.commit()
    db.refresh(document)
    return document
