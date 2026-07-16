import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, field_validator


class DocumentUploadResponse(BaseModel):
    document_id: uuid.UUID


class DocumentDetail(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    original_filename: str
    content_type: str
    status: str
    title: str | None
    author: str | None
    shelf_location: str | None
    category_id: uuid.UUID | None
    epub_object_key: str | None
    created_at: datetime


class DocumentMetadataUpdate(BaseModel):
    title: str
    author: str
    shelf_location: str | None = None
    category_id: uuid.UUID | None = None

    @field_validator("title", "author")
    @classmethod
    def required_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("must not be empty or whitespace")
        return value

    @field_validator("shelf_location")
    @classmethod
    def optional_text(cls, value: str | None) -> str | None:
        if value is None:
            return None
        return value.strip() or None


class OcrJobDetail(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    job_id: uuid.UUID
    attempt: int
    status: str
    error_message: str | None
    created_at: datetime
    updated_at: datetime


class OcrJobAccepted(BaseModel):
    job_id: uuid.UUID
    attempt: int
    status: str


class PageSummary(BaseModel):
    page_number: int
    text_content: str
    has_image: bool


class PageDetail(PageSummary):
    pass


class PageTextUpdate(BaseModel):
    text_content: str


class OcrDashboardItem(BaseModel):
    document_id: uuid.UUID
    original_filename: str
    document_status: str
    job_id: uuid.UUID | None
    attempt: int | None
    ocr_status: str | None
    error_message: str | None
    created_at: datetime
    updated_at: datetime | None


class PublishJobDetail(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    publish_job_id: uuid.UUID
    attempt: int
    status: str
    error_message: str | None
    created_at: datetime
    updated_at: datetime


class PublishJobAccepted(BaseModel):
    publish_job_id: uuid.UUID
    attempt: int
    status: str
