"""M8 Identity — Google OAuth 2.0 authorization-code flow (LDMS-018)."""

import secrets
import time
import uuid
from dataclasses import dataclass

from authlib.integrations.httpx_client import OAuth2Client

from app.core.config import settings
from app.core.exceptions import UnauthorizedError
from app.services.auth_service import check_allowed_domain

AUTHORIZATION_ENDPOINT = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"
USERINFO_ENDPOINT = "https://openidconnect.googleapis.com/v1/userinfo"
SCOPE = "openid email profile"
STATE_TTL_SECONDS = 300

_pending_states: dict[str, float] = {}


@dataclass
class GoogleUser:
    sub: str
    email: str
    name: str | None = None


def _new_client() -> OAuth2Client:
    return OAuth2Client(
        client_id=settings.google_client_id,
        client_secret=settings.google_client_secret,
        redirect_uri=settings.google_redirect_uri,
        scope=SCOPE,
    )


def build_authorization_redirect() -> str:
    state = secrets.token_urlsafe(24)
    _pending_states[state] = time.time() + STATE_TTL_SECONDS
    url, _ = _new_client().create_authorization_url(AUTHORIZATION_ENDPOINT, state=state)
    return url


def _consume_state(state: str | None) -> None:
    expires_at = _pending_states.pop(state or "", None)
    if expires_at is None or expires_at < time.time():
        raise UnauthorizedError("Invalid or expired OAuth state.")


def exchange_code_for_user(code: str, state: str | None) -> GoogleUser:
    _consume_state(state)
    client = _new_client()
    client.fetch_token(TOKEN_ENDPOINT, code=code)
    response = client.get(USERINFO_ENDPOINT)
    response.raise_for_status()
    payload = response.json()
    email = payload.get("email", "")
    check_allowed_domain(email)
    return GoogleUser(
        sub=payload.get("sub", str(uuid.uuid4())), email=email, name=payload.get("name")
    )
