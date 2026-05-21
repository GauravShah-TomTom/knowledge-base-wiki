---
type: concept
---

# Segment Traversal

*Source: raw/scans/MEDS Overview.pdf*

Segment Traversal data tracks, for each directed road segment (identified by start junction → end junction), how many times it was **suggested** by navigation versus how many times it was actually **traversed** by drivers. This is one of the core input signals for [[MEDS]] detectors.

## Data schema

| Field | Description |
|---|---|
| Segment ID | Identifier of the road segment |
| Start Junction | Origin junction of the directed segment |
| End Junction | Destination junction of the directed segment |
| DateTime | Time window of the measurement |
| Suggested | Count of trips where navigation routed through this segment |
| Traversed | Count of trips where a driver actually drove this segment |

## Example

| Segment ID | Start Junction | End Junction | DateTime | Suggested | Traversed |
|---|---|---|---|---|---|
| segment-1 | J_1 | J_2 | 2026-01-01 12:00 | 16 | 3 |
| segment-1 | J_2 | J_1 | 2026-01-01 12:00 | 22 | 21 |
| segment-2 | J_3 | J_4 | 2026-01-01 13:00 | 8 | 12 |

A low traversal ratio (suggested >> traversed) for a directed segment indicates a potential map error (e.g., wrong one-way designation, blocked road).

## Usage in MEDS detectors

- **OneWay detector** uses traversal% to identify incorrectly bidirectional segments
- **Blocked Road detector** uses traversals = 0 with high suggestions to detect missing blockpassage
- **TurnPermitted** uses traversal counts as part of its threshold logic

## Related

- [[MEDS]] — consumer
- [[Transition Traversal]] — the 3-segment (turn-level) variant of this signal
- [[Route Divergence]] — related signal capturing segment-level divergences
