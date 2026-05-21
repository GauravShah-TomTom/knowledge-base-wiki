---
type: problem
---

# Veritas Silent Lead Skipping

[[Veritas]] previously silently skipped leads when it could not find road IDs or maneuver IDs in [[CoreDB]], or encountered runtime exceptions during lookup. These leads produced no output and no [[Camunda]] task closure, causing tasks to remain open indefinitely.

## Impact

- Camunda tasks backed by silently-skipped leads were never closed
- The pipeline moved to [[Camunda]]-based task management (story context: integrating Camunda task closing into the Veritas flow), making this a **production blocker** — every consumed lead must produce a status

## Resolution (story 5950)

Add explicit fallout status handling in Veritas for all skip scenarios:
- Missing road ID in CoreDB → set "fallout missing feature" status
- Missing maneuver ID in CoreDB → set "fallout missing feature" status
- Runtime/CoreDB exception → set "not verified" (already handled) or appropriate exception status

See [[decisions/veritas-fallout-status-generic]] for the status design decision.

*Source: `raw/notes/Sprint grooming_ Quality improvement - PC restrictions.docx` — sprint grooming meeting 2026-05-12*
