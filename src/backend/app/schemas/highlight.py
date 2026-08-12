"""M6 Reader — LDMS-021. Schema cho highlight và ghi chú."""

import uuid
from datetime import datetime

from pydantic import BaseModel, field_validator

from app.core.exceptions import ValidationError

MAX_NOTE_LENGTH = 2000
MAX_SELECTED_TEXT_LENGTH = 5000


def _validate_note(value: str | None) -> str | None:
    if value is None:
        return None
    if len(value) > MAX_NOTE_LENGTH:
        raise ValidationError(f"Ghi chú quá dài ({len(value)}/{MAX_NOTE_LENGTH} ký tự).")
    stripped = value.strip()
    return stripped or None


class HighlightCreate(BaseModel):
    cfi_range: str
    selected_text: str
    note: str | None = None

    @field_validator("selected_text")
    @classmethod
    def non_empty_selection(cls, value: str) -> str:
        stripped = value.strip()
        if not stripped:
            raise ValidationError("Vùng chọn không có nội dung.")
        if len(stripped) > MAX_SELECTED_TEXT_LENGTH:
            raise ValidationError(f"Đoạn chọn quá dài (tối đa {MAX_SELECTED_TEXT_LENGTH} ký tự).")
        return stripped

    @field_validator("cfi_range")
    @classmethod
    def single_chapter_range(cls, value: str) -> str:
        stripped = value.strip()
        if not stripped.startswith("epubcfi("):
            raise ValidationError("Vị trí đánh dấu không hợp lệ.")
        # CFI range có dạng epubcfi(<phần chung>,<đầu>,<cuối>). Phần chung phải
        # đã đi vào trong một spine item (chứa "!") thì hai đầu mới chắc chắn
        # cùng một chương (FR-005b, research.md R3).
        head, separator, _ = stripped.partition(",")
        if separator and "!" not in head:
            raise ValidationError("Chỉ đánh dấu được trong cùng một chương.")
        return stripped

    @field_validator("note")
    @classmethod
    def note_within_limit(cls, value: str | None) -> str | None:
        return _validate_note(value)


class HighlightNoteUpdate(BaseModel):
    note: str | None

    @field_validator("note")
    @classmethod
    def note_within_limit(cls, value: str | None) -> str | None:
        return _validate_note(value)


class HighlightDetail(BaseModel):
    """Không trả `user_sub`: client luôn chỉ nhận highlight của chính mình."""

    id: uuid.UUID
    document_id: uuid.UUID
    cfi_range: str
    selected_text: str
    note: str | None
    created_at: datetime
    updated_at: datetime
