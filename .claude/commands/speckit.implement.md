---
description: "Execute tasks.md for the current feature, phase by phase, respecting dependencies"
---

# Implement Tasks

## User Input

```text
$ARGUMENTS
```

Consider the user input if provided (e.g. "only Phase 3" / "just User Story 1").

## Execution

1. Run `bash .specify/scripts/bash/check-prerequisites.sh --json --require-tasks --include-tasks`. Read `tasks.md` plus `plan.md`, `data-model.md`, `contracts/` as available.
2. Work through tasks in dependency order: Setup → Foundational → user stories in priority order (P1 first) → Polish, unless `$ARGUMENTS` restricts scope.
3. Within a phase, tasks marked `[P]` touch different files with no ordering dependency — batch them; unmarked tasks are sequential.
4. After finishing each user story's phase, stop and report a checkpoint: what was implemented, and how to verify that story independently (per its "Independent Test" in `tasks.md`). Don't silently continue past a checkpoint into the next story if the user only asked for the MVP.
5. Mark tasks off in `tasks.md` (`[ ]` → `[x]`) as you complete them, so `/speckit.analyze` and future `/speckit.implement` runs see accurate state.
6. Follow this project's standing rules while implementing: `AGENTS.md`/`CLAUDE.md` Definition of Done (frontend `npm run format && npm run lint` in `src/frontend`; backend `uv run ruff format . && uv run ruff check .` in `src/backend`, `uv run pytest` when tests are in scope), and `.specify/memory/constitution.md` (Principle IV file-security is non-negotiable even mid-task).
7. If a task turns out to be ambiguous or blocked (e.g. missing dependency, conflicting with constitution), stop and ask rather than guessing — don't mark it complete.
