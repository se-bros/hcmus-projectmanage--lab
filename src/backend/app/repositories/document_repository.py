import uuid

from sqlalchemy.orm import Session

from app.models.document import Document


class DocumentRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(
        self,
        *,
        document_id: uuid.UUID,
        original_filename: str,
        object_key: str,
        content_type: str,
        status: str = "uploaded",
        owner_id: uuid.UUID | None = None,
    ) -> Document:
        document = Document(
            id=document_id,
            original_filename=original_filename,
            object_key=object_key,
            content_type=content_type,
            status=status,
            owner_id=owner_id,
        )
        self.db.add(document)
        return document

    def get(self, document_id: uuid.UUID) -> Document | None:
        return self.db.get(Document, document_id)
