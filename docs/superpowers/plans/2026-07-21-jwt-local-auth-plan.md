# JWT Local Authentication (Register/Login/Logout) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add real, persisted-account JWT authentication (register/login/logout) that runs alongside the existing Google OAuth login, sharing one `users` table and one role model.

**Architecture:** A new `users` table backs both local (email/password) and Google-authenticated identities. A `find_or_create_google_user` lookup makes Google logins reuse the same row as a matching local account, so role is consistent regardless of login method. `AUTH_MODE` (mock XOR google) is replaced by an always-on Google route plus an independent `ENABLE_MOCK_AUTH` flag for the dev-token endpoint. Logout is stateless (client discards the token).

**Tech Stack:** FastAPI, SQLAlchemy 2.0 (declarative `Mapped`/`mapped_column`), Alembic, PyJWT (existing), bcrypt (new), React 19, react-router, vitest + Testing Library.

**Spec:** `docs/superpowers/specs/2026-07-21-jwt-local-auth-design.md`

## Global Constraints

- New backend dependency: `bcrypt` (added via `uv add bcrypt`). No `passlib`, no `pydantic.EmailStr`/`email-validator` — keep the dependency footprint minimal, matching the existing codebase's total absence of an email-validation library.
- Password rule: minimum 8 characters, maximum 72 bytes (bcrypt silently truncates beyond 72 bytes — capping in the schema avoids a silent-truncation correctness bug).
- Both local registration and Google login default new accounts to role `reader`. This is a deliberate behavior change from the current hardcoded `role="editor"` on Google login.
- `AUTH_MODE` config key is removed entirely. Google OAuth and local JWT (register/login/logout) are always routable; only the mock dev-token endpoint is flag-gated, via new `ENABLE_MOCK_AUTH` (default `true`).
- Local registration is restricted to the same domain allowlist as Google (`GOOGLE_ALLOWED_DOMAINS`), enforced by one shared `check_allowed_domain()` function — do not duplicate the domain-check logic.
- `/auth/logout` is stateless: `204 No Content`, no server-side revocation, no new storage.
- Follow existing codebase conventions: no repository class for `User` (mirrors `category_service.py`'s direct `db.scalar(select(...))`/`db.add`/`db.commit()` style, not `document_repository.py`'s class-based style — `User` has no external side effects like MinIO that would justify a repository layer).
- Every modified Python file must stay `ruff format`/`ruff check` clean; every modified TS/TSX file must stay `prettier`/`oxlint` clean.

---

## Task 1: `User` model + Alembic migration

**Files:**
- Create: `src/backend/app/models/user.py`
- Modify: `src/backend/app/models/__init__.py`
- Create: `src/backend/app/db/migrations/versions/20260721_0006_users.py`

**Interfaces:**
- Produces: `app.models.user.User` — SQLAlchemy model with `id: uuid.UUID`, `email: str`, `password_hash: str | None`, `role: str`, `auth_provider: str`, `created_at: datetime`. Later tasks construct it as `User(id=uuid.uuid4(), email=..., password_hash=..., role=..., auth_provider=...)`.

- [ ] **Step 1: Write the model**

Create `src/backend/app/models/user.py`:

```python
from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(320), unique=True)
    password_hash: Mapped[str | None] = mapped_column(String(255), nullable=True)
    role: Mapped[str] = mapped_column(String(32), default="reader", server_default="reader")
    auth_provider: Mapped[str] = mapped_column(String(32))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
```

- [ ] **Step 2: Register the model in the package `__init__`**

Modify `src/backend/app/models/__init__.py` to:

```python
from app.models.category import Category
from app.models.document import Document
from app.models.ocr_job import OcrJob
from app.models.page import Page
from app.models.publish_job import PublishJob
from app.models.user import User

__all__ = ["Category", "Document", "OcrJob", "Page", "PublishJob", "User"]
```

- [ ] **Step 3: Write the migration**

Create `src/backend/app/db/migrations/versions/20260721_0006_users.py`:

```python
"""create users table

Revision ID: 20260721_0006
Revises: 20260716_0005
Create Date: 2026-07-21
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "20260721_0006"
down_revision: str | None = "20260716_0005"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("email", sa.String(length=320), nullable=False),
        sa.Column("password_hash", sa.String(length=255), nullable=True),
        sa.Column("role", sa.String(length=32), server_default="reader", nullable=False),
        sa.Column("auth_provider", sa.String(length=32), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )


def downgrade() -> None:
    op.drop_table("users")
```

- [ ] **Step 4: Verify the migration is syntactically valid (offline dry-run, no DB needed)**

Run (from `src/backend`): `uv run alembic upgrade head --sql`
Expected: prints `CREATE TABLE users (...)` SQL for all pending revisions ending in the new `users` table, with no traceback.

- [ ] **Step 5: Verify the model loads and creates a table under SQLite**

Run (from `src/backend`):
```bash
uv run python -c "
from sqlalchemy import create_engine
from app.db.base import Base
from app import models  # noqa: F401
engine = create_engine('sqlite://')
Base.metadata.create_all(engine)
print('users' in Base.metadata.tables)
"
```
Expected: prints `True`.

- [ ] **Step 6: Format, lint, commit**

```bash
cd src/backend && uv run ruff format app/models/user.py app/models/__init__.py app/db/migrations/versions/20260721_0006_users.py
uv run ruff check app/models/user.py app/models/__init__.py app/db/migrations/versions/20260721_0006_users.py
cd ../.. && git add src/backend/app/models/user.py src/backend/app/models/__init__.py src/backend/app/db/migrations/versions/20260721_0006_users.py
git commit -m "feat(backend): add users table for local + Google identity"
```

---

## Task 2: Password hashing helpers (bcrypt)

**Files:**
- Modify: `src/backend/app/core/security.py`
- Modify: `src/backend/pyproject.toml` (via `uv add`)
- Test: `src/backend/tests/core/test_security.py` (new)

**Interfaces:**
- Consumes: nothing new.
- Produces: `hash_password(password: str) -> str`, `verify_password(password: str, password_hash: str) -> bool` in `app.core.security`. Task 3's `auth_service.py` imports both.

- [ ] **Step 1: Add the bcrypt dependency**

```bash
cd src/backend && uv add bcrypt
```
Expected: `pyproject.toml` gains a `bcrypt>=...` line under `dependencies`, `uv.lock` updates.

- [ ] **Step 2: Write the failing test**

Create `src/backend/tests/core/__init__.py` (empty file) and `src/backend/tests/core/test_security.py`:

```python
from app.core.security import hash_password, verify_password


def test_hash_password_does_not_return_the_plaintext():
    hashed = hash_password("supersecret")
    assert hashed != "supersecret"


def test_verify_password_accepts_the_correct_password():
    hashed = hash_password("supersecret")
    assert verify_password("supersecret", hashed) is True


def test_verify_password_rejects_the_wrong_password():
    hashed = hash_password("supersecret")
    assert verify_password("wrong-password", hashed) is False


def test_hash_password_is_salted_and_nondeterministic():
    assert hash_password("supersecret") != hash_password("supersecret")
```

- [ ] **Step 3: Run the tests to verify they fail**

Run: `cd src/backend && uv run pytest tests/core/test_security.py -v`
Expected: `ImportError: cannot import name 'hash_password'` (function doesn't exist yet).

- [ ] **Step 4: Implement the helpers**

In `src/backend/app/core/security.py`, add `import bcrypt` to the imports at the top, then add these two functions right after the `_bearer_scheme = HTTPBearer(auto_error=False)` line and before the `@dataclass` block:

```python
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(password: str, password_hash: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), password_hash.encode("utf-8"))
```

- [ ] **Step 5: Run the tests to verify they pass**

Run: `cd src/backend && uv run pytest tests/core/test_security.py -v`
Expected: 4 passed.

- [ ] **Step 6: Format, lint, commit**

```bash
cd src/backend && uv run ruff format app/core/security.py tests/core/test_security.py
uv run ruff check app/core/security.py tests/core/test_security.py
cd ../.. && git add src/backend/app/core/security.py src/backend/tests/core/__init__.py src/backend/tests/core/test_security.py src/backend/pyproject.toml src/backend/uv.lock
git commit -m "feat(backend): add bcrypt password hashing helpers"
```

---

## Task 3: `auth_service.py` (register/authenticate/find-or-create) + shared domain check

**Files:**
- Create: `src/backend/app/services/auth_service.py`
- Modify: `src/backend/app/services/google_oauth_service.py`
- Test: `src/backend/tests/services/test_auth_service.py` (new)

**Interfaces:**
- Consumes: `hash_password`/`verify_password` from Task 2, `User` model from Task 1, `settings.google_allowed_domains` from `app.core.config`.
- Produces (used by Task 5's API layer):
  - `check_allowed_domain(email: str) -> None` — raises `ForbiddenError` if the email's domain isn't in `settings.google_allowed_domains`.
  - `register_local_user(db: Session, email: str, password: str) -> User` — raises `ForbiddenError` (bad domain) or `ConflictError` (email taken).
  - `authenticate_local_user(db: Session, email: str, password: str) -> User` — raises `UnauthorizedError` on any mismatch (unknown email, Google-only account, wrong password).
  - `find_or_create_google_user(db: Session, email: str) -> User` — never raises for a valid Google email; returns the existing row if the email is already registered (local or google), otherwise creates a `role="reader"`, `auth_provider="google"` row.

- [ ] **Step 1: Write the failing tests**

Create `src/backend/tests/services/test_auth_service.py`:

```python
import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.exceptions import ConflictError, ForbiddenError, UnauthorizedError
from app.db.base import Base
from app.models.user import User
from app.services import auth_service


@pytest.fixture(autouse=True)
def _allowed_domains(monkeypatch):
    monkeypatch.setattr(settings, "google_allowed_domains", ["hcmus.edu.vn"])


def _db() -> Session:
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    return Session(engine)


def test_register_local_user_creates_reader_with_hashed_password():
    with _db() as db:
        user = auth_service.register_local_user(db, "student@hcmus.edu.vn", "supersecret")
        assert user.role == "reader"
        assert user.auth_provider == "local"
        assert user.password_hash != "supersecret"


def test_register_local_user_rejects_disallowed_domain():
    with _db() as db:
        with pytest.raises(ForbiddenError):
            auth_service.register_local_user(db, "student@gmail.com", "supersecret")


def test_register_local_user_rejects_duplicate_email():
    with _db() as db:
        auth_service.register_local_user(db, "student@hcmus.edu.vn", "supersecret")
        with pytest.raises(ConflictError):
            auth_service.register_local_user(db, "student@hcmus.edu.vn", "anotherpass")


def test_authenticate_local_user_accepts_correct_password():
    with _db() as db:
        auth_service.register_local_user(db, "student@hcmus.edu.vn", "supersecret")
        user = auth_service.authenticate_local_user(db, "student@hcmus.edu.vn", "supersecret")
        assert user.email == "student@hcmus.edu.vn"


def test_authenticate_local_user_rejects_wrong_password():
    with _db() as db:
        auth_service.register_local_user(db, "student@hcmus.edu.vn", "supersecret")
        with pytest.raises(UnauthorizedError):
            auth_service.authenticate_local_user(db, "student@hcmus.edu.vn", "wrongpass")


def test_authenticate_local_user_rejects_unknown_email():
    with _db() as db:
        with pytest.raises(UnauthorizedError):
            auth_service.authenticate_local_user(db, "nobody@hcmus.edu.vn", "supersecret")


def test_authenticate_local_user_rejects_google_only_account():
    with _db() as db:
        auth_service.find_or_create_google_user(db, "student@hcmus.edu.vn")
        with pytest.raises(UnauthorizedError):
            auth_service.authenticate_local_user(db, "student@hcmus.edu.vn", "anything")


def test_find_or_create_google_user_creates_reader_first_time():
    with _db() as db:
        user = auth_service.find_or_create_google_user(db, "student@hcmus.edu.vn")
        assert user.role == "reader"
        assert user.auth_provider == "google"
        assert user.password_hash is None


def test_find_or_create_google_user_reuses_existing_local_identity():
    with _db() as db:
        local_user = auth_service.register_local_user(db, "student@hcmus.edu.vn", "supersecret")
        google_user = auth_service.find_or_create_google_user(db, "student@hcmus.edu.vn")
        assert google_user.id == local_user.id
        assert google_user.auth_provider == "local"


def test_check_allowed_domain_rejects_non_allowed_domain():
    with pytest.raises(ForbiddenError):
        auth_service.check_allowed_domain("someone@gmail.com")


def test_check_allowed_domain_accepts_allowed_domain():
    auth_service.check_allowed_domain("someone@hcmus.edu.vn")  # does not raise


def test_registered_user_is_queryable_by_email(_db_session=None):
    with _db() as db:
        auth_service.register_local_user(db, "student@hcmus.edu.vn", "supersecret")
        assert db.scalar(select(User).where(User.email == "student@hcmus.edu.vn")) is not None
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `cd src/backend && uv run pytest tests/services/test_auth_service.py -v`
Expected: `ModuleNotFoundError: No module named 'app.services.auth_service'`.

- [ ] **Step 3: Implement `auth_service.py`**

Create `src/backend/app/services/auth_service.py`:

```python
import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.exceptions import ConflictError, ForbiddenError, UnauthorizedError
from app.core.security import hash_password, verify_password
from app.models.user import User

DEFAULT_ROLE = "reader"


def check_allowed_domain(email: str) -> None:
    if not any(email.lower().endswith(f"@{domain}") for domain in settings.google_allowed_domains):
        allowed = ", ".join(f"@{domain}" for domain in settings.google_allowed_domains)
        raise ForbiddenError(f"Only {allowed} accounts are allowed.")


def register_local_user(db: Session, email: str, password: str) -> User:
    check_allowed_domain(email)
    if db.scalar(select(User).where(User.email == email)) is not None:
        raise ConflictError("An account with this email already exists.")
    user = User(
        id=uuid.uuid4(),
        email=email,
        password_hash=hash_password(password),
        role=DEFAULT_ROLE,
        auth_provider="local",
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_local_user(db: Session, email: str, password: str) -> User:
    user = db.scalar(select(User).where(User.email == email))
    if user is None or user.password_hash is None or not verify_password(
        password, user.password_hash
    ):
        raise UnauthorizedError("Invalid email or password.")
    return user


def find_or_create_google_user(db: Session, email: str) -> User:
    user = db.scalar(select(User).where(User.email == email))
    if user is not None:
        return user
    user = User(
        id=uuid.uuid4(),
        email=email,
        password_hash=None,
        role=DEFAULT_ROLE,
        auth_provider="google",
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
```

- [ ] **Step 4: Refactor `google_oauth_service.py` to reuse the shared domain check**

In `src/backend/app/services/google_oauth_service.py`:

Change the import line:
```python
from app.core.exceptions import UnauthorizedError
```
(was `from app.core.exceptions import ForbiddenError, UnauthorizedError` — `ForbiddenError` is no longer raised directly in this file)

Add a new import:
```python
from app.services.auth_service import check_allowed_domain
```

Replace the body of `exchange_code_for_user`:
```python
def exchange_code_for_user(code: str, state: str | None) -> GoogleUser:
    _consume_state(state)
    client = _new_client()
    client.fetch_token(TOKEN_ENDPOINT, code=code)
    response = client.get(USERINFO_ENDPOINT)
    response.raise_for_status()
    payload = response.json()
    email = payload.get("email", "")
    check_allowed_domain(email)
    return GoogleUser(sub=payload.get("sub", str(uuid.uuid4())), email=email)
```

- [ ] **Step 5: Run the new tests to verify they pass**

Run: `cd src/backend && uv run pytest tests/services/test_auth_service.py -v`
Expected: 12 passed.

- [ ] **Step 6: Run the existing Google OAuth service tests to confirm the refactor didn't break them**

Run: `cd src/backend && uv run pytest tests/services/test_google_oauth_service.py -v`
Expected: 6 passed (unchanged — same exception types/messages, just relocated).

- [ ] **Step 7: Format, lint, commit**

```bash
cd src/backend && uv run ruff format app/services/auth_service.py app/services/google_oauth_service.py tests/services/test_auth_service.py
uv run ruff check app/services/auth_service.py app/services/google_oauth_service.py tests/services/test_auth_service.py
cd ../.. && git add src/backend/app/services/auth_service.py src/backend/app/services/google_oauth_service.py src/backend/tests/services/test_auth_service.py
git commit -m "feat(backend): add local auth service, share domain check with Google OAuth"
```

---

## Task 4: Config — replace `AUTH_MODE` with `ENABLE_MOCK_AUTH`

**Files:**
- Modify: `src/backend/app/core/config.py`
- Modify: `src/backend/.env.example`
- Modify: `src/backend/tests/conftest.py`

**Interfaces:**
- Produces: `settings.enable_mock_auth: bool` (default `True`). `settings.google_client_id`/`google_client_secret`/`google_redirect_uri` remain `str | None`, but are no longer validated at startup — Task 5's endpoints check them at request time instead.
- Removes: `settings.auth_mode` and the `_validate_google_mode` validator.

- [ ] **Step 1: Edit `config.py`**

In `src/backend/app/core/config.py`, replace:
```python
    # Identity & Access (LDMS-009/010/018)
    auth_mode: str = "mock"  # "mock" | "google"
    jwt_secret: str
```
with:
```python
    # Identity & Access (LDMS-009/010/018)
    enable_mock_auth: bool = True
    jwt_secret: str
```

Then delete the whole `_validate_google_mode` validator block:
```python
    @model_validator(mode="after")
    def _validate_google_mode(self) -> "Settings":
        if self.auth_mode == "google" and not (
            self.google_client_id and self.google_client_secret and self.google_redirect_uri
        ):
            raise ValueError(
                "AUTH_MODE=google requires GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, "
                "GOOGLE_REDIRECT_URI to be set."
            )
        return self
```

Since `model_validator` is now unused in this file, remove it from the import line too — change:
```python
from pydantic import model_validator
```
to nothing (delete the line; `pydantic_settings` import for `BaseSettings`/`SettingsConfigDict` stays).

- [ ] **Step 2: Update `.env.example`**

In `src/backend/.env.example`, replace:
```
AUTH_MODE=mock
```
with:
```
ENABLE_MOCK_AUTH=true
```

- [ ] **Step 3: Update `conftest.py`**

In `src/backend/tests/conftest.py`, remove this line (mock auth is now the default, no env var needed):
```python
os.environ.setdefault("AUTH_MODE", "mock")
```

- [ ] **Step 4: Verify the app still boots and existing tests still pass**

Run: `cd src/backend && uv run pytest tests/ -v`
Expected: all currently-passing tests still pass (some `test_auth.py` tests will now fail because they still reference `auth_mode` — that's expected and fixed in Task 5; if any *other* test file fails, stop and investigate before continuing).

- [ ] **Step 5: Format, lint, commit**

```bash
cd src/backend && uv run ruff format app/core/config.py tests/conftest.py
uv run ruff check app/core/config.py tests/conftest.py
cd ../.. && git add src/backend/app/core/config.py src/backend/.env.example src/backend/tests/conftest.py
git commit -m "feat(backend): replace AUTH_MODE with independent ENABLE_MOCK_AUTH flag"
```

---

## Task 5: API endpoints — register/login/logout + Google callback update + schemas

**Files:**
- Modify: `src/backend/app/schemas/auth.py`
- Modify: `src/backend/app/api/auth.py`
- Modify: `src/backend/tests/api/test_auth.py`

**Interfaces:**
- Consumes: `auth_service.register_local_user`/`authenticate_local_user`/`find_or_create_google_user` (Task 3), `settings.enable_mock_auth` (Task 4), `DbSession` from `app.api.dependencies` (existing).
- Produces: `POST /auth/register`, `POST /auth/login`, `POST /auth/logout`, updated `GET /auth/login/google` / `GET /auth/callback/google`, renamed gate on `POST /auth/dev-token`.

- [ ] **Step 1: Add request schemas**

In `src/backend/app/schemas/auth.py`, add `Field` to the pydantic import and append two new classes:

```python
from typing import Literal

from pydantic import BaseModel, Field

Role = Literal["reader", "editor", "admin"]


class DevTokenRequest(BaseModel):
    role: Role = "reader"


class DevTokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role: Role


class RegisterRequest(BaseModel):
    email: str
    password: str = Field(min_length=8, max_length=72)


class LoginRequest(BaseModel):
    email: str
    password: str
```

- [ ] **Step 2: Rewrite `app/api/auth.py`**

Replace the full contents of `src/backend/app/api/auth.py` with:

```python
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
```

- [ ] **Step 3: Rewrite `tests/api/test_auth.py`**

Replace the full contents of `src/backend/tests/api/test_auth.py` with:

```python
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


def test_google_login_returns_404_when_not_configured(api_context) -> None:
    client, _, _ = api_context
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
```

- [ ] **Step 4: Run the full backend test suite**

Run: `cd src/backend && uv run pytest -v`
Expected: all tests pass, including the 16 in `test_auth.py`, the 12 in `test_auth_service.py`, and every pre-existing test file (documents, categories, ocr, publish, editor, health, metadata, workers).

- [ ] **Step 5: Format, lint, commit**

```bash
cd src/backend && uv run ruff format app/schemas/auth.py app/api/auth.py tests/api/test_auth.py
uv run ruff check app/schemas/auth.py app/api/auth.py tests/api/test_auth.py
cd ../.. && git add src/backend/app/schemas/auth.py src/backend/app/api/auth.py src/backend/tests/api/test_auth.py
git commit -m "feat(backend): add register/login/logout endpoints, unify Google role lookup"
```

---

## Task 6: README docs update

**Files:**
- Modify: `README.md`

**Interfaces:** none (docs only).

- [ ] **Step 1: Replace the "Xác thực & Phân quyền" section**

In `README.md`, replace lines 141–188 (from `## Xác thực & Phân quyền (LDMS-009, LDMS-010, LDMS-018)` through the paragraph ending `...khi cấp qua \`/auth/dev-token\` ở chế độ mock để test kịch bản RBAC từ chối ghi).`) with:

```markdown
## Xác thực & Phân quyền (LDMS-009, LDMS-010, LDMS-018)

Hệ thống hỗ trợ song song 2 cách đăng nhập, dùng chung một bảng `users` và một
tập role (`reader` | `editor` | `admin`): đăng ký/đăng nhập bằng email+mật khẩu,
và đăng nhập Google OAuth. Tài khoản mới (dù tạo qua cách nào) đều mặc định
role `reader`; nâng quyền lên `editor`/`admin` hiện là thao tác thủ công trên
DB (`UPDATE users SET role = 'editor' WHERE email = '...'`).

`ENABLE_MOCK_AUTH` trong `.env` (mặc định `true`) bật/tắt endpoint dev-token
dùng riêng cho test RBAC nhanh, độc lập với đăng nhập thật:

```bash
curl -fsS -X POST http://localhost:8000/auth/dev-token -H 'Content-Type: application/json' \
  -d '{"role":"editor"}'
curl -fsS -X POST http://localhost:8000/auth/dev-token -H 'Content-Type: application/json' \
  -d '{"role":"reader"}'
curl -fsS -X POST http://localhost:8000/auth/dev-token -H 'Content-Type: application/json' \
  -d '{"role":"admin"}'
```

Đăng ký / đăng nhập bằng email + mật khẩu (yêu cầu email thuộc
`GOOGLE_ALLOWED_DOMAINS`, mật khẩu tối thiểu 8 ký tự):

```bash
curl -fsS -X POST http://localhost:8000/auth/register -H 'Content-Type: application/json' \
  -d '{"email":"student@hcmus.edu.vn","password":"supersecret"}'
curl -fsS -X POST http://localhost:8000/auth/login -H 'Content-Type: application/json' \
  -d '{"email":"student@hcmus.edu.vn","password":"supersecret"}'
curl -fsS -X POST http://localhost:8000/auth/logout
```

`POST /auth/logout` không giữ trạng thái phía server — trả `204`, việc "đăng
xuất" thực tế là FE xoá token khỏi `localStorage`.

Gắn token vào header `Authorization: Bearer <token>`. `POST /documents` và `POST
/documents/{id}/publish` yêu cầu role `editor` hoặc `admin`; role `reader` hoặc
không có token đều bị từ chối (`403`/`401`). RBAC hiện chỉ áp trên hai endpoint
ghi tiêu biểu theo AC (`upload`, `publish`); các endpoint ghi khác (`PUT
.../pages/{n}`, `PUT .../metadata`, `/categories`) chưa có guard — ghi nhận là
gap còn lại cho các module tương ứng bổ sung sau.

Document có field `is_public` (mặc định `false`). Guest (không token) chỉ đọc
được document `is_public = true`; ngược lại `GET /documents/{id}` và
`.../source` trả `401`. Đặt một document thành public để test thủ công:

```bash
docker compose exec postgres psql -U ldms -d ldms \
  -c "UPDATE documents SET is_public = true WHERE id = 'DOCUMENT_ID';"
```

### Google OAuth 2.0 (LDMS-018)

Đặt `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`,
`GOOGLE_REDIRECT_URI=http://localhost:8000/auth/callback/google` trong `.env`
(lấy từ [Google Cloud Console](https://console.cloud.google.com/apis/credentials)
— thêm redirect URI trên vào danh sách Authorized redirect URIs của OAuth
Client) để bật `/auth/login/google`. Không cần tắt gì khác — Google OAuth và
đăng nhập email/mật khẩu luôn chạy song song; thiếu 1 trong 3 biến trên thì
`/auth/login/google` trả `404`.

Luồng: mở `http://localhost:5173/login` → bấm "Đăng nhập với Google" → consent screen Google →
callback về BE → BE tìm hoặc tạo user theo email (role mặc định `reader` nếu
là user mới) → redirect FE tới `/auth/callback?token=...` → FE lưu token vào
`localStorage`. Email không thuộc một trong các domain liệt kê ở
`GOOGLE_ALLOWED_DOMAINS` (JSON array, mặc định `["hcmus.edu.vn"]`, có thể thêm
domain khoa/chương trình khác — vd. `["hcmus.edu.vn","clc.fitus.edu.vn"]`) bị
từ chối với `403`. Domain allowlist này áp dụng cho cả đăng ký email/mật khẩu.

Nếu một email đã đăng ký bằng mật khẩu trước đó đăng nhập lại bằng Google (hoặc
ngược lại), hệ thống dùng lại đúng identity/role cũ — không tạo user trùng.

**Bảo mật:** `GOOGLE_CLIENT_SECRET`/`JWT_SECRET` chỉ đọc từ `.env` (gitignored),
không hardcode trong repo.
```

- [ ] **Step 2: Verify no stale references remain**

Run: `grep -n "AUTH_MODE" README.md`
Expected: no output (all references removed).

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "docs: document register/login/logout alongside Google OAuth"
```

---

## Task 7: Frontend API client — `registerUser`/`loginUser`/`logoutUser`

**Files:**
- Modify: `src/frontend/src/services/api.ts`

**Interfaces:**
- Produces: `AuthResponse` type (`{ access_token: string; token_type: string; role: 'reader' | 'editor' | 'admin' }`), `registerUser(email: string, password: string): Promise<AuthResponse>`, `loginUser(email: string, password: string): Promise<AuthResponse>`, `logoutUser(): Promise<void>`. Consumed by Tasks 8–10.

- [ ] **Step 1: Add the type and functions**

In `src/frontend/src/services/api.ts`, add after the existing `type ApiErrorBody = {...}` block (before `async function request`):

```typescript
export type AuthResponse = {
  access_token: string
  token_type: string
  role: 'reader' | 'editor' | 'admin'
}
```

Add at the end of the file:

```typescript
export function registerUser(email: string, password: string): Promise<AuthResponse> {
  return request('/auth/register', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password }),
  })
}

export function loginUser(email: string, password: string): Promise<AuthResponse> {
  return request('/auth/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password }),
  })
}

export function logoutUser(): Promise<void> {
  return request('/auth/logout', { method: 'POST' })
}
```

- [ ] **Step 2: Type-check**

Run: `cd src/frontend && npx tsc -b --noEmit`
Expected: no errors.

- [ ] **Step 3: Format, lint, commit**

```bash
cd src/frontend && npm run format && npm run lint
cd ../.. && git add src/frontend/src/services/api.ts
git commit -m "feat(frontend): add register/login/logout API client functions"
```

---

## Task 8: `LoginPage` — add local email/password form

**Files:**
- Modify: `src/frontend/src/pages/LoginPage.tsx`
- Modify: `src/frontend/src/pages/LoginPage.test.tsx`
- Modify: `src/frontend/src/App.css`

**Interfaces:**
- Consumes: `loginUser` (Task 7), `useAuth()` (existing `AuthContext`), `react-router`'s `Link`/`useNavigate`.

- [ ] **Step 1: Update the failing test first**

Replace the full contents of `src/frontend/src/pages/LoginPage.test.tsx`:

```typescript
import { cleanup, fireEvent, render, screen, waitFor } from '@testing-library/react'
import { MemoryRouter } from 'react-router'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { LoginPage } from './LoginPage'
import { AuthProvider, useAuth } from '../context/AuthContext'

const fetchMock = vi.fn<typeof fetch>()

function response(body: object, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json' },
  })
}

function TokenProbe() {
  const { token } = useAuth()
  return <span data-testid="token">{token ?? 'none'}</span>
}

describe('LoginPage', () => {
  beforeEach(() => {
    vi.stubGlobal('fetch', fetchMock)
    fetchMock.mockReset()
  })

  afterEach(() => {
    cleanup()
    vi.restoreAllMocks()
    vi.unstubAllGlobals()
    window.localStorage.clear()
  })

  it('links to the backend Google login redirect', () => {
    render(
      <AuthProvider>
        <MemoryRouter>
          <LoginPage />
        </MemoryRouter>
      </AuthProvider>,
    )
    const link = screen.getByRole('link', { name: 'Đăng nhập với Google' })
    expect(link).toHaveAttribute('href', '/api/auth/login/google')
  })

  it('logs in with email and password and stores the token', async () => {
    fetchMock.mockResolvedValueOnce(
      response({ access_token: 'local-token', token_type: 'bearer', role: 'reader' }),
    )

    render(
      <AuthProvider>
        <MemoryRouter>
          <LoginPage />
          <TokenProbe />
        </MemoryRouter>
      </AuthProvider>,
    )

    fireEvent.change(screen.getByLabelText('Email'), {
      target: { value: 'student@hcmus.edu.vn' },
    })
    fireEvent.change(screen.getByLabelText('Mật khẩu'), {
      target: { value: 'supersecret' },
    })
    fireEvent.click(screen.getByRole('button', { name: 'Đăng nhập' }))

    await waitFor(() => expect(screen.getByTestId('token').textContent).toBe('local-token'))
    expect(fetchMock).toHaveBeenCalledWith(
      '/api/auth/login',
      expect.objectContaining({
        method: 'POST',
        body: JSON.stringify({ email: 'student@hcmus.edu.vn', password: 'supersecret' }),
      }),
    )
  })

  it('shows an error message when login fails', async () => {
    fetchMock.mockResolvedValueOnce(response({ detail: 'Invalid email or password.' }, 401))

    render(
      <AuthProvider>
        <MemoryRouter>
          <LoginPage />
        </MemoryRouter>
      </AuthProvider>,
    )

    fireEvent.change(screen.getByLabelText('Email'), {
      target: { value: 'student@hcmus.edu.vn' },
    })
    fireEvent.change(screen.getByLabelText('Mật khẩu'), {
      target: { value: 'wrong' },
    })
    fireEvent.click(screen.getByRole('button', { name: 'Đăng nhập' }))

    expect(await screen.findByRole('alert')).toHaveTextContent('Invalid email or password.')
  })

  it('links to the register page', () => {
    render(
      <AuthProvider>
        <MemoryRouter>
          <LoginPage />
        </MemoryRouter>
      </AuthProvider>,
    )
    expect(screen.getByRole('link', { name: 'Đăng ký' })).toHaveAttribute('href', '/register')
  })
})
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `cd src/frontend && npx vitest run src/pages/LoginPage.test.tsx`
Expected: fails — `getByLabelText('Email')` finds nothing yet (form doesn't exist).

- [ ] **Step 3: Rewrite `LoginPage.tsx`**

Replace the full contents of `src/frontend/src/pages/LoginPage.tsx`:

```typescript
import { useState } from 'react'
import type { FormEvent } from 'react'
import { Link, useNavigate } from 'react-router'
import { loginUser } from '../services/api'
import { useAuth } from '../context/AuthContext'

const API_BASE = '/api'

function GoogleIcon() {
  return (
    <svg width="18" height="18" viewBox="0 0 18 18" aria-hidden="true">
      <path
        fill="#4285F4"
        d="M17.64 9.2c0-.637-.057-1.251-.164-1.84H9v3.481h4.844a4.14 4.14 0 0 1-1.796 2.716v2.259h2.908c1.702-1.567 2.684-3.874 2.684-6.615z"
      />
      <path
        fill="#34A853"
        d="M9 18c2.43 0 4.467-.806 5.956-2.184l-2.908-2.259c-.806.54-1.837.86-3.048.86-2.344 0-4.328-1.584-5.036-3.711H.957v2.332A8.997 8.997 0 0 0 9 18z"
      />
      <path
        fill="#FBBC05"
        d="M3.964 10.706A5.41 5.41 0 0 1 3.682 9c0-.593.102-1.17.282-1.706V4.962H.957A8.996 8.996 0 0 0 0 9c0 1.452.348 2.827.957 4.038l3.007-2.332z"
      />
      <path
        fill="#EA4335"
        d="M9 3.58c1.321 0 2.508.454 3.44 1.345l2.582-2.58C13.463.891 11.426 0 9 0A8.997 8.997 0 0 0 .957 4.962L3.964 7.294C4.672 5.167 6.656 3.58 9 3.58z"
      />
    </svg>
  )
}

const HIGHLIGHTS = [
  'Tra cứu toàn văn tức thì trên toàn bộ kho tài liệu',
  'Đọc sách bảo mật trên mọi thiết bị, không giới hạn',
  'Biên tập song song ảnh scan và văn bản OCR',
]

export function LoginPage() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [error, setError] = useState('')
  const { setToken } = useAuth()
  const navigate = useNavigate()

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    setIsSubmitting(true)
    setError('')

    try {
      const { access_token: accessToken } = await loginUser(email, password)
      setToken(accessToken)
      navigate('/', { replace: true })
    } catch (loginError) {
      setError(
        loginError instanceof Error ? loginError.message : 'Không thể kết nối đến máy chủ.',
      )
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <main className="auth-shell">
      <section className="auth-hero">
        <div className="auth-hero-glow" aria-hidden="true" />
        <div className="auth-hero-content">
          <p className="eyebrow auth-hero-eyebrow">HCMUS Library</p>
          <h1 className="auth-hero-title">
            Số hóa tri thức,
            <br />
            lưu giữ trăm năm.
          </h1>
          <p className="auth-hero-copy">
            Nền tảng quản lý và số hóa tài liệu thư viện HCMUS — tra cứu, biên tập và đọc sách trực
            tuyến trong một không gian duy nhất.
          </p>
          <ul className="auth-hero-list">
            {HIGHLIGHTS.map((item) => (
              <li key={item}>
                <span aria-hidden="true">✓</span>
                {item}
              </li>
            ))}
          </ul>
        </div>
      </section>

      <section className="auth-panel">
        <div className="login-card" aria-labelledby="login-title">
          <header>
            <p className="eyebrow">Đăng nhập</p>
            <h2 id="login-title">Chào mừng trở lại</h2>
            <p className="intro">Đăng nhập bằng email hoặc tài khoản Google trường.</p>
          </header>

          <form className="local-auth-form" onSubmit={handleSubmit}>
            <label>
              Email
              <input
                type="email"
                required
                value={email}
                onChange={(event) => setEmail(event.target.value)}
              />
            </label>
            <label>
              Mật khẩu
              <input
                type="password"
                required
                value={password}
                onChange={(event) => setPassword(event.target.value)}
              />
            </label>
            <button type="submit" disabled={isSubmitting}>
              {isSubmitting ? 'Đang đăng nhập…' : 'Đăng nhập'}
            </button>
          </form>

          {error && (
            <p className="message error" role="alert">
              {error}
            </p>
          )}

          <p className="login-hint">
            Chưa có tài khoản? <Link to="/register">Đăng ký</Link>
          </p>

          <div className="auth-divider" role="separator">
            <span>hoặc</span>
          </div>

          <a className="google-button" href={`${API_BASE}/auth/login/google`}>
            <GoogleIcon />
            <span>Đăng nhập với Google</span>
          </a>

          <p className="login-hint">
            Chỉ chấp nhận email trường (vd. <code>@hcmus.edu.vn</code>,{' '}
            <code>@clc.fitus.edu.vn</code>). Tài khoản thuộc domain khác sẽ bị từ chối sau bước xác
            thực.
          </p>
        </div>
      </section>
    </main>
  )
}
```

- [ ] **Step 4: Add CSS for the form and the divider**

In `src/frontend/src/App.css`, right after the `.login-hint code { ... }` block (around line 176), add:

```css
.local-auth-form {
  display: grid;
  gap: 14px;
  margin-top: 24px;
  text-align: left;
}

.local-auth-form label {
  display: grid;
  gap: 7px;
  color: #425e55;
  font-size: 0.76rem;
  font-weight: 750;
}

.local-auth-form input {
  box-sizing: border-box;
  width: 100%;
  padding: 11px 12px;
  border: 1px solid #d5e2dd;
  border-radius: 9px;
  color: #294b40;
  background: #f8fbfa;
  font: inherit;
}

.local-auth-form button {
  justify-self: stretch;
  margin-top: 4px;
}

.auth-divider {
  display: flex;
  align-items: center;
  gap: 12px;
  margin: 24px 0 0;
  color: #a2b2ac;
  font-size: 0.72rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.auth-divider::before,
.auth-divider::after {
  content: '';
  flex: 1;
  height: 1px;
  background: #dbe5e1;
}
```

Then find the existing `.google-button` rule (around line 130) and change `margin-top: 34px;` to `margin-top: 18px;` (the divider above it now supplies the top spacing).

- [ ] **Step 5: Run the tests to verify they pass**

Run: `cd src/frontend && npx vitest run src/pages/LoginPage.test.tsx`
Expected: 4 passed.

- [ ] **Step 6: Format, lint, commit**

```bash
cd src/frontend && npm run format && npm run lint
cd ../.. && git add src/frontend/src/pages/LoginPage.tsx src/frontend/src/pages/LoginPage.test.tsx src/frontend/src/App.css
git commit -m "feat(frontend): add email/password login form alongside Google button"
```

---

## Task 9: `RegisterPage` (new)

**Files:**
- Create: `src/frontend/src/pages/RegisterPage.tsx`
- Create: `src/frontend/src/pages/RegisterPage.test.tsx`
- Modify: `src/frontend/src/App.tsx`

**Interfaces:**
- Consumes: `registerUser` (Task 7), `useAuth()`, `react-router`'s `Link`/`useNavigate`.
- Produces: route `/register`.

- [ ] **Step 1: Write the failing test**

Create `src/frontend/src/pages/RegisterPage.test.tsx`:

```typescript
import { cleanup, fireEvent, render, screen, waitFor } from '@testing-library/react'
import { MemoryRouter } from 'react-router'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { RegisterPage } from './RegisterPage'
import { AuthProvider, useAuth } from '../context/AuthContext'

const fetchMock = vi.fn<typeof fetch>()

function response(body: object, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json' },
  })
}

function TokenProbe() {
  const { token } = useAuth()
  return <span data-testid="token">{token ?? 'none'}</span>
}

describe('RegisterPage', () => {
  beforeEach(() => {
    vi.stubGlobal('fetch', fetchMock)
    fetchMock.mockReset()
  })

  afterEach(() => {
    cleanup()
    vi.restoreAllMocks()
    vi.unstubAllGlobals()
    window.localStorage.clear()
  })

  it('registers with matching passwords and stores the token', async () => {
    fetchMock.mockResolvedValueOnce(
      response({ access_token: 'new-token', token_type: 'bearer', role: 'reader' }, 201),
    )

    render(
      <AuthProvider>
        <MemoryRouter>
          <RegisterPage />
          <TokenProbe />
        </MemoryRouter>
      </AuthProvider>,
    )

    fireEvent.change(screen.getByLabelText('Email'), {
      target: { value: 'student@hcmus.edu.vn' },
    })
    fireEvent.change(screen.getByLabelText('Mật khẩu'), {
      target: { value: 'supersecret' },
    })
    fireEvent.change(screen.getByLabelText('Xác nhận mật khẩu'), {
      target: { value: 'supersecret' },
    })
    fireEvent.click(screen.getByRole('button', { name: 'Đăng ký' }))

    await waitFor(() => expect(screen.getByTestId('token').textContent).toBe('new-token'))
    expect(fetchMock).toHaveBeenCalledWith(
      '/api/auth/register',
      expect.objectContaining({
        method: 'POST',
        body: JSON.stringify({ email: 'student@hcmus.edu.vn', password: 'supersecret' }),
      }),
    )
  })

  it('shows an error and does not call the API when passwords do not match', () => {
    render(
      <AuthProvider>
        <MemoryRouter>
          <RegisterPage />
        </MemoryRouter>
      </AuthProvider>,
    )

    fireEvent.change(screen.getByLabelText('Email'), {
      target: { value: 'student@hcmus.edu.vn' },
    })
    fireEvent.change(screen.getByLabelText('Mật khẩu'), {
      target: { value: 'supersecret' },
    })
    fireEvent.change(screen.getByLabelText('Xác nhận mật khẩu'), {
      target: { value: 'different' },
    })
    fireEvent.click(screen.getByRole('button', { name: 'Đăng ký' }))

    expect(screen.getByRole('alert')).toHaveTextContent('Mật khẩu xác nhận không khớp.')
    expect(fetchMock).not.toHaveBeenCalled()
  })

  it('shows the server error when registration fails', async () => {
    fetchMock.mockResolvedValueOnce(
      response({ detail: 'An account with this email already exists.' }, 409),
    )

    render(
      <AuthProvider>
        <MemoryRouter>
          <RegisterPage />
        </MemoryRouter>
      </AuthProvider>,
    )

    fireEvent.change(screen.getByLabelText('Email'), {
      target: { value: 'student@hcmus.edu.vn' },
    })
    fireEvent.change(screen.getByLabelText('Mật khẩu'), {
      target: { value: 'supersecret' },
    })
    fireEvent.change(screen.getByLabelText('Xác nhận mật khẩu'), {
      target: { value: 'supersecret' },
    })
    fireEvent.click(screen.getByRole('button', { name: 'Đăng ký' }))

    expect(await screen.findByRole('alert')).toHaveTextContent(
      'An account with this email already exists.',
    )
  })

  it('links back to the login page', () => {
    render(
      <AuthProvider>
        <MemoryRouter>
          <RegisterPage />
        </MemoryRouter>
      </AuthProvider>,
    )
    expect(screen.getByRole('link', { name: 'Đăng nhập' })).toHaveAttribute('href', '/login')
  })
})
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `cd src/frontend && npx vitest run src/pages/RegisterPage.test.tsx`
Expected: fails — `Failed to resolve import "./RegisterPage"`.

- [ ] **Step 3: Write `RegisterPage.tsx`**

Create `src/frontend/src/pages/RegisterPage.tsx`:

```typescript
import { useState } from 'react'
import type { FormEvent } from 'react'
import { Link, useNavigate } from 'react-router'
import { registerUser } from '../services/api'
import { useAuth } from '../context/AuthContext'

export function RegisterPage() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [confirmPassword, setConfirmPassword] = useState('')
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [error, setError] = useState('')
  const { setToken } = useAuth()
  const navigate = useNavigate()

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    if (password !== confirmPassword) {
      setError('Mật khẩu xác nhận không khớp.')
      return
    }

    setIsSubmitting(true)
    setError('')

    try {
      const { access_token: accessToken } = await registerUser(email, password)
      setToken(accessToken)
      navigate('/', { replace: true })
    } catch (registerError) {
      setError(
        registerError instanceof Error ? registerError.message : 'Không thể kết nối đến máy chủ.',
      )
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <main className="auth-shell">
      <section className="auth-hero">
        <div className="auth-hero-glow" aria-hidden="true" />
        <div className="auth-hero-content">
          <p className="eyebrow auth-hero-eyebrow">HCMUS Library</p>
          <h1 className="auth-hero-title">
            Tạo tài khoản,
            <br />
            bắt đầu số hóa.
          </h1>
          <p className="auth-hero-copy">
            Đăng ký bằng email trường để tải lên, biên tập và đọc tài liệu số hóa của thư viện
            HCMUS.
          </p>
        </div>
      </section>

      <section className="auth-panel">
        <div className="login-card" aria-labelledby="register-title">
          <header>
            <p className="eyebrow">Đăng ký</p>
            <h2 id="register-title">Tạo tài khoản mới</h2>
            <p className="intro">Chỉ chấp nhận email trường (vd. @hcmus.edu.vn).</p>
          </header>

          <form className="local-auth-form" onSubmit={handleSubmit}>
            <label>
              Email
              <input
                type="email"
                required
                value={email}
                onChange={(event) => setEmail(event.target.value)}
              />
            </label>
            <label>
              Mật khẩu
              <input
                type="password"
                required
                minLength={8}
                value={password}
                onChange={(event) => setPassword(event.target.value)}
              />
            </label>
            <label>
              Xác nhận mật khẩu
              <input
                type="password"
                required
                minLength={8}
                value={confirmPassword}
                onChange={(event) => setConfirmPassword(event.target.value)}
              />
            </label>
            <button type="submit" disabled={isSubmitting}>
              {isSubmitting ? 'Đang đăng ký…' : 'Đăng ký'}
            </button>
          </form>

          {error && (
            <p className="message error" role="alert">
              {error}
            </p>
          )}

          <p className="login-hint">
            Đã có tài khoản? <Link to="/login">Đăng nhập</Link>
          </p>
        </div>
      </section>
    </main>
  )
}
```

- [ ] **Step 4: Wire the route into `App.tsx`**

In `src/frontend/src/App.tsx`, add the import:
```typescript
import { RegisterPage } from './pages/RegisterPage'
```
(place it right after `import { LoginPage } from './pages/LoginPage'`)

Add the route inside `<Routes>`, right after `<Route path="/login" element={<LoginPage />} />`:
```typescript
        <Route path="/register" element={<RegisterPage />} />
```

- [ ] **Step 5: Run the tests to verify they pass**

Run: `cd src/frontend && npx vitest run src/pages/RegisterPage.test.tsx`
Expected: 4 passed.

- [ ] **Step 6: Run the full frontend test suite**

Run: `cd src/frontend && npm run test`
Expected: all test files pass, including `LoginPage.test.tsx`, `RegisterPage.test.tsx`, and every pre-existing page/component test.

- [ ] **Step 7: Format, lint, commit**

```bash
cd src/frontend && npm run format && npm run lint
cd ../.. && git add src/frontend/src/pages/RegisterPage.tsx src/frontend/src/pages/RegisterPage.test.tsx src/frontend/src/App.tsx
git commit -m "feat(frontend): add register page and route"
```

---

## Task 10: Logout calls `POST /auth/logout` before clearing the token

**Files:**
- Modify: `src/frontend/src/App.tsx`

**Interfaces:**
- Consumes: `logoutUser` (Task 7), existing `clearToken()` from `useAuth()`.

- [ ] **Step 1: Update `AuthNavItem` in `App.tsx`**

Add the import:
```typescript
import { logoutUser } from './services/api'
```

Replace the `AuthNavItem` function body:
```typescript
function AuthNavItem() {
  const { token, clearToken } = useAuth()
  const navigate = useNavigate()

  if (!token) {
    return <NavLink to="/login">Đăng nhập</NavLink>
  }

  return (
    <button
      type="button"
      className="nav-logout"
      onClick={() => {
        void logoutUser().finally(() => {
          clearToken()
          navigate('/login')
        })
      }}
    >
      Đăng xuất
    </button>
  )
}
```

(`.finally()` guarantees the client still discards the token and navigates away even if the `POST /auth/logout` network call fails — logout must never get the user stuck.)

- [ ] **Step 2: Manually verify in the browser**

Run: `cd src/frontend && npm run dev` (with the backend running via `docker compose up` / `uv run uvicorn app.main:app --reload` from `src/backend`)

1. Open `http://localhost:5173/register`, register a new `@hcmus.edu.vn` account → should redirect to `/` and show "Đăng xuất" in the nav.
2. Click "Đăng xuất" → should redirect to `/login`, nav should show "Đăng nhập" again.
3. Open `http://localhost:5173/login`, log back in with the same email/password → should redirect to `/` again.
4. If `GOOGLE_CLIENT_ID`/`SECRET`/`REDIRECT_URI` are set in `src/backend/.env`, click "Đăng nhập với Google" → should redirect to Google's consent screen.

Expected: all four flows work without console errors.

- [ ] **Step 3: Run the full frontend test suite one more time**

Run: `cd src/frontend && npm run test`
Expected: all tests still pass (App.tsx has no dedicated test file, so this step is a regression check on the pages that render it indirectly).

- [ ] **Step 4: Format, lint, commit**

```bash
cd src/frontend && npm run format && npm run lint
cd ../.. && git add src/frontend/src/App.tsx
git commit -m "feat(frontend): call POST /auth/logout before clearing the local token"
```

---

## Final verification (run once all 10 tasks are complete)

- [ ] Backend: `cd src/backend && uv run ruff format . && uv run ruff check . && uv run pytest -v`
- [ ] Frontend: `cd src/frontend && npm run format && npm run lint && npm run test`
- [ ] `grep -rn "AUTH_MODE" src/backend README.md` returns nothing.
- [ ] `git log --oneline -12` shows one commit per task, in order.
