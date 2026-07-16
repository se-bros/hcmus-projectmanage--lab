"""M8 Identity & Access — owner: Tuấn Anh — LDMS-009, LDMS-010, LDMS-018.

Mock JWT dev-token, RBAC guard, Google OAuth 2.0 login.
"""

import uuid

from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from app.core.config import settings
from app.core.exceptions import NotFoundError
from app.core.security import create_access_token
from app.schemas.auth import DevTokenRequest, DevTokenResponse
from app.services.google_oauth_service import build_authorization_redirect, exchange_code_for_user

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/dev-token", response_model=DevTokenResponse)
def issue_dev_token(payload: DevTokenRequest) -> DevTokenResponse:
    if settings.auth_mode != "mock":
        raise NotFoundError("Mock auth is disabled; use Google OAuth login.")
    token = create_access_token(subject=str(uuid.uuid4()), role=payload.role)
    return DevTokenResponse(access_token=token, role=payload.role)


@router.get("/login/google")
def login_google() -> RedirectResponse:
    if settings.auth_mode != "google":
        raise NotFoundError("Google OAuth is disabled; use /auth/dev-token in mock mode.")
    return RedirectResponse(build_authorization_redirect(), status_code=307)


@router.get("/callback/google")
def callback_google(code: str, state: str | None = None) -> RedirectResponse:
    if settings.auth_mode != "google":
        raise NotFoundError("Google OAuth is disabled.")
    user = exchange_code_for_user(code, state)
    token = create_access_token(subject=user.sub, role="editor", email=user.email)
    return RedirectResponse(
        f"{settings.frontend_base_url}/auth/callback?token={token}", status_code=307
    )
