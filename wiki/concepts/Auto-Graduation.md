---
type: concept
---

# Auto-Graduation

Auto-Graduation is the automated pipeline that converts [[MEDS]] map error detections into applied map fixes, without requiring human review for every individual detection. Detections that meet confidence thresholds are automatically "graduated" to the [[TomTom]] pipeline, which applies the corresponding map edits.

## How It Works

1. [[MEDS]] detectors produce candidate map errors (e.g. a missing road segment, an invalid turn restriction).
2. Each detection is assessed against confidence thresholds (internal OPS analysis accuracy).
3. Detections exceeding the threshold are passed to the [[TomTom]] pipeline as a specific fix type (e.g. `AddSegment`, `DeleteTurnRestriction`).
4. TomTom's pipeline applies the fix to the map data.
5. The overall throughput metric is **Pipeline yield** — the fraction of MEDS detections that result in an accepted map fix.

## Performance by Detector

| Detector | Accuracy (OPS) | Fix type | Pipeline yield | Fixes/week |
|---|---|---|---|---|
| MissingRoad (GeoCatch) | 75% | AddSegment | 43% | ~600 |
| TurnPermitted | 80% | DeleteTurnRestriction | 15% | ~1 200 |
| MissingOneWay | 50–70% | MakeRoadOneWay | 13% | ~150 |
| TurnRestriction | ~50% | AddTurnRestriction | 5% | ~50 |
| InvalidPermanentBlockPassage | 80% | DeleteBarrier | TBD | TBD |

**Key insight:** TurnPermitted generates the most fixes per week (1 200) despite a low pipeline yield (15%) because it produces a large volume of detections with high internal accuracy.

## Related

- [[MEDS]] — source of detections
- [[TomTom]] — pipeline that applies the graduated fixes
- [[Map Healing]] — broader concept
- [[GeoCatch]] — missing-roads detector with 43% pipeline yield

*Source: `raw/scans/MEDS Overview.pdf`*
