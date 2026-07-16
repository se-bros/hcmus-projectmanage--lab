import jwt as pyjwt

from app.api import auth as auth_router
from app.core.config import settings


def test_dev_token_issues_valid_jwt_with_role(api_context) -> None:
    client, _, _ = api_context
    response = client.post("/auth/dev-token", json={"role": "editor"})

    assert response.status_code == 200
    body = response.json()
    assert body["role"] == "editor"
    payload = pyjwt.decode(
        body["access_token"], settings.jwt_secret, algorithms=[settings.jwt_algorithm]
    )
    assert payload["role"] == "editor"
    assert payload["sub"]


def test_dev_token_defaults_to_reader_role(api_context) -> None:
    client, _, _ = api_context
    response = client.post("/auth/dev-token", json={})

    assert response.status_code == 200
    assert response.json()["role"] == "reader"


def test_dev_token_rejects_unknown_role(api_context) -> None:
    client, _, _ = api_context
    response = client.post("/auth/dev-token", json={"role": "superadmin"})

    assert response.status_code == 422


def test_google_login_disabled_in_mock_mode(api_context) -> None:
    client, _, _ = api_context
    response = client.get("/auth/login/google", follow_redirects=False)
    assert response.status_code == 404


def test_google_login_redirects_when_enabled(api_context, monkeypatch) -> None:
    client, _, _ = api_context
    monkeypatch.setattr(settings, "auth_mode", "google")
    monkeypatch.setattr(settings, "google_client_id", "client-id")
    monkeypatch.setattr(settings, "google_client_secret", "client-secret")
    monkeypatch.setattr(
        settings, "google_redirect_uri", "http://localhost:8000/auth/callback/google"
    )

    response = client.get("/auth/login/google", follow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"].startswith("https://accounts.google.com")


def test_google_callback_issues_jwt_and_redirects_to_frontend(api_context, monkeypatch) -> None:
    client, _, _ = api_context
    monkeypatch.setattr(settings, "auth_mode", "google")

    class FakeUser:
        sub = "google-789"
        email = "student@hcmus.edu.vn"

    monkeypatch.setattr(auth_router, "exchange_code_for_user", lambda code, state: FakeUser())

    response = client.get(
        "/auth/callback/google", params={"code": "abc", "state": "xyz"}, follow_redirects=False
    )
    assert response.status_code == 307
    location = response.headers["location"]
    assert location.startswith(f"{settings.frontend_base_url}/auth/callback?token=")
    token = location.split("token=", 1)[1]
    payload = pyjwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
    assert payload["role"] == "editor"
    assert payload["email"] == "student@hcmus.edu.vn"


def test_dev_token_disabled_in_google_mode(api_context, monkeypatch) -> None:
    client, _, _ = api_context
    monkeypatch.setattr(settings, "auth_mode", "google")
    response = client.post("/auth/dev-token", json={"role": "editor"})
    assert response.status_code == 404
