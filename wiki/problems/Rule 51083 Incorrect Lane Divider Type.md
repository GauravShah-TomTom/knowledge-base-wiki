---
type: problem
status: open
---

# Rule 51083 — Incorrect Lane Divider Type or Incorrect Lane Connectivity

**Severity**: Warning, Critical

## Summary

Rule 51083 fires when turn lane dividers are solid where they should ideally not be, or when lane connectivity is incorrect. Solid dividers at turn lanes can indicate a data quality issue, though occasionally this reflects actual road reality.

- **Count in DEU-01 FMO run**: 557 occurrences.
- **Example transaction**: `751aeacf-a203-490d-99e2-f9057c86b8c1` at 53.8174655, 10.1738497.

## Root Cause

Lane dividers are not being populated correctly from HD data. Can also be a false positive when HD data and reality agree but the rule fires anyway.

## Proposed Solution / Decision

No action defined; populate dividers as per HD/reality. This rule may occasionally produce false positives.

See [[decisions/No Action for Lane Divider Rules 51083 and 51149]].

## Related

- [[problems/Rule 51149 Incorrect Lane Divider Type]] — same rule description, slightly different conditions
- [[concepts/Lane Connectivity]]
- [[systems/HD Basemap]]

*Source: `raw/confluence/Lanes FMO-- violation review.md`*
