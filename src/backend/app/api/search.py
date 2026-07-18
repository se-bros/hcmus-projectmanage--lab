"""M7 Search — owner: Khoa Nguyễn — LDMS-015, LDMS-016.

Tìm kiếm toàn văn (PostgreSQL FTS) và snippet kết quả.
"""

from typing import Annotated

from fastapi import APIRouter, Depends

from app.api.dependencies import DbSession
from app.core.security import AuthenticatedUser, get_optional_user
from app.schemas.document import SearchResult
from app.services.search_service import search_documents

router = APIRouter(prefix="/search", tags=["search"])


@router.get("", response_model=list[SearchResult])
def search(
    db: DbSession,
    user: Annotated[AuthenticatedUser | None, Depends(get_optional_user)],
    q: str = "",
) -> list[SearchResult]:
    return search_documents(db, q, user)
