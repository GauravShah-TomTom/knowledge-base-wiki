---
type: problem
status: open
---

# Rule 52261 — Carriageways Too Close Based Upon Number of Lanes

**Severity**: Warning, Normal

## Summary

Rule 52261 fires when the physical spacing between carriageways is too narrow relative to the number of lanes each carries. This is a geometric validation rule; carriageways should be widely spaced to accommodate a higher number of lanes.

- **Count in DEU-01 FMO run**: 335 occurrences.
- **Example transaction**: `e81b0467-4301-411d-a1cc-44aed72961d6` at 54.4732102, 9.0546438.

## Root Cause

Not dependent on the derivation pipeline or HD data quality — this reflects actual road geometry where carriageways are close together despite multiple lanes.

## Proposed Solution / Decision

Candidate for skipping from the [[projects/Lanes|Lanes project]] scope — no action required from the pipeline. See [[decisions/Skip Rule 52261 from Lanes Project Scope]].

## Related

- [[projects/Lanes]]

*Source: `raw/confluence/Lanes FMO-- violation review.md`*
