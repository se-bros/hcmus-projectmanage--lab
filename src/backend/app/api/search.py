"""M7 Search — owner: Khoa Nguyễn — LDMS-015, LDMS-016.

Tìm kiếm toàn văn (PostgreSQL FTS) và snippet kết quả.
"""

from fastapi import APIRouter

from app.fixtures.documents import DOCUMENT_CONTENTS, DOCUMENTS
from app.schemas.document import SearchResult

router = APIRouter(prefix="/search", tags=["search"])

_SNIPPET_RADIUS = 40
_TITLES = {doc.id: doc.title for doc in DOCUMENTS}


def _make_snippet(text: str, match_start: int) -> str:
    start = max(0, match_start - _SNIPPET_RADIUS)
    end = min(len(text), match_start + _SNIPPET_RADIUS)
    snippet = text[start:end].strip()
    prefix = "…" if start > 0 else ""
    suffix = "…" if end < len(text) else ""
    return f"{prefix}{snippet}{suffix}"


@router.get("", response_model=list[SearchResult])
def search_documents(q: str = "") -> list[SearchResult]:
    keyword = q.strip().lower()
    if not keyword:
        return []
    results: list[SearchResult] = []
    for document_id, text in DOCUMENT_CONTENTS.items():
        match_start = text.lower().find(keyword)
        if match_start == -1:
            continue
        results.append(
            SearchResult(
                document_id=document_id,
                title=_TITLES.get(document_id, document_id),
                snippet=_make_snippet(text, match_start),
            )
        )
    return results
