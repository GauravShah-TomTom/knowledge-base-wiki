---
type: decision
date: 2026-05-12
deciders: [Aditya Krishna, Sunil Jaiswal]
---

# Use generic CoreDB exception status for Veritas fallouts

**Decision:** Use a single generic fallout status (e.g. `FALLOUT_MISSING_FEATURE`) for all cases where [[Veritas]] cannot find a feature in [[CoreDB]] (missing road ID, missing maneuver ID, or runtime CoreDB exception), rather than introducing separate per-exception-type statuses.

## Context

During sprint grooming on 2026-05-12, the team discussed how [[Veritas]] should handle leads that are currently silently skipped. Two options were considered:
1. Individual statuses per fallout type (one for missing road ID, one for missing maneuver ID, one for CoreDB exception).
2. A single generic fallout status for all missing-feature scenarios.

## Rationale

[[Aditya Krishna]] determined that propagating the generic `4DB exception` status as the verification result is sufficient. The specific reason for each fallout (e.g. "maneuver ID missing" vs "road ID missing") does not need to be surfaced separately in the current implementation.

A separate lower-priority sub-task to send detailed fallout reason text was deprioritised and is not blocking production deployment. See [[Defer detailed Veritas fallout reason field]].

## Implementation

- Add a new `FALLOUT_MISSING_FEATURE` status (or equivalent) in [[Veritas]].
- Apply this status wherever leads are currently silently skipped (missing road ID, missing maneuver ID, any similar CoreDB lookup failure).
- Story: task 5950 (to be converted to user story).

## Related

- [[Veritas]]
- [[CoreDB]]
- [[Veritas silently skipping leads]]
- [[Defer detailed Veritas fallout reason field]]
