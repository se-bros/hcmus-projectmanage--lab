"""M8 Identity & Access — owner: Tuấn Anh — LDMS-009, LDMS-010, LDMS-018.

Mock JWT dev-token, RBAC guard, Google OAuth 2.0 login.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])
