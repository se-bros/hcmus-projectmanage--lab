from app.core.config import settings


def _register(client, email, password="supersecret", monkeypatch=None):
    if monkeypatch is not None:
        monkeypatch.setattr(settings, "google_allowed_domains", ["hcmus.edu.vn"])
    response = client.post("/auth/register", json={"email": email, "password": password})
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_reader_can_create_and_read_own_request(api_context, monkeypatch) -> None:
    client, _, _ = api_context
    headers = _register(client, "reader@hcmus.edu.vn", monkeypatch=monkeypatch)

    response = client.post("/role-requests", headers=headers)
    assert response.status_code == 201
    body = response.json()
    assert body["status"] == "pending"
    assert body["requested_role"] == "editor"
    assert body["user_email"] == "reader@hcmus.edu.vn"

    own = client.get("/role-requests/me", headers=headers)
    assert own.status_code == 200
    assert own.json()["status"] == "pending"


def test_second_pending_request_is_rejected(api_context, monkeypatch) -> None:
    client, _, _ = api_context
    headers = _register(client, "reader@hcmus.edu.vn", monkeypatch=monkeypatch)
    client.post("/role-requests", headers=headers)

    response = client.post("/role-requests", headers=headers)
    assert response.status_code == 409


def test_non_reader_cannot_create_request(api_context) -> None:
    client, _, _ = api_context
    token = client.post("/auth/dev-token", json={"role": "editor"}).json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.post("/role-requests", headers=headers)
    assert response.status_code == 404


def test_own_request_is_null_when_none_submitted(api_context, monkeypatch) -> None:
    client, _, _ = api_context
    headers = _register(client, "reader@hcmus.edu.vn", monkeypatch=monkeypatch)

    response = client.get("/role-requests/me", headers=headers)
    assert response.status_code == 200
    assert response.json() is None


def test_list_requests_requires_admin(api_context, monkeypatch) -> None:
    client, _, _ = api_context
    reader_headers = _register(client, "reader@hcmus.edu.vn", monkeypatch=monkeypatch)
    client.post("/role-requests", headers=reader_headers)

    forbidden = client.get("/role-requests", headers=reader_headers)
    assert forbidden.status_code == 403

    admin_token = client.post("/auth/dev-token", json={"role": "admin"}).json()["access_token"]
    admin_headers = {"Authorization": f"Bearer {admin_token}"}
    listed = client.get("/role-requests", headers=admin_headers)
    assert listed.status_code == 200
    assert len(listed.json()) == 1
    assert listed.json()[0]["user_email"] == "reader@hcmus.edu.vn"


def test_admin_approve_upgrades_role_and_allows_relogin_with_editor_role(
    api_context, monkeypatch
) -> None:
    client, _, _ = api_context
    reader_headers = _register(client, "reader@hcmus.edu.vn", monkeypatch=monkeypatch)
    request_id = client.post("/role-requests", headers=reader_headers).json()["id"]

    admin_token = client.post("/auth/dev-token", json={"role": "admin"}).json()["access_token"]
    admin_headers = {"Authorization": f"Bearer {admin_token}"}

    response = client.post(f"/role-requests/{request_id}/approve", headers=admin_headers)
    assert response.status_code == 200
    assert response.json()["status"] == "approved"

    relogin = client.post(
        "/auth/login", json={"email": "reader@hcmus.edu.vn", "password": "supersecret"}
    )
    assert relogin.json()["role"] == "editor"


def test_admin_decline_leaves_role_unchanged(api_context, monkeypatch) -> None:
    client, _, _ = api_context
    reader_headers = _register(client, "reader@hcmus.edu.vn", monkeypatch=monkeypatch)
    request_id = client.post("/role-requests", headers=reader_headers).json()["id"]

    admin_token = client.post("/auth/dev-token", json={"role": "admin"}).json()["access_token"]
    admin_headers = {"Authorization": f"Bearer {admin_token}"}

    response = client.post(f"/role-requests/{request_id}/decline", headers=admin_headers)
    assert response.status_code == 200
    assert response.json()["status"] == "rejected"

    relogin = client.post(
        "/auth/login", json={"email": "reader@hcmus.edu.vn", "password": "supersecret"}
    )
    assert relogin.json()["role"] == "reader"

    # A declined request doesn't block a fresh request.
    new_request = client.post("/role-requests", headers=reader_headers)
    assert new_request.status_code == 201


def test_deciding_an_already_decided_request_returns_conflict(api_context, monkeypatch) -> None:
    client, _, _ = api_context
    reader_headers = _register(client, "reader@hcmus.edu.vn", monkeypatch=monkeypatch)
    request_id = client.post("/role-requests", headers=reader_headers).json()["id"]

    admin_token = client.post("/auth/dev-token", json={"role": "admin"}).json()["access_token"]
    admin_headers = {"Authorization": f"Bearer {admin_token}"}
    client.post(f"/role-requests/{request_id}/approve", headers=admin_headers)

    response = client.post(f"/role-requests/{request_id}/decline", headers=admin_headers)
    assert response.status_code == 409
