---
type: problem
status: open
---

# Rule 53887 — Lane Connectivity Conflicts with Lane Direction Category

**Severity**: Rare Warning, Critical

## Summary

Rule 53887 fires when the Lane Direction Category (e.g. "Only Left") of a lane is violated by its connectivity. A lane marked "Only Left" should connect only to a left-turn lane, not straight-ahead. Any other connectivity causes this rule to fire.

- **Count in DEU-01 FMO run**: 303 occurrences.
- **Example transaction**: `751aeacf-a203-490d-99e2-f9057c86b8c1` at 53.8172101, 10.1735019.

## Root Cause

Lane Direction Category data from [[Orbis]] is not being respected during connectivity derivation.

## Proposed Solution

Orbis improvement needed: Lane Direction Category data needs to be correctly reflected in connectivity generation.

## Related

- [[concepts/Lane Connectivity]]
- [[systems/Orbis]]
- [[systems/Lanes Automator]]

*Source: `raw/confluence/Lanes FMO-- violation review.md`*
