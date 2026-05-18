---
type: problem
status: open
---

# Rule 52379 — Incorrect Lane Connectivity Relationship

**Severity**: Error, Critical

## Summary

Rule 52379 fires when lane connectivities reference lanes that do not exist in the database — the connectivity was created for a lane count that doesn't match actual database state.

- **Count in DEU-01 FMO run**: 572 occurrences.
- **Example transaction**: `70954547-3a89-4750-93a8-5d0c981eb803` at 54.4861910, 9.7097606.

## Root Cause

The connectivity derivation logic does not enforce that connections are only created from/to lanes that actually exist in the database.

## Proposed Solution

Refinement in lane connectivity logic: guarantee that connectivity is only created from existing lanes.

## Related

- [[concepts/Lane Connectivity]]
- [[systems/Lanes Automator]]

*Source: `raw/confluence/Lanes FMO-- violation review.md`*
