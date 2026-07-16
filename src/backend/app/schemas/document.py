"""Schemas cho M1/M6/M7 — placeholder LDMS-026/008/015 (đọc fixture).

Xem specs/001-reader-search-placeholder/data-model.md và contracts/.
"""

from datetime import date
from typing import Literal

from pydantic import BaseModel


class DocumentSummary(BaseModel):
    id: str
    title: str
    status: Literal["draft", "published"]
    created_at: date


class DocumentContent(BaseModel):
    document_id: str
    text: str


class SearchResult(BaseModel):
    document_id: str
    title: str
    snippet: str
