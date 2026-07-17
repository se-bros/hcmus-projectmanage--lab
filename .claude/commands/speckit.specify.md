---
description: "Create or update the feature specification from a natural language feature description"
---

# Create Feature Specification

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (empty is not valid — ask the user for a feature description if missing).

## Execution

1. Generate a concise short name (2-4 words, action-noun style, e.g. "add-user-auth") from the feature description.
2. Create the feature branch and spec scaffold by running (this repo has no `.specify/scripts/powershell`, so always use bash — on Windows that's WSL's `bash.exe`, already on PATH):

   ```bash
   bash .specify/scripts/bash/create-new-feature.sh --json --short-name "<short-name>" "<feature description>"
   ```

   Parse the JSON output for `BRANCH_NAME`, `SPEC_FILE`, `FEATURE_NUM`. Run this only once per feature — if it fails because the branch already exists, ask the user before retrying with `--allow-existing-branch`.
3. Load `SPEC_FILE` (already seeded from `.specify/templates/spec-template.md` by the script) and fill it in:
   - Replace `[FEATURE NAME]`, `[###-feature-name]`, `[DATE]` (today's date).
   - Write 1-3 prioritized user stories (P1/P2/P3+), each independently testable — a P1-only implementation must still be a viable MVP.
   - Fill **Edge Cases**, **Functional Requirements** (`FR-00X`), **Key Entities** (if data is involved), and **Success Criteria** (`SC-00X`, measurable, technology-agnostic).
   - Fill **Assumptions** for anything the description left ambiguous instead of guessing silently — but flag genuinely blocking ambiguities as `[NEEDS CLARIFICATION: ...]` rather than assuming.
4. Do not include implementation details (languages, frameworks, APIs) in the spec — that belongs in `/speckit.plan`.
5. Report back: branch name, spec file path, number of user stories, and any `[NEEDS CLARIFICATION]` markers left for `/speckit.clarify` to resolve.
