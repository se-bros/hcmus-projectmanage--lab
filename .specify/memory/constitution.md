# HCMUS-LDMS Constitution

## MVP Phase Note

The team is currently in the MVP sprint (see `docs/plan.md`): trimmed
acceptance criteria, scaffolding on fixture/mock data, one person coding
both frontend and backend for a single story. This is accepted behavior,
not a violation of the principles below. The priority is getting an
**end-to-end flow working** first; full AC coverage, tests, and clean
layering come after. The principles below are a long-term direction, not a
checklist that blocks every commit during the MVP phase.

## Core Principles

### I. Layering (a direction, not rigid during MVP)

Backend aims for 3 layers: `api/` (router) → `services/` (business logic) →
`repositories/` + `models/` (SQLAlchemy). Frontend aims for `components/`,
`pages/`, `services/` (API calls), `context/` (state) — technical layering,
not feature-based.
During scaffolding/MVP work, one person may code both layers or temporarily
fold service logic into the router — that's acceptable. Once a story is
officially picked (full AC), it should be split back into this layering
before merging into `develop`.
Rationale: The team is 4 part-time engineers; layering keeps code easy to
navigate long-term, but isn't worth blocking progress during the first
2-day sprint.

### II. Clear Contracts Once a Story Is Officially Picked

Once an endpoint is considered "done" for an officially picked story (full
AC), it should have a Pydantic schema in `schemas/` and use the `AppError`
hierarchy (`core/exceptions.py`) instead of ad hoc `JSONResponse`.
Scaffolding endpoints/placeholders (reading from fixtures, no official AC
yet) are exempt — but should be cleaned up before the story is picked for
real.
Rationale: Keeps frontend/backend in sync without adding paperwork overhead
to scaffolding work.

### III. Test & Lint — Required Before Merging into `develop`, Not During Scaffolding

Before merging `feature/*` → `develop` for a story with completed picked
AC, run: `uv run ruff format .`, `uv run ruff check .`, `uv run pytest`
(backend) and `npm run format`, `npm run lint` (frontend).
While scaffolding with fixture data (not yet wired to the real API), this
is not required — speed takes priority.
Rationale: Automated gates matter for code that will live long-term, but
shouldn't be forced onto scaffold code that will be replaced within days.

**CI enforcement note:** `.github/workflows/ci.yml` runs on every PR
targeting `main`/`develop` (backend: `ruff format --check`, `ruff check`,
`pytest`; frontend: `npm run lint`, `npm run build`, `npm test`). CI does
not distinguish scaffolding from officially-picked stories — it gates the
PR either way. So in practice, once scaffolding work is opened as a PR
into `develop` (not just pushed to a feature branch), it must already be
lint-clean and must not break existing tests, even if full AC/DoD isn't
done yet. The "not required" exemption applies to in-progress feature
branches before a PR is opened, not to the PR/merge step itself.

### IV. File Security Is Non-Negotiable Even During MVP

Original scanned files and EPUB files must never be exposed via
public/direct URLs. Access must go through a MinIO Signed URL (max 15
minutes), only after RBAC has been checked. This principle must NOT be
trimmed even in the reduced-AC MVP, since it is the system's core value
proposition (preventing piracy of copyrighted library material).
Rationale: `docs/06-architecture.md` §2.1, §5.1 — this is the reason the
architecture exists, not a technical detail that can be deferred.

### V. Heavy Work Runs in the Background, Never Blocks the Request

OCR (Tesseract) and EPUB compilation (Pandoc) run via FastAPI
`BackgroundTasks`, never synchronously on the request thread — even in the
trimmed-AC version. The API returns a status immediately; the frontend
polls. Celery/Redis/Elasticsearch are not needed unless the actual roadmap
thresholds are hit (`docs/06-architecture.md` §4.1).
Rationale: Avoids blocking the main thread; simpler than Celery, so it
costs no more effort than doing it synchronously.

## Technology Constraints

- Frontend: React 18+ & TypeScript, Vite, Epub.js, axios, Zustand/Context.
- Backend: FastAPI (Python 3.11, managed with `uv`), SQLAlchemy, Alembic,
  Pydantic.
- Data: PostgreSQL 16 (metadata + RBAC + FTS via `tsvector`/GIN).
- Storage: MinIO (S3-compatible), on-premise.
- Auth: Google OAuth 2.0 (`authlib`) or Mock Auth for local dev.
- Deployment: Docker & Docker Compose.
- Do not silently add Elasticsearch/Celery+Redis/Keycloak — these are
  roadmap items, only added when there's real need, with
  `docs/06-architecture.md` updated accordingly.

## Development Workflow

- Git follows GitFlow: `feature/*` → `develop` → `release/*` → `main`,
  `hotfix/*` from `main` for emergencies. Merging into `main` requires PR
  approval from the Tech Lead.
- When adding real files to `models/`, `repositories/`, `schemas/`,
  `services/` — one file per entity (e.g. `models/document.py`), avoid
  dumping into a shared file. Does not apply to temporary scaffold/fixture
  code.
- Migrations: `uv run alembic revision --autogenerate -m "..."` then
  `uv run alembic upgrade head`; new models must be imported into
  `app/db/migrations/env.py`.

## Governance

This constitution is a directional framework, prioritizing MVP sprint
speed over procedure. Principle IV (file security) is non-negotiable; the
other principles can be temporarily relaxed while scaffolding, but must be
cleaned up before the corresponding story is considered "Done". Amendments
must state a reason and update `docs/06-architecture.md` if they affect the
tech stack.

Versioning: MAJOR (backward-incompatible principle changes/removals) ·
MINOR (new principle/section) · PATCH (wording clarifications).

**Version**: 1.2.0 | **Ratified**: 2026-07-16 | **Last Amended**: 2026-07-17
