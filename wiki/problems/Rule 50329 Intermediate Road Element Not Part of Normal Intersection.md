---
type: problem
status: open
---

# Rule 50329 — Intermediate Road Element Not Part of Normal Intersection

## Summary

Rule 50329 fires when an [[Intermediate Roads|intermediate road element]] inside a junction is not recognised as part of a normal intersection. The [[Lanes]] pipeline has skipped creating lane information on these "normal" roads inside junction areas, because HD data models them as large junction areas with trajectories instead of centerlines.

## Root Cause

In [[HD Basemap]], some junctions are represented as large areas with HD trajectories rather than standard centerlines. When the [[Lanes Automator]] encounters these, it skips populating lane information on the intermediate road elements, which then triggers the violation.

- **Count in DEU-01 FMO run**: 37,115 occurrences; affected 5,129 unique transactions (36.4% of all QA transactions).
- **Example transaction**: `c3a3c801-49ef-4d5e-beed-f31a6d984e0f` at 54.2898788, 10.4342199.

## Proposed Solutions

1. **Default by main road**: Determine the main road by FRC/N2C; match lane count on the intermediate road accordingly. If lane counts differ, use the lower number.
2. **Derive from trajectories**: Identify parallel HD trajectories as proxy centerlines; assign the same lane count as the adjacent road.
3. **Orbis improvement**: Request Orbis to indicate lane counts on such intermediate road elements.

> **Note**: Roundabouts should be excluded from any automatic defaulting logic, at least initially.

## Implementation approach (2026-05-19)

[[Gaurav Shah]] is implementing the post-processing task (Route 5832) with this logic:

1. Check if the road element is part of a normal intersection or not.
2. If it is a normal intersection and the road is still in the "VR roads" category, apply lane count and lane connectivity accordingly (based on the highest-FRC / neighbouring road class).
3. Extend the output JSON metadata with the rule ID so each JSON file maps to exactly one transaction — this enables downstream tracing of which transaction fixed which rule.

A separate task is being created to wire up the upstream country driving direction property (currently hardcoded in `application.properties`) — see [[problems/Missing Country Driving Direction in Derivation]].

Testing plan: replicate 4–5 existing transactions (impacted by this rule) in the dev environment; full-zone testing on the test branch will cover all rules together.

Confluence page links are being added to the story for full test case details.

## Related

- [[concepts/Intermediate Roads]] — definition of intermediate road elements
- [[concepts/Lane Connectivity]] — connectivity derivation rules
- [[systems/Genesis]] — QA system that flags this violation
- [[systems/Orbis]] — potential source for improvement
- [[systems/HD Basemap]] — source of junction area modelling

*Sources: `raw/confluence/Lanes FMO-- violation review.md`, `raw/transcripts/converted/2026-05-19 Lanes_Sprint_Planning.md`*
