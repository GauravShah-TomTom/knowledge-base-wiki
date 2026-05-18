---
type: problem
status: open
---

# Rule 51830 — Incorrect Relationship to Lane Connectivity

**Severity**: Error, Critical

## Summary

Rule 51830 fires due to haphazard or incorrect lane connectivity that causes incorrect relationships between lane connectivity objects.

- **Count in DEU-01 FMO run**: 1,232 occurrences.
- **Example transaction**: `a9001aef-5dc3-4840-94f9-c071486a03e4` at 54.7064429, 9.5306095.

## Root Cause

Incorrect lane connectivity derivation. The affected junction has an intermediate road element that was not correctly identified, leading to disorganised connectivity.

## Proposed Solution

Correctly identify the intermediate road element and improve lane connectivity derivation. HD data at such junctions also needs improvement.

## Related

- [[concepts/Lane Connectivity]]
- [[concepts/Intermediate Roads]]
- [[systems/HD Basemap]]
- [[systems/Lanes Automator]]

*Source: `raw/confluence/Lanes FMO-- violation review.md`*
