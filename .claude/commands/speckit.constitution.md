---
description: "Create or update the project constitution from interactive or provided principle inputs"
---

# Update Constitution

Create, update, or amend the project constitution at `.specify/memory/constitution.md`.

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Execution

1. Read the existing `.specify/memory/constitution.md`. If it only contains placeholder tokens like `[PROJECT_NAME]`, treat this as a first-time creation; otherwise treat this as an amendment.
2. Identify all placeholder tokens (`[ALL_CAPS_IDENTIFIER]`) if starting from `.specify/templates/constitution-template.md`, or identify the sections the user's `$ARGUMENTS` asks to change if amending.
3. Draft the new/updated content:
   - Derive concrete principles from user input, `AGENTS.md`/`CLAUDE.md`, and `docs/06-architecture.md` if present — do not invent constraints not implied by the project.
   - Each principle needs a short name, a description, and a rationale.
   - Keep a `Governance` section describing how amendments happen and what supersedes what.
4. Bump the version at the bottom following semver:
   - **MAJOR**: backward-incompatible principle removals/redefinitions
   - **MINOR**: new principle or materially expanded section
   - **PATCH**: wording/clarification only
   Set `Last Amended` to today's date; keep `Ratified` as the original date unless this is the first ratification.
5. Write the result to `.specify/memory/constitution.md`, replacing all placeholder tokens — no bracketed placeholders may remain.
6. After writing, list every other file that references constitution principles (e.g. `.specify/templates/plan-template.md`'s Constitution Check gate, `README.md`) and flag any that are now inconsistent with the new wording, without editing them unless asked.
7. Output a short summary: version bump (old → new), principles added/removed/reworded, and any follow-up files flagged in step 6.

## Note

This project's constitution already exists and is filled in (`.specify/memory/constitution.md`, currently v1.1.0). Prefer **amending** it over regenerating from scratch — read it first and preserve the MVP-phase framing already established there unless the user asks to remove it.
