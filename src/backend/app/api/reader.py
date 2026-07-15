"""M6 Reader — owner: Khoa Nguyễn — LDMS-008, LDMS-014, LDMS-019, LDMS-020.

Đọc EPUB qua MinIO Signed URL (15 phút), tùy chỉnh giao diện đọc, bookmark.
"""

from fastapi import APIRouter

router = APIRouter(tags=["reader"])
