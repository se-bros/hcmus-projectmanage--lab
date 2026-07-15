"""M5 Publish EPUB — owner: Khoa Ngô — LDMS-007, LDMS-013.

Đóng gói EPUB (Pandoc) và chặn xuất bản khi thiếu metadata.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/documents", tags=["publish"])
