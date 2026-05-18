---
type: problem
status: open
---

# Rule 52497 — Curvature at Junction Starts and Ends at Same Location

**Severity**: Error, Critical

## Summary

Rule 52497 fires when the curvature at a junction starts and ends at the same location for all linear assignment maneuvers on that junction. This is caused by the presence of a Linear Assignment Maneuver (LAM).

- **Count in DEU-01 FMO run**: 281 occurrences.
- **Example transaction**: `ebc265e4-3549-4d36-8d95-697db765f40f` at 54.2728757, 10.0173329.

## Root Cause

Presence of Linear Assignment Maneuver objects at the junction.

## Proposed Solution

Needs more investigation.

## Related

- [[concepts/Lane Connectivity]]
- [[systems/Lanes Automator]]

*Source: `raw/confluence/Lanes FMO-- violation review.md`*
