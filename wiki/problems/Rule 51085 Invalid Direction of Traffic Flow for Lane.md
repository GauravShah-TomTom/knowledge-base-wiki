---
type: problem
status: open
---

# Rule 51085 — Invalid Direction of Traffic Flow for Lane

**Severity**: Rare Warning, Critical

## Summary

Rule 51085 fires when the direction of traffic flow (DTFR) on a lane does not match the road's DTFR. Somewhat similar to [[problems/Rule 51059 Lanes on Non-Payload Roads|Rule 51059]]: when a road is open in both directions but carries vehicle-type restrictions, lanes should inherit those restrictions.

- **Count in DEU-01 FMO run**: 1,382 occurrences.
- **Example transaction**: `acd28c8a-2b57-4fe5-bbcd-ff9db90beb9f` at 53.6072871, 9.6370286.

## Root Cause

Transaction logic that copies traffic flow from road elements does not correctly propagate vehicle-type traffic restrictions (e.g. specific vehicle categories) to lane level.

## Proposed Solution

Improve the transaction logic that copies traffic flow on road elements, focusing on traffic restriction propagation.

## Related

- [[problems/Rule 51059 Lanes on Non-Payload Roads]] — related DTFR mismatch rule
- [[concepts/DTFR]]
- [[systems/Lanes Automator]]

*Source: `raw/confluence/Lanes FMO-- violation review.md`*
