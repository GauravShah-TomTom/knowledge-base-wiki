---
type: concept
---

# Transition Traversal

*Source: raw/scans/MEDS Overview.pdf*

Transition Traversal data tracks, for each 3-segment turn sequence (From → Via → To), how many times that sequence was **suggested** by navigation versus how many times it was actually **traversed** by drivers. This is the turn-level input signal for [[MEDS]], providing finer granularity than [[Segment Traversal]].

## Data schema

| Field | Description |
|---|---|
| Segment From | The segment a driver is coming from |
| Segment Via | The intermediate segment (the turn corridor) |
| Segment To | The segment a driver continues onto |
| DateTime | Time window of the measurement |
| Suggested | Count of trips where navigation suggested this transition |
| Traversed | Count of trips where a driver actually took this transition |

## Example

| Segment From | Segment Via | Segment To | DateTime | Suggested | Traversed |
|---|---|---|---|---|---|
| seg-1 | seg-2 | seg-3 | 2026-01-01 12:00 | 12 | 12 |
| seg-1 | seg-4 | seg-5 | 2026-01-01 12:00 | 16 | 15 |
| seg-2 | seg-3 | seg-7 | 2026-01-01 13:00 | 122 | 18 |

The third row is suspicious: 122 suggestions but only 18 traversals, indicating a likely turn restriction or physical barrier on the via segment.

## Usage in MEDS detectors

- **TurnPermitted** — identifies restricted maneuvers that drivers are actually traversing (threshold: ≥21 traversals of a restricted transition)
- **IPBP** — joins barrier data with 3-segment transition traversal data to detect invalid permanent barriers
- **TurnRestriction** — uses traversal rates of problematic vs. alternative transitions to detect missing turn restrictions

## Related

- [[MEDS]] — primary consumer
- [[Segment Traversal]] — the segment-level (2-point) variant of this signal
- [[Route Divergence]] — the divergence-level signal
