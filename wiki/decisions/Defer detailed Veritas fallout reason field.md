---
type: decision
date: 2026-05-12
deciders: [Sunil Jaiswal, Aditya Krishna]
---

# Defer detailed Veritas fallout reason field

**Decision:** Defer adding a dedicated "fallout reason" text field to [[Veritas]] output (to surface per-lead exception details to [[Camunda]]). This is lower priority and not required for production deployment.

## Context

During sprint grooming on 2026-05-12, [[Sunil Jaiswal]] raised a sub-task to send the specific reason for a [[Veritas]] fallout back to [[Camunda]] (e.g. "maneuver ID not found", "CoreDB exception"). This would require adding a new field to the Veritas output model.

## Rationale

- The existing `verification_result` field already captures the generic fallout status.
- Production deployment deadline is end of May 2026; this sub-task is not on the critical path.
- The generic status approach (see [[Use generic CoreDB exception status for Veritas fallouts]]) is deemed sufficient for now.

## Status

Deprioritised. May be revisited after initial production deployment.

## Related

- [[Veritas]]
- [[Use generic CoreDB exception status for Veritas fallouts]]
- [[Veritas silently skipping leads]]
