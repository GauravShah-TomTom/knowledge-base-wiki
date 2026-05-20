---
type: decision
date: 2026-05-12
deciders: [Sunil Jaiswal, Aditya Krishna]
status: pending-verification
---

# Use task ID as restriction ID instead of external ID in Veritas

**Decision (pending verification):** Use the [[Camunda]] task ID as the restriction ID to close Camunda tasks, instead of adding a separate `externalId` field to the [[Veritas]] output model.

## Context

Story 5952 proposed adding an `externalId` field to the Veritas model, populated with a value that [[Camunda]] could use to close the corresponding task. During sprint grooming on 2026-05-12, [[Sunil Jaiswal]] suggested that the task ID already present in the system may be usable directly as the restriction ID.

## Rationale

If the task ID can serve as the restriction ID, no schema change to the Veritas output model is needed. This simplifies the implementation and avoids the invalid-XML issue with an empty `externalId` field (see [[Empty external ID causes invalid XML in Veritas]]).

## Status

**Pending verification** — [[Sunil Jaiswal]] to confirm whether using task ID as restriction ID works for closing Camunda tasks. If it works, story 5952 (add external ID) may be dropped or significantly reduced in scope.

## Related

- [[Veritas]]
- [[Camunda]]
- [[Empty external ID causes invalid XML in Veritas]]
- [[Guard Veritas XML against empty transition metadata fields]]
