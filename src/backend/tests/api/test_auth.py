import jwt as pyjwt
from sqlalchemy import select

from app.api import auth as auth_router
from app.core.config import settings
from app.models.user import User


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


def test_dev_token_disabled_when_mock_auth_off(api_context, monkeypatch) -> None:
    client, _, _ = api_context
    monkeypatch.setattr(settings, "enable_mock_auth", False)
    response = client.post("/auth/dev-token", json={"role": "editor"})
    assert response.status_code == 404


def test_register_creates_reader_and_returns_jwt(api_context, monkeypatch) -> None:
    client, _, _ = api_context
    monkeypatch.setattr(settings, "google_allowed_domains", ["hcmus.edu.vn"])

    response = client.post(
        "/auth/register", json={"email": "student@hcmus.edu.vn", "password": "supersecret"}
    )

    assert response.status_code == 201
    body = response.json()
    assert body["role"] == "reader"
    payload = pyjwt.decode(
        body["access_token"], settings.jwt_secret, algorithms=[settings.jwt_algorithm]
    )
    assert payload["email"] == "student@hcmus.edu.vn"
    assert payload["role"] == "reader"


def test_register_rejects_duplicate_email(api_context, monkeypatch) -> None:
    client, _, _ = api_context
    monkeypatch.setattr(settings, "google_allowed_domains", ["hcmus.edu.vn"])
    body = {"email": "student@hcmus.edu.vn", "password": "supersecret"}

    client.post("/auth/register", json=body)
    response = client.post("/auth/register", json=body)

    assert response.status_code == 409


def test_register_rejects_disallowed_domain(api_context, monkeypatch) -> None:
    client, _, _ = api_context
    monkeypatch.setattr(settings, "google_allowed_domains", ["hcmus.edu.vn"])

    response = client.post(
        "/auth/register", json={"email": "student@gmail.com", "password": "supersecret"}
    )

    assert response.status_code == 403


def test_register_rejects_short_password(api_context, monkeypatch) -> None:
    client, _, _ = api_context
    monkeypatch.setattr(settings, "google_allowed_domains", ["hcmus.edu.vn"])

    response = client.post(
        "/auth/register", json={"email": "student@hcmus.edu.vn", "password": "short"}
    )

    assert response.status_code == 422


def test_login_returns_jwt_for_correct_credentials(api_context, monkeypatch) -> None:
    client, _, _ = api_context
    monkeypatch.setattr(settings, "google_allowed_domains", ["hcmus.edu.vn"])
    client.post("/auth/register", json={"email": "student@hcmus.edu.vn", "password": "supersecret"})

    response = client.post(
        "/auth/login", json={"email": "student@hcmus.edu.vn", "password": "supersecret"}
    )

    assert response.status_code == 200
    assert response.json()["role"] == "reader"


def test_login_rejects_wrong_password(api_context, monkeypatch) -> None:
    client, _, _ = api_context
    monkeypatch.setattr(settings, "google_allowed_domains", ["hcmus.edu.vn"])
    client.post("/auth/register", json={"email": "student@hcmus.edu.vn", "password": "supersecret"})

    response = client.post(
        "/auth/login", json={"email": "student@hcmus.edu.vn", "password": "wrongpass"}
    )

    assert response.status_code == 401


def test_logout_returns_no_content(api_context) -> None:
    client, _, _ = api_context
    response = client.post("/auth/logout")
    assert response.status_code == 204


def test_google_login_returns_404_when_not_configured(api_context, monkeypatch) -> None:
    client, _, _ = api_context
    monkeypatch.setattr(settings, "google_client_id", None)
    monkeypatch.setattr(settings, "google_client_secret", None)
    monkeypatch.setattr(settings, "google_redirect_uri", None)
    response = client.get("/auth/login/google", follow_redirects=False)
    assert response.status_code == 404


def test_google_login_redirects_when_configured(api_context, monkeypatch) -> None:
    client, _, _ = api_context
    monkeypatch.setattr(settings, "google_client_id", "client-id")
    monkeypatch.setattr(settings, "google_client_secret", "client-secret")
    monkeypatch.setattr(
        settings, "google_redirect_uri", "http://localhost:8000/auth/callback/google"
    )

    response = client.get("/auth/login/google", follow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"].startswith("https://accounts.google.com")


def test_google_callback_issues_jwt_with_reader_role_for_new_user(api_context, monkeypatch) -> None:
    client, _, _ = api_context
    monkeypatch.setattr(settings, "google_client_id", "client-id")
    monkeypatch.setattr(settings, "google_client_secret", "client-secret")
    monkeypatch.setattr(
        settings, "google_redirect_uri", "http://localhost:8000/auth/callback/google"
    )

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
    assert payload["role"] == "reader"
    assert payload["email"] == "student@hcmus.edu.vn"


def test_google_callback_reuses_existing_users_role(api_context, monkeypatch) -> None:
    client, testing_session, _ = api_context
    monkeypatch.setattr(settings, "google_client_id", "client-id")
    monkeypatch.setattr(settings, "google_client_secret", "client-secret")
    monkeypatch.setattr(
        settings, "google_redirect_uri", "http://localhost:8000/auth/callback/google"
    )
    monkeypatch.setattr(settings, "google_allowed_domains", ["hcmus.edu.vn"])
    client.post("/auth/register", json={"email": "editor@hcmus.edu.vn", "password": "supersecret"})
    with testing_session() as db:
        user = db.scalar(select(User).where(User.email == "editor@hcmus.edu.vn"))
        user.role = "editor"
        db.commit()

    class FakeUser:
        sub = "google-999"
        email = "editor@hcmus.edu.vn"

    monkeypatch.setattr(auth_router, "exchange_code_for_user", lambda code, state: FakeUser())

    response = client.get(
        "/auth/callback/google", params={"code": "abc", "state": "xyz"}, follow_redirects=False
    )
    token = response.headers["location"].split("token=", 1)[1]
    payload = pyjwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
    assert payload["role"] == "editor"
