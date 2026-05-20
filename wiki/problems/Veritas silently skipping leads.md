---
type: problem
status: in-progress
---

# Veritas silently skipping leads

[[Veritas]] currently silently skips leads when it cannot find required road IDs or maneuver IDs in [[CoreDB]], or when a runtime exception occurs during lead processing. These leads produce no output record, so the corresponding [[Camunda]] tasks are never closed.

## Impact

- Leads with missing road IDs or maneuver IDs in [[CoreDB]] are dropped without any status — [[Camunda]] tasks remain open indefinitely.
- Silently skipped leads are invisible in [[Veritas]] output, making it impossible to track or reconcile them.
- Blocking issue for production deployment: every task consumed from [[Camunda]] must be closeable.

## Root Cause

Veritas's code paths for missing road elements and missing maneuver IDs exit without writing a status to the output. The console log records these but no output record is produced.

## Resolution

Story 5950 (to be converted from task to user story): introduce explicit fallout statuses for these cases.

**Agreed approach (May 2026):**
- Introduce `FALLOUT_MISSING_FEATURE` (or equivalent generic) status for missing road ID / maneuver ID.
- Use existing generic `NOT_VERIFIED` / `4DB exception` status for runtime CoreDB exceptions.
- All skipped leads must appear in Veritas output with an appropriate status so Camunda tasks can be closed.

See [[Use generic CoreDB exception status for Veritas fallouts]].

## Related

- [[Veritas]]
- [[CoreDB]]
- [[Camunda]]
- [[Use generic CoreDB exception status for Veritas fallouts]]
- [[Veritas Uber ACI Flow Integration]]
- [[Sunil Jaiswal]]
