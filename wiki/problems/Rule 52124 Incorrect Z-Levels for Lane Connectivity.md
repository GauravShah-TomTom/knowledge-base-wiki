---
type: problem
status: open
---

# Rule 52124 — Incorrect Z-Levels for Lane Connectivity

**Severity**: Error, Critical

## Summary

Rule 52124 fires when the sequence of composition for a lane connectivity object is incorrect. The correct sequence is: First Road Element → Junction → Intermediate Road Element → Last Road Element. Deviations from this order trigger the rule.

- **Count in DEU-01 FMO run**: 250 occurrences.
- **Example transaction**: `09211602-5b09-4638-a370-bb91233fe900` at 54.3321177, 10.1197807.

## Root Cause

Incorrect derivation of lane connectivity composition/sequencing in [[Lanes Automator]].

## Proposed Solution

Review and improve the derivation logic for lane connectivity sequences.

## Related

- [[concepts/Lane Connectivity]]
- [[systems/Lanes Automator]]

*Source: `raw/confluence/Lanes FMO-- violation review.md`*
