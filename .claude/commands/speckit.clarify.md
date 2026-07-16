---
description: "Identify and resolve ambiguities in the current feature spec before planning"
---

# Clarify Feature Specification

## User Input

```text
$ARGUMENTS
```

Consider the user input if provided — it may target specific sections to clarify.

## Execution

1. Resolve paths: `bash .specify/scripts/bash/check-prerequisites.sh --json --paths-only`. Read `FEATURE_SPEC` from the output.
2. Read the spec. Scan for:
   - Explicit `[NEEDS CLARIFICATION: ...]` markers
   - Vague quantifiers ("fast", "scalable", "many users") without a measurable success criterion
   - Missing edge cases implied by the user stories
   - Requirements that assume a technical choice not actually decided
3. For each ambiguity found, ask the user a **single, specific, answerable question** (prefer a short multiple-choice list over an open question). Ask them one at a time — do not dump the whole list at once unless the user explicitly asked for a batch review.
4. After each answer, immediately update the spec in place: replace the `[NEEDS CLARIFICATION: ...]` marker or vague wording with the resolved requirement/success criterion. Do not wait until the end to write changes.
5. Stop when there are no more blocking ambiguities, or the user says to proceed as-is.
6. Report a short summary: how many ambiguities were found, how many resolved, and any the user chose to leave open (call these out explicitly so `/speckit.plan` doesn't silently assume).
