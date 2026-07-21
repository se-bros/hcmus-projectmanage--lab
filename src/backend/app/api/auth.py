"""M8 Identity & Access — owner: Tuấn Anh — LDMS-009, LDMS-010, LDMS-018.

Mock JWT dev-token, local email/password JWT auth, RBAC guard, Google OAuth 2.0 login.
"""

import uuid

from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from app.api.dependencies import DbSession
from app.core.config import settings
from app.core.exceptions import NotFoundError
from app.core.security import create_access_token
from app.schemas.auth import DevTokenRequest, DevTokenResponse, LoginRequest, RegisterRequest
from app.services import auth_service
from app.services.google_oauth_service import build_authorization_redirect, exchange_code_for_user

router = APIRouter(prefix="/auth", tags=["auth"])


def _google_configured() -> bool:
    return bool(
        settings.google_client_id and settings.google_client_secret and settings.google_redirect_uri
    )


@router.post("/dev-token", response_model=DevTokenResponse)
def issue_dev_token(payload: DevTokenRequest) -> DevTokenResponse:
    if not settings.enable_mock_auth:
        raise NotFoundError("Mock auth is disabled.")
    token = create_access_token(subject=str(uuid.uuid4()), role=payload.role)
    return DevTokenResponse(access_token=token, role=payload.role)


@router.post("/register", response_model=DevTokenResponse, status_code=201)
def register(payload: RegisterRequest, db: DbSession) -> DevTokenResponse:
    user = auth_service.register_local_user(db, payload.email, payload.password)
    token = create_access_token(subject=str(user.id), role=user.role, email=user.email)
    return DevTokenResponse(access_token=token, role=user.role)


@router.post("/login", response_model=DevTokenResponse)
def login(payload: LoginRequest, db: DbSession) -> DevTokenResponse:
    user = auth_service.authenticate_local_user(db, payload.email, payload.password)
    token = create_access_token(subject=str(user.id), role=user.role, email=user.email)
    return DevTokenResponse(access_token=token, role=user.role)


@router.post("/logout", status_code=204)
def logout() -> None:
    return None


@router.get("/login/google")
def login_google() -> RedirectResponse:
    if not _google_configured():
        raise NotFoundError("Google OAuth is not configured.")
    return RedirectResponse(build_authorization_redirect(), status_code=307)


@router.get("/callback/google")
def callback_google(code: str, db: DbSession, state: str | None = None) -> RedirectResponse:
    if not _google_configured():
        raise NotFoundError("Google OAuth is not configured.")
    google_user = exchange_code_for_user(code, state)
    user = auth_service.find_or_create_google_user(db, google_user.email)
    token = create_access_token(subject=str(user.id), role=user.role, email=user.email)
    return RedirectResponse(
        f"{settings.frontend_base_url}/auth/callback?token={token}", status_code=307
    )
