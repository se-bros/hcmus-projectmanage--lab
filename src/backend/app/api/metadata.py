"""M4 Metadata — owner: Thái — LDMS-011, LDMS-012.

Gán metadata bắt buộc (title/author/shelf_location), cây category 2 cấp.
"""

from fastapi import APIRouter

router = APIRouter(tags=["metadata"])
