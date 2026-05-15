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

*Source: `raw/transcripts/converted/2026-05-15 Lanes_Sprint_Planning.md`*
