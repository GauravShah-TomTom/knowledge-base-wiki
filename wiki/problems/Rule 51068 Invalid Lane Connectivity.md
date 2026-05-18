---
type: problem
status: open
---

# Rule 51068 — Invalid Lane Connectivity (Genesis vs Orbis Conflict)

## Summary

Rule 51068 fires when [[Genesis]] and [[Orbis]] provide conflicting lane connectivity data for the same road. The scenarios are varied and not yet fully catalogued.

## Current state

A spike story has been created to analyse the full set of scenarios (see [[decisions/Create Spike for Rule 51068 Before Implementing]]). Implementation will be groomed after the spike is complete.

- Spike owner: Niranjan
- Acceptance criteria: all scenarios documented in Confluence

## Context

[[Gaurav Shah]] noted this is a case where "Genesis is saying something and Orbis is saying something else, so the conflicting scenarios will cause this." Only 5–10 cases had been reviewed at sprint planning time.

## Additional context (from FMO review)

The FMO violation review provides additional detail: rule 51068 fires when existing restrictions on road elements — BP (barrier prohibition), DTFR (direction of traffic flow), maneuvers, GR (general restrictions), etc. — should prevent lane connectivity from being created, but the pipeline populates it anyway.
- **Count in DEU-01 FMO run**: 3,710 occurrences; affected 2,097 unique transactions (14.91% of all QA transactions).
- **Example transaction**: `bd3826da-9e8f-4cb7-8043-2c666cb0eaf0` at 54.5051924, 8.9377945.
- **Proposed solution (FMO review)**: Orbis improvement — confirm whether Orbis takes into account maneuvers, DTFR, GR when creating connectivities; if not, determine whether to ignore such connectivities.

*Sources: `raw/transcripts/converted/2026-05-15 Lanes_Sprint_Planning.md`, `raw/confluence/Lanes FMO-- violation review.md`*
