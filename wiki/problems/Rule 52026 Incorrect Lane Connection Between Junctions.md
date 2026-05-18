---
type: problem
status: open
---

# Rule 52026 — Incorrect Lane Connection Between Junctions

**Severity**: (unspecified)

## Summary

Rule 52026 fires when an incorrect lane connection exists between junctions — connectivity is created in the wrong direction or to the wrong target.

- **Count in DEU-01 FMO run**: 198 occurrences.
- **Example transaction**: `f0590ca1-422a-43aa-9779-24471f450f25` at 53.9409179, 10.2571595.

## Root Cause

Wrong lane connection between junctions, arising from derivation errors.

## Proposed Solution

Orbis improvement and/or improve lane connectivity logic in [[Lanes Automator]].

## Related

- [[concepts/Lane Connectivity]]
- [[systems/Orbis]]
- [[systems/Lanes Automator]]

*Source: `raw/confluence/Lanes FMO-- violation review.md`*
