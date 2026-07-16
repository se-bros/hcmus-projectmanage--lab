import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, field_validator


class CategoryCreate(BaseModel):
    name: str
    parent_id: uuid.UUID | None = None

    @field_validator("name")
    @classmethod
    def valid_name(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("must not be empty or whitespace")
        return value


class CategoryUpdate(BaseModel):
    name: str

    @field_validator("name")
    @classmethod
    def valid_name(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("must not be empty or whitespace")
        return value


class CategoryDetail(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    parent_id: uuid.UUID | None
    created_at: datetime
    updated_at: datetime


class CategoryTree(CategoryDetail):
    children: list[CategoryDetail]
