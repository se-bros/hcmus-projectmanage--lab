---
description: "Cross-check spec, plan, and tasks for consistency, coverage gaps, and constitution violations before implementing"
---

# Analyze Consistency

## User Input

```text
$ARGUMENTS
```

Consider the user input if provided (e.g. focus areas). This command is read-only analysis — it does not modify files.

## Execution

1. Run `bash .specify/scripts/bash/check-prerequisites.sh --json --require-tasks --include-tasks`. This fails if `plan.md` or `tasks.md` are missing (run `/speckit.plan` / `/speckit.tasks` first).
2. Read `spec.md`, `plan.md`, `tasks.md`, and `.specify/memory/constitution.md`.
3. Cross-check and report findings in these categories, most severe first:
   - **Coverage gaps**: user stories or functional requirements (`FR-00X`) with no corresponding task.
   - **Orphan tasks**: tasks that don't trace to any requirement or user story.
   - **Constitution violations**: anything in `plan.md`/`tasks.md` that conflicts with a non-negotiable principle (Principle IV, file security, applies even during MVP) without a justification in Complexity Tracking.
   - **Inconsistencies**: terminology/entity name mismatches between spec and plan/data-model, or a plan decision that contradicts a spec requirement.
   - **Ambiguities**: any remaining `[NEEDS CLARIFICATION]` markers that should have been resolved by `/speckit.clarify`.
4. Do not silently fix anything — report findings, then ask the user which to address (or address only what they explicitly approve).
