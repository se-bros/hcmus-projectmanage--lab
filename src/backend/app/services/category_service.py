import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.exceptions import ConflictError, NotFoundError, ValidationError
from app.models.category import Category
from app.models.document import Document
from app.schemas.category import CategoryCreate


def create_category(db: Session, payload: CategoryCreate) -> Category:
    if payload.parent_id is not None:
        parent = db.get(Category, payload.parent_id)
        if parent is None:
            raise NotFoundError("Parent category not found.")
        if parent.parent_id is not None:
            raise ValidationError("Categories are limited to two levels.")

    category = Category(id=uuid.uuid4(), name=payload.name, parent_id=payload.parent_id)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def list_category_tree(db: Session) -> list[Category]:
    return list(
        db.scalars(
            select(Category)
            .where(Category.parent_id.is_(None))
            .order_by(Category.name, Category.id)
        )
    )


def rename_category(db: Session, category_id: uuid.UUID, name: str) -> Category:
    category = db.get(Category, category_id)
    if category is None:
        raise NotFoundError("Category not found.")
    category.name = name
    db.commit()
    db.refresh(category)
    return category


def delete_category(db: Session, category_id: uuid.UUID) -> None:
    category = db.get(Category, category_id)
    if category is None:
        raise NotFoundError("Category not found.")
    if db.scalar(select(Category.id).where(Category.parent_id == category_id).limit(1)):
        raise ConflictError("Category cannot be deleted while it has children.")
    if db.scalar(select(Document.id).where(Document.category_id == category_id).limit(1)):
        raise ConflictError("Category cannot be deleted while documents use it.")
    db.delete(category)
    db.commit()
