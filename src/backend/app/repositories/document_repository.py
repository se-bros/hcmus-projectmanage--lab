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
    ) -> Document:
        document = Document(
            id=document_id,
            original_filename=original_filename,
            object_key=object_key,
        )
        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)
        return document

    def get(self, document_id: uuid.UUID) -> Document | None:
        return self.db.get(Document, document_id)
