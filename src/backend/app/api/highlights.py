"""M6 Reader — owner: Khoa Nguyễn — LDMS-021.

Highlight và ghi chú trên tài liệu đã xuất bản. Mọi endpoint bắt buộc đăng nhập
(FR-015) — khác `GET /documents/{id}/reader` vốn cho khách xem tài liệu public.
"""

import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.api.dependencies import DbSession
from app.core.security import AuthenticatedUser, get_current_user
from app.schemas.highlight import HighlightCreate, HighlightDetail, HighlightNoteUpdate
from app.services.highlight_service import (
    create_highlight,
    delete_highlight,
    list_highlights,
    update_note,
)

router = APIRouter(prefix="/documents", tags=["highlights"])

CurrentUser = Annotated[AuthenticatedUser, Depends(get_current_user)]


@router.get("/{document_id}/highlights", response_model=list[HighlightDetail])
def read_highlights(
    document_id: uuid.UUID,
    db: DbSession,
    user: CurrentUser,
) -> list[HighlightDetail]:
    return [
        HighlightDetail.model_validate(highlight, from_attributes=True)
        for highlight in list_highlights(db, document_id, user)
    ]


@router.post(
    "/{document_id}/highlights",
    response_model=HighlightDetail,
    status_code=status.HTTP_201_CREATED,
)
def write_highlight(
    document_id: uuid.UUID,
    payload: HighlightCreate,
    db: DbSession,
    user: CurrentUser,
) -> HighlightDetail:
    highlight = create_highlight(db, document_id, user, payload)
    return HighlightDetail.model_validate(highlight, from_attributes=True)


@router.patch("/{document_id}/highlights/{highlight_id}", response_model=HighlightDetail)
def write_highlight_note(
    document_id: uuid.UUID,
    highlight_id: uuid.UUID,
    payload: HighlightNoteUpdate,
    db: DbSession,
    user: CurrentUser,
) -> HighlightDetail:
    highlight = update_note(db, document_id, highlight_id, user.sub, payload.note)
    return HighlightDetail.model_validate(highlight, from_attributes=True)


@router.delete("/{document_id}/highlights/{highlight_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_highlight(
    document_id: uuid.UUID,
    highlight_id: uuid.UUID,
    db: DbSession,
    user: CurrentUser,
) -> None:
    delete_highlight(db, document_id, highlight_id, user.sub)
