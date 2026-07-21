"""M4 Metadata — owner: Thái — LDMS-011, LDMS-012.

Gán metadata bắt buộc (title/author/shelf_location), cây category 2 cấp.
"""

import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.api.dependencies import DbSession
from app.core.security import AuthenticatedUser, require_roles
from app.models.category import Category
from app.models.document import Document
from app.schemas.category import CategoryCreate, CategoryDetail, CategoryTree, CategoryUpdate
from app.schemas.document import DocumentDetail, DocumentMetadataUpdate
from app.services.category_service import (
    create_category,
    delete_category,
    list_category_tree,
    rename_category,
)
from app.services.metadata_service import update_document_metadata

router = APIRouter(prefix="/documents", tags=["metadata"])
category_router = APIRouter(prefix="/categories", tags=["metadata"])


@router.put("/{document_id}/metadata", response_model=DocumentDetail)
def replace_document_metadata(
    document_id: uuid.UUID,
    payload: DocumentMetadataUpdate,
    db: DbSession,
    user: Annotated[AuthenticatedUser, Depends(require_roles("editor", "admin"))],
) -> Document:
    return update_document_metadata(db, document_id, payload, user)


@category_router.post(
    "",
    response_model=CategoryDetail,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_roles("admin"))],
)
def add_category(payload: CategoryCreate, db: DbSession) -> Category:
    return create_category(db, payload)


@category_router.get("", response_model=list[CategoryTree])
def read_categories(db: DbSession) -> list[Category]:
    return list_category_tree(db)


@category_router.patch(
    "/{category_id}",
    response_model=CategoryDetail,
    dependencies=[Depends(require_roles("admin"))],
)
def update_category(
    category_id: uuid.UUID,
    payload: CategoryUpdate,
    db: DbSession,
) -> Category:
    return rename_category(db, category_id, payload.name)


@category_router.delete(
    "/{category_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(require_roles("admin"))],
)
def remove_category(category_id: uuid.UUID, db: DbSession) -> None:
    delete_category(db, category_id)
