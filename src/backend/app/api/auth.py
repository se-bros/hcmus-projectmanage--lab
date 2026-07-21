"""M8 Identity & Access — owner: Tuấn Anh — LDMS-009, LDMS-010, LDMS-018.

Mock JWT dev-token, local email/password JWT auth, RBAC guard, Google OAuth 2.0 login,
user profile (username/password) and Google auto-populated display name.
"""

import uuid
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse

from app.api.dependencies import DbSession
from app.core.config import settings
from app.core.exceptions import NotFoundError
from app.core.security import AuthenticatedUser, create_access_token, get_current_user
from app.models.user import User
from app.schemas.auth import (
    ChangePasswordRequest,
    DevTokenRequest,
    DevTokenResponse,
    LoginRequest,
    RegisterRequest,
    UpdateProfileRequest,
    UserProfile,
)
from app.services import auth_service
from app.services.google_oauth_service import build_authorization_redirect, exchange_code_for_user

router = APIRouter(prefix="/auth", tags=["auth"])


def _google_configured() -> bool:
    return bool(
        settings.google_client_id and settings.google_client_secret and settings.google_redirect_uri
    )


def _require_db_user(db: DbSession, user: AuthenticatedUser) -> User:
    db_user = auth_service.get_user_by_id(db, user.sub)
    if db_user is None:
        raise NotFoundError("No account found for this session.")
    return db_user


def _to_profile(db_user: User) -> UserProfile:
    return UserProfile(
        id=str(db_user.id),
        email=db_user.email,
        username=db_user.username,
        role=db_user.role,
        auth_provider=db_user.auth_provider,
        has_password=db_user.password_hash is not None,
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
    user = auth_service.find_or_create_google_user(db, google_user.email, google_user.name)
    token = create_access_token(subject=str(user.id), role=user.role, email=user.email)
    return RedirectResponse(
        f"{settings.frontend_base_url}/auth/callback?token={token}", status_code=307
    )


@router.get("/me", response_model=UserProfile)
def read_profile(
    db: DbSession,
    user: Annotated[AuthenticatedUser, Depends(get_current_user)],
) -> UserProfile:
    db_user = auth_service.get_user_by_id(db, user.sub)
    if db_user is None:
        return UserProfile(
            id=user.sub,
            email=user.email,
            username=None,
            role=user.role,
            auth_provider="mock",
            has_password=False,
        )
    return _to_profile(db_user)


@router.patch("/me", response_model=UserProfile)
def update_profile(
    payload: UpdateProfileRequest,
    db: DbSession,
    user: Annotated[AuthenticatedUser, Depends(get_current_user)],
) -> UserProfile:
    db_user = _require_db_user(db, user)
    db_user = auth_service.update_profile(db, db_user, payload.username)
    return _to_profile(db_user)


@router.post("/change-password", response_model=UserProfile)
def change_password(
    payload: ChangePasswordRequest,
    db: DbSession,
    user: Annotated[AuthenticatedUser, Depends(get_current_user)],
) -> UserProfile:
    db_user = _require_db_user(db, user)
    db_user = auth_service.change_password(
        db, db_user, payload.current_password, payload.new_password
    )
    return _to_profile(db_user)
