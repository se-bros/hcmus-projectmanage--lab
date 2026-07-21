from app.core.config import settings


def _register(client, email="student@hcmus.edu.vn", password="supersecret", monkeypatch=None):
    if monkeypatch is not None:
        monkeypatch.setattr(settings, "google_allowed_domains", ["hcmus.edu.vn"])
    response = client.post("/auth/register", json={"email": email, "password": password})
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_read_profile_for_local_user(api_context, monkeypatch) -> None:
    client, _, _ = api_context
    headers = _register(client, monkeypatch=monkeypatch)

    response = client.get("/auth/me", headers=headers)

    assert response.status_code == 200
    body = response.json()
    assert body["email"] == "student@hcmus.edu.vn"
    assert body["username"] is None
    assert body["role"] == "reader"
    assert body["auth_provider"] == "local"
    assert body["has_password"] is True


def test_read_profile_for_mock_token_returns_synthesized_profile(api_context) -> None:
    client, _, _ = api_context
    token = client.post("/auth/dev-token", json={"role": "editor"}).json()["access_token"]

    response = client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    body = response.json()
    assert body["username"] is None
    assert body["role"] == "editor"
    assert body["auth_provider"] == "mock"
    assert body["has_password"] is False


def test_update_profile_sets_username(api_context, monkeypatch) -> None:
    client, _, _ = api_context
    headers = _register(client, monkeypatch=monkeypatch)

    response = client.patch("/auth/me", json={"username": "New Name"}, headers=headers)

    assert response.status_code == 200
    assert response.json()["username"] == "New Name"
    assert client.get("/auth/me", headers=headers).json()["username"] == "New Name"


def test_update_profile_rejected_for_mock_token(api_context) -> None:
    client, _, _ = api_context
    token = client.post("/auth/dev-token", json={"role": "reader"}).json()["access_token"]

    response = client.patch(
        "/auth/me", json={"username": "New Name"}, headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 404


def test_change_password_requires_correct_current_password(api_context, monkeypatch) -> None:
    client, _, _ = api_context
    headers = _register(client, monkeypatch=monkeypatch)

    wrong = client.post(
        "/auth/change-password",
        json={"current_password": "wrong", "new_password": "newsecret1"},
        headers=headers,
    )
    assert wrong.status_code == 401

    correct = client.post(
        "/auth/change-password",
        json={"current_password": "supersecret", "new_password": "newsecret1"},
        headers=headers,
    )
    assert correct.status_code == 200

    relogin = client.post(
        "/auth/login", json={"email": "student@hcmus.edu.vn", "password": "newsecret1"}
    )
    assert relogin.status_code == 200


def test_change_password_for_google_only_account_does_not_require_current_password(
    api_context, monkeypatch
) -> None:
    client, _, _ = api_context
    monkeypatch.setattr(settings, "google_client_id", "client-id")
    monkeypatch.setattr(settings, "google_client_secret", "client-secret")
    monkeypatch.setattr(
        settings, "google_redirect_uri", "http://localhost:8000/auth/callback/google"
    )
    monkeypatch.setattr(settings, "google_allowed_domains", ["hcmus.edu.vn"])

    from app.api import auth as auth_router

    class FakeUser:
        sub = "google-1"
        email = "googleuser@hcmus.edu.vn"
        name = "Google User"

    monkeypatch.setattr(auth_router, "exchange_code_for_user", lambda code, state: FakeUser())
    callback = client.get(
        "/auth/callback/google", params={"code": "abc", "state": "xyz"}, follow_redirects=False
    )
    token = callback.headers["location"].split("token=", 1)[1]
    headers = {"Authorization": f"Bearer {token}"}

    assert client.get("/auth/me", headers=headers).json()["has_password"] is False

    response = client.post(
        "/auth/change-password", json={"new_password": "brandnewpass"}, headers=headers
    )
    assert response.status_code == 200
    assert response.json()["has_password"] is True

    relogin = client.post(
        "/auth/login", json={"email": "googleuser@hcmus.edu.vn", "password": "brandnewpass"}
    )
    assert relogin.status_code == 200
