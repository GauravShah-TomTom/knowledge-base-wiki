---
type: problem
status: open
---

# Rule 52721 — Geometry of Composing Part Does Not Match Composite Feature

**Severity**: (unspecified)

## Summary

Rule 52721 fires when the geometry of a composing part does not match the geometry of the composite feature it belongs to. In the context of lane connectivity, this results from incorrect "Level 2" feature lane connectivity caused by cascade failure.

- **Count in DEU-01 FMO run**: 209 occurrences.
- **Example transaction**: `68baee5b-1830-4c6a-afb6-a2acedc8c795` at 53.7784910, 9.9784629.

## Root Cause

Incorrect lane connectivity creation leads to a cascade failure when composing the higher-level ("Level 2") lane connectivity feature. [[HD Basemap|HD data]] inaccuracies at the affected location contribute to derivation errors.

## Proposed Solution

Improve lane connectivity logic. HD data at the affected junction also needs improvement.

## Related

- [[concepts/Lane Connectivity]]
- [[systems/HD Basemap]]
- [[systems/Lanes Automator]]

*Source: `raw/confluence/Lanes FMO-- violation review.md`*
