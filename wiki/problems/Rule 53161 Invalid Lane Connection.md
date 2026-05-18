---
type: problem
status: open
---

# Rule 53161 — Invalid Lane Connection (Crossing)

**Severity**: Rare Warning, Critical

## Summary

Rule 53161 fires when lane connectivities departing from the same road element cross each other. Connected lanes departing from the same road element must not cross.

- **Count in DEU-01 FMO run**: 2,065 occurrences.
- **Example transaction**: `8f04b539-e635-483c-b142-d020918a8f7e` at 53.7750315, 9.6616162.

## Root Cause

Seen over junctions where lane connectivities exist instead of lane centerlines. Crossing connectivities indicate that the lane topology at the junction is incorrectly derived.

## Proposed Solution

Improve lane connectivity derivation over junctions. Ensure that connectivities departing from the same road element do not cross each other.

## Related

- [[concepts/Lane Connectivity]]
- [[systems/Lanes Automator]]

*Source: `raw/confluence/Lanes FMO-- violation review.md`*
