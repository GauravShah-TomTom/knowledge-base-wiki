---
type: concept
---

# Auto-Graduation

*Source: raw/scans/MEDS Overview.pdf*

Auto-Graduation is [[MEDS]]'s automated map fix pipeline. When a detector produces a high-confidence detection, Auto-Graduation automatically submits the corresponding fix to the TomTom map provider pipeline without requiring manual review. This enables [[Map Healing]] at scale.

## How it works

Each [[MEDS]] detector maps to a specific TomTom pipeline operation:

| Detector | Error type | TomTom operation |
|---|---|---|
| GeoCatch / MissingRoad | Missing road segment | AddSegment |
| TurnPermitted | Invalid turn restriction | DeleteTurnRestriction |
| OneWay / MissingOneWay | Missing one-way restriction | MakeRoadOneWay |
| TurnRestriction | Missing turn restriction | AddTurnRestriction |
| IPBP / InvalidPermanentBlockPassage | Invalid permanent barrier | DeleteBarrier |

## Performance (as of source document)

| Detector | Internal OPS accuracy | TomTom pipeline yield | Applied fixes/week |
|---|---|---|---|
| MissingRoad | 75% | 43% | 600 |
| TurnPermitted | 80% | 15% | 1,200 |
| MissingOneWay | 50–70% | 13% | 150 |
| TurnRestriction | ~50% | 5% | 50 |
| InvalidPermanentBlockPassage | 80% | TBD | TBD |

"Pipeline yield" is the fraction of MEDS detections that TomTom's own validation pipeline accepts and applies. Internal OPS accuracy is Uber's manual evaluation of detection correctness before TomTom filtering.

## Related

- [[MEDS]] — the system that drives auto-graduation
- [[Map Healing]] — the broader initiative auto-graduation enables
- [[MIT Reporting]] — parallel reporting destination for detections
