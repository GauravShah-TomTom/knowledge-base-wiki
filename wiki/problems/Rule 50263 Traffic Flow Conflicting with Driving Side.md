---
type: problem
status: open
---

# Rule 50263 — Traffic Flow Conflicting with Driving Side

**Severity**: Warning, Critical

## Summary

Rule 50263 fires when lane traffic flow does not follow the driving side of the country. For a 2-way open road, there should be either one lane in each direction or one bidirectional lane. This violation can result from incorrect lane information in [[HD Basemap|HD]] data.

- **Count in DEU-01 FMO run**: 2,489 occurrences.
- **Example transaction**: `457576b0-5969-45c9-bba2-3e68802f23cd` at 54.0414632, 9.3480155.

## Root Cause

Incorrect HD lane information. Often co-occurs with [[problems/Rule 51059 Lanes on Non-Payload Roads|Rule 51059 (DTFR for Lane and Road not in line)]].

## Proposed Solution

When a single lane is present on a bidirectional road, create a bidirectional lane and set correct lane connectivity. This generally resolves both rule 50263 and rule 51059 together.

## Related

- [[problems/Rule 51059 Lanes on Non-Payload Roads]] — co-occurring violation; joint fix
- [[concepts/Lane Connectivity]]
- [[systems/HD Basemap]]

*Source: `raw/confluence/Lanes FMO-- violation review.md`*
