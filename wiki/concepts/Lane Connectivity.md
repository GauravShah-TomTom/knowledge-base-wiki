---
type: concept
---

# Lane Connectivity

Lane connectivity describes which lanes at an intersection or junction connect to which outgoing lanes, capturing legal and physical turn relationships between road segments.

In the [[Lanes]] project, lane connectivity is derived automatically from map data (HD data) and supplemented by default rules when the source data is incomplete. The derivation applies rules per intersection type (e.g., T-junctions / 3-valid junctions) and road classification.

## Key rules

| Rule ID | Description |
|---|---|
| Route 5832 | Post-processing task to add lanes at intersections (normal intersections, VR roads) |
| 51059 | Detect and filter lanes on non-payload roads |
| 51068 | Invalid lane connectivity — conflicting data between [[Genesis]] and [[Orbis]] sources (spike needed) |
| 50329 | DTFR story covering lane connectivity defaults |

## Handling missing data

When HD source data does not provide all possible connections for a junction, the pipeline fills in default connectivity. For 3-valid junctions (T-junctions), all three connections are considered valid; missing ones receive default values.

## FMO violation rules (DEU-01 zone run)

The following additional rule IDs were identified in the DEU-01 [[FMO]] run (14,055 total QA transactions):

| Rule ID | Description | Severity | Unique Txns |
|---|---|---|---|
| 50329 | Intermediate Road Element not part of Normal Intersection | — | 5,129 |
| 51684 | Missing Lane Connectivity (3-valent junctions) | — | 7,440 |
| 51147 | Missing Lane Connectivity (3-valent junctions) | — | 5,606 |
| 50311 | Incorrect Direction of Traffic Flow for Lane (connected lanes) | Error, Critical | — |
| 50263 | Traffic Flow Conflicting with Driving Side | Warning, Critical | — |
| 53161 | Invalid Lane Connection (crossing) | Rare Warning, Critical | — |
| 51830 | Incorrect relationship to Lane Connectivity | Error, Critical | — |
| 52379 | Incorrect Lane Connectivity Relationship | Error, Critical | — |
| 51083 | Incorrect Lane Divider Type or incorrect Lane Connectivity | Warning, Critical | — |
| 51149 | Incorrect Lane Divider Type or incorrect Lane Connectivity | — | — |
| 52261 | Carriageways too close based upon number of lanes | Warning, Normal | — |
| 53887 | Lane Connectivity conflicts with Lane Direction Category | Rare Warning, Critical | — |
| 52497 | Curvature at Junction (Linear Assignment Maneuver) | Error, Critical | — |
| 51062 | Incorrect Lane Connection | Rare Warning, Critical | — |
| 52124 | Incorrect Z-Levels for Lane Connectivity | Error, Critical | — |
| 52721 | Geometry of Composing Part does not match Composite Feature | — | — |
| 52026 | Incorrect Lane Connection between junctions | — | — |

See individual `wiki/problems/` pages for details.

*Sources: `raw/transcripts/converted/2026-05-15 Lanes_Sprint_Planning.md`, `raw/confluence/Lanes FMO-- violation review.md`*
