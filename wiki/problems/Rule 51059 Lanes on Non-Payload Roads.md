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

*Source: `raw/transcripts/converted/2026-05-15 Lanes_Sprint_Planning.md`*
