"""M7 Search — owner: Khoa Nguyễn — LDMS-015, LDMS-016.

Tìm kiếm toàn văn (PostgreSQL FTS) và snippet kết quả.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/search", tags=["search"])
