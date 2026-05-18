---
type: problem
status: open
---

# Rule 51149 — Incorrect Lane Divider Type or Incorrect Lane Connectivity

**Severity**: (unspecified)

## Summary

Rule 51149 is similar to [[problems/Rule 51083 Incorrect Lane Divider Type|Rule 51083]]. It fires when lane dividers are populated incorrectly or lane connectivity is wrong. Dividers should be populated as per reality.

- **Count in DEU-01 FMO run**: 387 occurrences.
- **Example transaction**: `ae08a947-8235-4a91-a6da-75b86116b70d` at 53.8126690, 10.3288546.

## Root Cause

Same as [[problems/Rule 51083 Incorrect Lane Divider Type|Rule 51083]]: lane dividers not correctly populated from HD data; occasionally a false positive.

## Proposed Solution / Decision

No action defined; populate dividers as per HD/reality.

See [[decisions/No Action for Lane Divider Rules 51083 and 51149]].

## Related

- [[problems/Rule 51083 Incorrect Lane Divider Type]] — same rule family
- [[systems/HD Basemap]]

*Source: `raw/confluence/Lanes FMO-- violation review.md`*
