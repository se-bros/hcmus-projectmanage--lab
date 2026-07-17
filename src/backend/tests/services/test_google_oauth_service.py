import httpx
import pytest

from app.core.config import settings
from app.core.exceptions import ForbiddenError, UnauthorizedError
from app.services import google_oauth_service as svc


@pytest.fixture(autouse=True)
def _google_settings(monkeypatch):
    monkeypatch.setattr(settings, "google_client_id", "client-id")
    monkeypatch.setattr(settings, "google_client_secret", "client-secret")
    monkeypatch.setattr(
        settings, "google_redirect_uri", "http://localhost:8000/auth/callback/google"
    )
    monkeypatch.setattr(settings, "google_allowed_domains", ["hcmus.edu.vn", "clc.fitus.edu.vn"])
    svc._pending_states.clear()


def test_build_authorization_redirect_registers_state_and_targets_google():
    url = svc.build_authorization_redirect()
    assert url.startswith("https://accounts.google.com/o/oauth2/v2/auth")
    assert len(svc._pending_states) == 1


def test_exchange_code_for_user_rejects_unknown_state():
    with pytest.raises(UnauthorizedError):
        svc.exchange_code_for_user("some-code", "unknown-state")


def test_exchange_code_for_user_accepts_hcmus_email(monkeypatch):
    url = svc.build_authorization_redirect()
    state = next(iter(svc._pending_states))
    assert state in url

    def fake_fetch_token(self, *args, **kwargs):
        return {"access_token": "fake"}

    def fake_get(self, *args, **kwargs):
        return httpx.Response(
            200,
            json={"sub": "google-123", "email": "student@hcmus.edu.vn"},
            request=httpx.Request("GET", svc.USERINFO_ENDPOINT),
        )

    monkeypatch.setattr(svc.OAuth2Client, "fetch_token", fake_fetch_token)
    monkeypatch.setattr(svc.OAuth2Client, "get", fake_get)

    user = svc.exchange_code_for_user("some-code", state)
    assert user.sub == "google-123"
    assert user.email == "student@hcmus.edu.vn"
    assert state not in svc._pending_states


def test_exchange_code_for_user_accepts_second_allowed_domain(monkeypatch):
    url = svc.build_authorization_redirect()
    state = next(iter(svc._pending_states))
    assert url

    def fake_fetch_token(self, *args, **kwargs):
        return {"access_token": "fake"}

    def fake_get(self, *args, **kwargs):
        return httpx.Response(
            200,
            json={"sub": "google-789", "email": "ntanh23@clc.fitus.edu.vn"},
            request=httpx.Request("GET", svc.USERINFO_ENDPOINT),
        )

    monkeypatch.setattr(svc.OAuth2Client, "fetch_token", fake_fetch_token)
    monkeypatch.setattr(svc.OAuth2Client, "get", fake_get)

    user = svc.exchange_code_for_user("some-code", state)
    assert user.email == "ntanh23@clc.fitus.edu.vn"


def test_exchange_code_for_user_rejects_non_hcmus_email(monkeypatch):
    url = svc.build_authorization_redirect()
    state = next(iter(svc._pending_states))
    assert url

    def fake_fetch_token(self, *args, **kwargs):
        return {"access_token": "fake"}

    def fake_get(self, *args, **kwargs):
        return httpx.Response(
            200,
            json={"sub": "google-456", "email": "someone@gmail.com"},
            request=httpx.Request("GET", svc.USERINFO_ENDPOINT),
        )

    monkeypatch.setattr(svc.OAuth2Client, "fetch_token", fake_fetch_token)
    monkeypatch.setattr(svc.OAuth2Client, "get", fake_get)

    with pytest.raises(ForbiddenError):
        svc.exchange_code_for_user("some-code", state)
