---
type: system
---

# CoreDB

CoreDB (also referred to as "4DB" in transcripts) is the organisation's core road network database. It stores road IDs, branch IDs, and maneuver IDs used by the [[Veritas]] pipeline for restriction verification.

## Role in Veritas Pipeline

When [[Veritas]] processes a lead, it looks up:
- **Road IDs** — to validate physical road elements
- **Maneuver IDs** — to validate turn restriction records

If a road ID or maneuver ID is not found in CoreDB (e.g. because the record was removed), Veritas previously silently skipped the lead. The current work (May 2026) introduces an explicit `FALLOUT_MISSING_FEATURE` status for these cases. See [[Veritas silently skipping leads]].

## Known Issues

- `CoreDB` exceptions at runtime (e.g. branch ID lookups) are caught and lead to `NOT_VERIFIED` status in Veritas; a generic exception status is considered sufficient without per-exception detail. See [[Use generic CoreDB exception status for Veritas fallouts]].

## Related

- [[Veritas]]
- [[Veritas silently skipping leads]]
