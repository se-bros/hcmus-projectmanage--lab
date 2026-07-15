"""M3 Editor — owner: Thái — LDMS-005, LDMS-006, LDMS-017.

Đọc/sửa text theo trang, UI biên tập, split-screen (ảnh scan + text OCR).
"""

from fastapi import APIRouter

router = APIRouter(prefix="/documents", tags=["editor"])
