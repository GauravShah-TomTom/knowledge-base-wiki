---
type: decision
---

# Decision: Use TomTom Pipeline for Automated Map Fix Application

*Source: raw/scans/MEDS Overview.pdf*

## Decision

[[MEDS]] detector outputs are automatically applied as map fixes via TomTom's editorial pipeline ([[Auto-Graduation]]), rather than requiring manual human review for every detection.

## Rationale

- [[MEDS]] detectors produce high volumes of detections (hundreds to thousands per week per detector type).
- Manual review at that scale is infeasible.
- Internal OPS analysis shows detector accuracy is sufficiently high (50–80% depending on detector) to justify automated submission.
- TomTom's own pipeline acts as a second validation layer, further filtering detections before they are applied (though pipeline yield is low — 5–43% depending on detector type).

## Trade-offs

| Pro | Con |
|---|---|
| Scales map healing to thousands of fixes/week | TomTom pipeline yield is low (e.g., only 43% for MissingRoad, 5% for TurnRestriction) |
| No manual review bottleneck | Incorrect detections can propagate to the live map |
| Provider handles change validation | Dependent on TomTom's pipeline acceptance criteria |

## Per-detector operations

| Detector | TomTom operation | Fixes/week |
|---|---|---|
| MissingRoad | AddSegment | 600 |
| TurnPermitted | DeleteTurnRestriction | 1,200 |
| MissingOneWay | MakeRoadOneWay | 150 |
| TurnRestriction | AddTurnRestriction | 50 |
| IPBP | DeleteBarrier | TBD |

## Related

- [[MEDS]] — the detection system
- [[Auto-Graduation]] — the pipeline concept
- [[Map Healing]] — overarching initiative
