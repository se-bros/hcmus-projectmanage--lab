"""M7 Search — owner: Khoa Nguyễn — LDMS-015, LDMS-016.

Full-text search over document title/author and OCR page content. Uses real
PostgreSQL FTS in production; falls back to a case-insensitive substring scan
on other dialects (SQLite in the test suite — see research.md §5).
"""

import re
import uuid

from sqlalchemy import ColumnElement, func, select, true
from sqlalchemy.orm import Session

from app.core.security import AuthenticatedUser
from app.models.document import Document
from app.models.page import Page
from app.schemas.document import SearchResult

_SNIPPET_RADIUS = 60
# ts_headline wraps matches in <b>…</b> by default; the frontend re-highlights,
# so strip the markup to avoid leaking literal tags into the rendered snippet.
_HEADLINE_MARKUP = re.compile(r"</?b>")


def search_documents(db: Session, q: str, user: AuthenticatedUser | None) -> list[SearchResult]:
    keyword = q.strip()
    if not keyword:
        return []
    if db.bind is not None and db.bind.dialect.name == "postgresql":
        return _search_postgres_fts(db, keyword, user)
    return _search_fallback(db, keyword, user)


def _rbac_filter(user: AuthenticatedUser | None) -> ColumnElement[bool]:
    if user is None:
        return Document.is_public.is_(True)
    return true()


def _make_snippet(text: str, match_start: int) -> str:
    start = max(0, match_start - _SNIPPET_RADIUS)
    end = min(len(text), match_start + _SNIPPET_RADIUS)
    snippet = text[start:end].strip()
    prefix = "…" if start > 0 else ""
    suffix = "…" if end < len(text) else ""
    return f"{prefix}{snippet}{suffix}"


def _search_postgres_fts(
    db: Session, keyword: str, user: AuthenticatedUser | None
) -> list[SearchResult]:
    tsquery = func.plainto_tsquery("simple", keyword)
    rbac = _rbac_filter(user)
    results: dict[uuid.UUID, SearchResult] = {}

    doc_vector = func.to_tsvector("simple", func.concat_ws(" ", Document.title, Document.author))
    for document_id, title, original_filename in db.execute(
        select(Document.id, Document.title, Document.original_filename).where(
            doc_vector.op("@@")(tsquery), rbac
        )
    ).all():
        results[document_id] = SearchResult(
            document_id=document_id,
            title=title or original_filename,
            snippet=title or original_filename,
        )

    page_vector = func.to_tsvector("simple", Page.text_content)
    headline = func.ts_headline(
        "simple", Page.text_content, tsquery, "MaxFragments=1, MaxWords=25, MinWords=10"
    )
    for document_id, title, original_filename, snippet in db.execute(
        select(Document.id, Document.title, Document.original_filename, headline)
        .join(Page, Page.document_id == Document.id)
        .where(page_vector.op("@@")(tsquery), rbac)
    ).all():
        results[document_id] = SearchResult(
            document_id=document_id,
            title=title or original_filename,
            snippet=_HEADLINE_MARKUP.sub("", snippet),
        )

    return list(results.values())


def _search_fallback(
    db: Session, keyword: str, user: AuthenticatedUser | None
) -> list[SearchResult]:
    needle = keyword.lower()
    rbac = _rbac_filter(user)
    results: dict[uuid.UUID, SearchResult] = {}

    for document in db.scalars(select(Document).where(rbac)).all():
        haystack = f"{document.title or ''} {document.author or ''}".lower()
        if needle in haystack:
            title = document.title or document.original_filename
            results[document.id] = SearchResult(document_id=document.id, title=title, snippet=title)

    for document_id, text_content, title, original_filename in db.execute(
        select(Page.document_id, Page.text_content, Document.title, Document.original_filename)
        .join(Document, Document.id == Page.document_id)
        .where(rbac)
    ).all():
        match_start = text_content.lower().find(needle)
        if match_start == -1:
            continue
        results[document_id] = SearchResult(
            document_id=document_id,
            title=title or original_filename,
            snippet=_make_snippet(text_content, match_start),
        )

    return list(results.values())
