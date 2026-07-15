"""M1 Documents & Storage — owner: Khoa Ngô (upload) / Khoa Nguyễn (list) — LDMS-002, LDMS-026.

Upload scan gốc lên MinIO, CRUD document, danh sách tài liệu.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/documents", tags=["documents"])
