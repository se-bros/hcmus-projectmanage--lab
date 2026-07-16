---
description: "Generate a dependency-ordered, per-user-story tasks.md from the current feature's plan and spec"
---

# Generate Tasks

## User Input

```text
$ARGUMENTS
```

Consider the user input if provided (e.g. "include tests" — tasks are test-optional by default).

## Execution

1. Run `bash .specify/scripts/bash/check-prerequisites.sh --json`. This requires `plan.md` to already exist (fails with a clear message telling the user to run `/speckit.plan` first if not). Parse `FEATURE_DIR` and `AVAILABLE_DOCS`.
2. Read `plan.md`, `spec.md`, and whichever of `research.md` / `data-model.md` / `contracts/` / `quickstart.md` are listed in `AVAILABLE_DOCS`.
3. Copy `.specify/templates/tasks-template.md` to `FEATURE_DIR/tasks.md` and replace ALL sample content — the template's sample tasks (T001-T028+) are illustration only and must not survive into the generated file.
4. Build the real task list:
   - **Phase 1 Setup** / **Phase 2 Foundational**: only include what this feature actually needs (skip DB/auth/routing scaffolding tasks if those already exist in the codebase — check before assuming greenfield).
   - **One phase per user story**, ordered by priority (P1 first), each with its own Goal, Independent Test, and implementation tasks with exact file paths (`src/backend/app/...`, `src/frontend/src/...`).
   - Only add test tasks if the spec or `$ARGUMENTS` explicitly asked for tests — this project's constitution defers test/lint gates until a story's AC is officially picked (not during scaffolding).
   - Mark `[P]` only for tasks touching different files with no ordering dependency.
   - Add a final **Polish** phase only if there's real cross-cutting work (not boilerplate filler).
5. Fill in **Dependencies & Execution Order** and a short **Implementation Strategy** (MVP-first: Setup → Foundational → P1 → validate) reflecting the actual phases you wrote, not the template's generic text.
6. Report: task count per phase/story, and which phase constitutes the MVP checkpoint.
