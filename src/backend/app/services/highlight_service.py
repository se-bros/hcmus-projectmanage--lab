"""M6 Reader — owner: Khoa Nguyễn — LDMS-021.

Highlight và ghi chú theo cặp (document_id, user_sub). Điều kiện user_sub luôn
nằm trong mệnh đề WHERE chứ không phải một lần kiểm sau khi đã lấy bản ghi:
quên điều kiện thì truy vấn không trả về gì, còn quên câu `if` thì rò dữ liệu
của user khác (FR-012).
"""

import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.exceptions import NotFoundError, ValidationError
from app.core.security import AuthenticatedUser
from app.models.highlight import Highlight
from app.schemas.highlight import HighlightCreate
from app.services.document_service import ensure_readable, get_document


def _get_owned_highlight(
    db: Session, document_id: uuid.UUID, highlight_id: uuid.UUID, user_sub: str
) -> Highlight:
    highlight = db.scalar(
        select(Highlight).where(
            Highlight.id == highlight_id,
            Highlight.document_id == document_id,
            Highlight.user_sub == user_sub,
        )
    )
    if highlight is None:
        raise NotFoundError("Không tìm thấy đánh dấu.")
    return highlight


def list_highlights(
    db: Session, document_id: uuid.UUID, user: AuthenticatedUser
) -> list[Highlight]:
    ensure_readable(get_document(db, document_id), user)
    return list(
        db.scalars(
            select(Highlight)
            .where(Highlight.document_id == document_id, Highlight.user_sub == user.sub)
            .order_by(Highlight.created_at)
        )
    )


def create_highlight(
    db: Session, document_id: uuid.UUID, user: AuthenticatedUser, payload: HighlightCreate
) -> Highlight:
    document = ensure_readable(get_document(db, document_id), user)
    # `published` CHỈ kiểm ở đường tạo: highlight đã có phải sống sót khi tài
    # liệu bị gỡ xuất bản, nếu không một vòng re-publish sẽ khoá độc giả khỏi
    # ghi chú của chính họ (contracts/highlights-api.md).
    if document.status != "published":
        raise ValidationError("Tài liệu chưa được xuất bản.")
    highlight = Highlight(
        document_id=document_id,
        user_sub=user.sub,
        cfi_range=payload.cfi_range,
        selected_text=payload.selected_text,
        note=payload.note,
    )
    db.add(highlight)
    db.commit()
    db.refresh(highlight)
    return highlight


def update_note(
    db: Session,
    document_id: uuid.UUID,
    highlight_id: uuid.UUID,
    user_sub: str,
    note: str | None,
) -> Highlight:
    highlight = _get_owned_highlight(db, document_id, highlight_id, user_sub)
    highlight.note = note
    db.commit()
    db.refresh(highlight)
    return highlight


def delete_highlight(
    db: Session, document_id: uuid.UUID, highlight_id: uuid.UUID, user_sub: str
) -> None:
    db.delete(_get_owned_highlight(db, document_id, highlight_id, user_sub))
    db.commit()
