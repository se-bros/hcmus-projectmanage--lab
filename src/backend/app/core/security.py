"""M8 Identity — owner: Tuấn Anh — LDMS-009, LDMS-018.

JWT issuance/verification shared by Mock dev-token and Google OAuth, plus
FastAPI dependencies for optional/required auth and role-based guards.
"""

from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from typing import Annotated

import jwt
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.config import settings
from app.core.exceptions import ForbiddenError, UnauthorizedError

_bearer_scheme = HTTPBearer(auto_error=False)


@dataclass
class AuthenticatedUser:
    sub: str
    role: str
    email: str | None = None


def create_access_token(subject: str, role: str, email: str | None = None) -> str:
    now = datetime.now(UTC)
    payload = {
        "sub": subject,
        "role": role,
        "email": email,
        "iat": now,
        "exp": now + timedelta(minutes=settings.jwt_expires_minutes),
    }
    return jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_algorithm)


def _decode(token: str) -> AuthenticatedUser:
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
    except jwt.PyJWTError as exc:
        raise UnauthorizedError("Invalid or expired access token.") from exc
    return AuthenticatedUser(sub=payload["sub"], role=payload["role"], email=payload.get("email"))


def get_optional_user(
    credentials: Annotated[HTTPAuthorizationCredentials | None, Depends(_bearer_scheme)],
) -> AuthenticatedUser | None:
    if credentials is None:
        return None
    return _decode(credentials.credentials)


def get_current_user(
    user: Annotated[AuthenticatedUser | None, Depends(get_optional_user)],
) -> AuthenticatedUser:
    if user is None:
        raise UnauthorizedError("Missing or invalid access token.")
    return user


def require_roles(*roles: str) -> Callable[..., AuthenticatedUser]:
    def dependency(
        user: Annotated[AuthenticatedUser, Depends(get_current_user)],
    ) -> AuthenticatedUser:
        if user.role not in roles:
            raise ForbiddenError(f"Role '{user.role}' is not permitted for this action.")
        return user

    return dependency
