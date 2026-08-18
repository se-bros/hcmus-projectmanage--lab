# JWT Local Authentication (Register/Login/Logout) alongside Google OAuth

**Task:** 23127152 — Tuấn Anh, per `docs/plan.md` §4 (LDMS-009 lineage) and
`docs/07-product-backlog.md` LDMS-009/LDMS-018.

## Problem

The current auth system has no persisted users. `POST /auth/dev-token`
(LDMS-009) mints a JWT for a random UUID subject purely for dev/testing.
Google OAuth (LDMS-018) issues a JWT with a hardcoded `role="editor"` and
never touches the database. The two are mutually exclusive via
`AUTH_MODE=mock|google` — enabling one 404s the other.

This project needs real, persisted-account JWT authentication
(register / login / logout) that runs **at the same time** as Google OAuth,
with roles that behave the same way regardless of which method a user
signs in with.

## Decisions

1. **Shared identity.** One `users` table backs both local (email/password)
   and Google-authenticated accounts. If a Google login's email matches an
   existing user (however that account was created), it reuses that row —
   one person, one role, one identity, regardless of login method.
2. **No more mutual exclusion.** `AUTH_MODE` is removed. Local JWT
   (register/login/logout) and Google OAuth are both always routable. The
   mock dev-token endpoint becomes independently flag-gated via
   `ENABLE_MOCK_AUTH` (default `true`), unrelated to Google's availability.
3. **Logout is client-side.** JWTs stay stateless — no revocation list.
   `POST /auth/logout` exists for symmetry/audit and returns `204`; the
   frontend deletes the token from `localStorage`. A stolen token remains
   valid until `exp`, same as today.
4. **Local registration respects the same domain allowlist as Google**
   (`GOOGLE_ALLOWED_DOMAINS`, e.g. `hcmus.edu.vn`) — only school members
   get accounts, regardless of path.
5. **Both paths default new accounts to role `reader`.** This changes
   existing Google-login behavior (previously hardcoded `editor`) to match
   the LDMS-018 backlog AC and to be consistent with local registration.
   Existing Google users get `reader` on next login unless promoted.

## Data model

New table `users`:

| column | type | notes |
|---|---|---|
| `id` | UUID pk | |
| `email` | string, unique, indexed | |
| `password_hash` | string, nullable | null for Google-only accounts |
| `role` | string | `reader` \| `editor` \| `admin`, default `reader` |
| `auth_provider` | string | `local` \| `google` — how the account was first created |
| `created_at` | timestamptz | server default now() |

New Alembic migration `20260721_0006_users.py`, `down_revision =
"20260716_0005"`, following the existing migration file style
(`op.create_table` / `op.drop_table`).

`UserRepository` (`app/repositories/user_repository.py`): `create`,
`get_by_email` — same shape as `DocumentRepository`.

## Password hashing

Add `bcrypt` as a new backend dependency. `hash_password()` /
`verify_password()` added to `app/core/security.py`, next to the existing
`create_access_token`/`_decode` helpers. No `passlib`, no
`pydantic.EmailStr`/`email-validator` — email format/domain validation
reuses the same manual `str.endswith("@domain")` check
`google_oauth_service.py` already does, to avoid adding a second dependency
for one field.

Password rule: minimum 8 characters, enforced in the request schema.

## Service layer — `app/services/auth_service.py`

- `register_local_user(db, email, password) -> User`: domain check → reject
  if email already exists → hash password → create with `role="reader"`,
  `auth_provider="local"`.
- `authenticate_local_user(db, email, password) -> User`: look up by email;
  if missing, `password_hash is None` (Google-only account), or hash
  mismatch → `UnauthorizedError` (same generic message in all three cases,
  no user-enumeration signal).
- `find_or_create_google_user(db, email) -> User`: look up by email; if
  found, return as-is (role untouched, even if provider differs); if not
  found, create with `auth_provider="google"`, `password_hash=None`,
  `role="reader"`.

## API — `app/api/auth.py`

| Endpoint | Change |
|---|---|
| `POST /auth/register` | **New.** Body `{email, password}` → creates user, auto-issues JWT, returns `{access_token, token_type, role}` (reuses existing `DevTokenResponse` shape) |
| `POST /auth/login` | **New.** Body `{email, password}` → verifies, returns JWT |
| `POST /auth/logout` | **New.** No body, no auth required, returns `204` |
| `GET /auth/login/google` | Behavior same; no longer gated by `auth_mode`, gated by whether Google credentials are configured |
| `GET /auth/callback/google` | Now calls `find_or_create_google_user`; JWT role comes from the DB row, not a hardcoded literal |
| `POST /auth/dev-token` | Unchanged logic; gate switches from `auth_mode != "mock"` to `not settings.enable_mock_auth` |

## Config — `app/core/config.py`

- Remove `auth_mode: str` and the `_validate_google_mode` startup
  validator.
- Add `enable_mock_auth: bool = True`.
- Google credentials (`google_client_id`/`secret`/`redirect_uri`) become
  fully optional at startup; `GET /auth/login/google` raises
  `NotFoundError("Google OAuth is not configured.")` at request time if
  they're unset, instead of failing app boot.

## Frontend

- `RegisterPage.tsx` (new) — email/password/confirm-password form, calls
  `POST /api/auth/register`, auto-logs in (`setToken`) on success, route
  `/register`.
- `LoginPage.tsx` — add an email/password form above the existing Google
  button, plus a link to `/register`.
- `App.tsx`'s `AuthNavItem` — before `clearToken()`, fire-and-forget
  `POST /api/auth/logout`.
- `AuthContext.tsx` — unchanged.

## Tests

Rewrite `tests/api/test_auth.py`:
- Replace `auth_mode` monkeypatches with direct
  `google_client_id`/`enable_mock_auth` monkeypatches.
- New: register success, duplicate email, disallowed domain, weak password.
- New: login success, wrong password, unknown email, Google-only account
  rejected on local login.
- New: logout returns `204`.
- Update: Google callback test now asserts role `reader` (was `editor`),
  and a second test asserts an existing local user's role is preserved
  when they subsequently log in via Google.

## Docs

Update README "Xác thực & Phân quyền" section: replace `AUTH_MODE`
mock/google explanation with `ENABLE_MOCK_AUTH`, add `curl` examples for
`/auth/register` and `/auth/login`, and correct the note that currently
says Google logins get `editor` by default.

## Out of scope

- No refresh tokens, no server-side token revocation/blacklist.
- No admin-facing role-promotion endpoint — promoting a user to
  `editor`/`admin` remains a manual DB operation, same as today's Google
  flow.
- No password reset / email verification flow.
