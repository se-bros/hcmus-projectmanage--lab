---
description: "Generate the implementation plan (and Phase 0/1 design docs) for the current feature spec"
---

# Create Implementation Plan

## User Input

```text
$ARGUMENTS
```

Consider the user input if provided (e.g. tech constraints not already in the spec or `CLAUDE.md`).

## Execution

1. Run `bash .specify/scripts/bash/setup-plan.sh --json` from repo root. Parse `FEATURE_SPEC`, `IMPL_PLAN`, `SPECS_DIR`, `BRANCH`. The script copies `.specify/templates/plan-template.md` to `IMPL_PLAN` if not already present, and fails if the current branch isn't a recognized feature branch (`check_feature_branch` in `.specify/scripts/bash/common.sh`).
2. Read `FEATURE_SPEC` fully, plus `CLAUDE.md` and `.specify/memory/constitution.md` for stack/architecture constraints — do not re-derive stack choices already fixed there (React+TS/Vite frontend, FastAPI/Python 3.11/`uv` backend, PostgreSQL, MinIO; see `docs/06-architecture.md`).
3. Fill in `IMPL_PLAN`'s **Technical Context** section concretely (no `NEEDS CLARIFICATION` left if it's answerable from the constitution/architecture docs).
4. **Constitution Check** (gate before Phase 0, re-checked after Phase 1): walk each principle in `.specify/memory/constitution.md` and state pass/fail against this feature. Remember this project is mid-MVP-sprint — Principles I-III (layering, contracts, test/lint gates) are relaxed for scaffolding work, but Principle IV (file security — signed MinIO URLs, RBAC before access) is non-negotiable regardless of MVP status. Any violation must be justified in **Complexity Tracking** or the plan must be revised to avoid it.
5. **Phase 0 — research.md**: For anything left ambiguous in Technical Context, research and record a Decision / Rationale / Alternatives-considered entry. Do not carry forward `NEEDS CLARIFICATION` into Phase 1.
6. **Phase 1 — design docs** (only for entities/endpoints actually in scope for this feature):
   - `data-model.md`: entities, fields, relationships, validation rules derived from the spec's Key Entities/Functional Requirements.
   - `contracts/`: one file per API surface touched (endpoint + request/response schema), matching the FastAPI/Pydantic conventions already used in `src/backend`.
   - `quickstart.md`: minimal steps to run/verify this feature locally.
7. Fill **Project Structure** in `IMPL_PLAN` with the real paths this feature touches under `src/frontend` / `src/backend` (delete the unused Option 1/2/3 template scaffolding — the delivered plan must not contain option labels).
8. Do not create `tasks.md` — that's `/speckit.tasks`.
9. Report: plan file path, Constitution Check result (pass, or violations + justification), and which of research/data-model/contracts/quickstart were generated.
