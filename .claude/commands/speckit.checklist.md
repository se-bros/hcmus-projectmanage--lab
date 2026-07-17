---
description: "Generate a custom review checklist (e.g. security, UX, requirements-quality) for the current feature"
---

# Generate Checklist

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input — it specifies what kind of checklist is wanted (e.g. "security checklist for the upload flow", "requirements-quality checklist"). Ask if it's missing/ambiguous rather than guessing the checklist type.

## Execution

1. Resolve paths: `bash .specify/scripts/bash/check-prerequisites.sh --json --paths-only`. Read whatever of `spec.md` / `plan.md` / `tasks.md` exist for context.
2. Determine the checklist type and category from `$ARGUMENTS`. Common types for this project: requirements-quality, security (file-access/RBAC per Constitution Principle IV), API-contract review, UX/accessibility.
3. Copy `.specify/templates/checklist-template.md` to `FEATURE_DIR/checklists/<type>.md` (create the `checklists/` dir if needed) and replace ALL sample `CHK00X` items — they are illustration only.
4. Write real, checkable items grounded in the actual spec/plan/requirements — not generic boilerplate. Each item should be something a reviewer can verify true/false against this specific feature (e.g. "CHK004 Every endpoint under `/api/documents/*` checks RBAC before generating a MinIO signed URL" rather than "Add security checks").
5. Group items under meaningful categories (not the template's placeholder `[Category 1]`/`[Category 2]`).
6. Report: checklist file path and item count per category.
