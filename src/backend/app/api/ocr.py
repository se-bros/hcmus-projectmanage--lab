"""M2 OCR — owner: Khoa Ngô — LDMS-003, LDMS-004, LDMS-022.

Kích hoạt job OCR nền (FastAPI BackgroundTasks), trạng thái job, kết quả theo trang.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/documents", tags=["ocr"])
