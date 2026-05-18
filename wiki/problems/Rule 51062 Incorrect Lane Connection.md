---
type: problem
status: open
---

# Rule 51062 — Incorrect Lane Connection

**Severity**: Rare Warning, Critical

## Summary

Rule 51062 fires due to incorrect lane connectivity derivation at junctions.

- **Count in DEU-01 FMO run**: 265 occurrences.
- **Example transaction**: `22c8d4ba-122b-4d4a-a017-420ea2e1819e` at 54.3072634, 10.6521663.

## Root Cause

Incorrect lane connectivity derivation in [[Lanes Automator]].

## Proposed Solution

Improve lane connectivity logic at junctions.

## Related

- [[concepts/Lane Connectivity]]
- [[systems/Lanes Automator]]

*Source: `raw/confluence/Lanes FMO-- violation review.md`*
