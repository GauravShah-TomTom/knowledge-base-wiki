---
type: problem
status: open
---

# Rule 51059 — Lanes on Non-Payload Roads

## Summary

Story 505-1059 / rule 51059: lanes appearing on non-payload roads need to be detected and filtered. The [[Lanes]] pipeline currently cannot reliably identify and remove lane data that is attached to roads that should not carry payload.

## Scenarios

Four scenarios involving directional closures and vehicle restrictions were identified:
1. Road closed in one direction for all vehicles, open for all vehicles in the other.
2. Road closed in both directions for specific vehicle types.
3. Road closed in one direction for all vehicles, open for specific vehicles in the other.
4. Road open in both directions, but the street data provides only one lane (forward or backward).

Subtasks will be created for each scenario plus a testing subtask (4–5 sample transactions in dev; full zone testing on test branch).

## Owner

Speaker 3 (name not captured in transcript).

## Additional context (from FMO review)

The [[concepts/FMO|FMO]] violation review for zone DEU-01 describes rule 51059 as "DTFR for Lane and Road not in line" with two distinct scenarios:
1. A road element has a traffic restriction (e.g. closed for medium trucks) that HD does not reflect at the lane level — all lanes appear open for all vehicles.
2. A road open in both directions has only one lane populated in one direction, causing the violation.
- **Count in DEU-01 FMO run**: 5,763 occurrences; affected 3,346 unique transactions (23.8% of all QA transactions).
- **Example transactions**: `36a315bc-5e73-4bea-b52c-f9c0511daafb` (scenario 1), `5aa9db90-abf5-418c-8dba-89237b27b676` (scenario 2).

**Proposed solutions**:
1. Modify DTFR of lane to match road restriction; close the lane for the restricted direction.
2. If only one lane is to be populated on a side road, create it with no DTFR restriction.

Often co-occurs with [[problems/Rule 50263 Traffic Flow Conflicting with Driving Side|Rule 50263]]; a joint fix (bidirectional lane creation) can resolve both.

*Sources: `raw/transcripts/converted/2026-05-15 Lanes_Sprint_Planning.md`, `raw/confluence/Lanes FMO-- violation review.md`*
