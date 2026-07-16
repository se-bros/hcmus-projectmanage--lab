import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


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
    epub_object_key: str | None
    created_at: datetime


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
