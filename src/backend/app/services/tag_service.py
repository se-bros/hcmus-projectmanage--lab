import uuid

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.exceptions import NotFoundError
from app.core.security import AuthenticatedUser, ensure_document_editable
from app.models.document import Document
from app.models.document_tag import DocumentTag
from app.services.document_service import ensure_readable, get_document


def normalize_tag(tag_name: str) -> str:
    normalized = tag_name.strip().lower()
    if not normalized:
        raise ValueError("Tag name must not be empty or whitespace.")
    return normalized


def get_document_tags(
    db: Session,
    document_id: uuid.UUID,
    user: AuthenticatedUser | None,
) -> list[str]:
    document = get_document(db, document_id)
    ensure_readable(document, user)
    tags = db.scalars(
        select(DocumentTag.name)
        .where(DocumentTag.document_id == document_id)
        .order_by(DocumentTag.name.asc())
    ).all()
    return list(tags)


def add_document_tag(
    db: Session,
    document_id: uuid.UUID,
    tag_name: str,
    user: AuthenticatedUser,
) -> list[str]:
    document = db.get(Document, document_id)
    if document is None:
        raise NotFoundError("Document not found.")
    ensure_document_editable(document.owner_id, user)

    normalized_name = normalize_tag(tag_name)

    existing_tag = db.scalars(
        select(DocumentTag).where(
            DocumentTag.document_id == document_id,
            DocumentTag.name == normalized_name,
        )
    ).first()

    if existing_tag is None:
        new_tag = DocumentTag(document_id=document_id, name=normalized_name)
        db.add(new_tag)
        db.commit()

    return get_document_tags(db, document_id, user)


def delete_document_tag(
    db: Session,
    document_id: uuid.UUID,
    tag_name: str,
    user: AuthenticatedUser,
) -> list[str]:
    document = db.get(Document, document_id)
    if document is None:
        raise NotFoundError("Document not found.")
    ensure_document_editable(document.owner_id, user)

    normalized_name = tag_name.strip().lower()

    existing_tag = db.scalars(
        select(DocumentTag).where(
            DocumentTag.document_id == document_id,
            DocumentTag.name == normalized_name,
        )
    ).first()

    if existing_tag is not None:
        db.delete(existing_tag)
        db.commit()

    return get_document_tags(db, document_id, user)
