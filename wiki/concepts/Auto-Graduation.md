---
type: concept
---

# Auto-Graduation

Auto-Graduation is the automated pipeline that converts [[MEDS]] detector outputs into actual map fixes applied via external provider (e.g. [[TomTom]]) edit pipelines. It is the "graduation" of a detection into a confirmed, applied correction.

*Source: raw/scans/MEDS Overview.pdf*

## How It Works

1. A [[MEDS]] detector produces a detection (e.g. a suspected missing road segment)
2. Auto-Graduation validates the detection against internal OPS analysis
3. The validated detection is packaged as a fix instruction for the TomTom pipeline (e.g. `AddSegment`, `DeleteTurnRestriction`)
4. The TomTom pipeline applies the fix to the map

## Performance by Detector

| Detector | Internal OPS accuracy | Pipeline action | Pipeline yield | Fixes/week |
|---|---|---|---|---|
| MissingRoad ([[GeoCatch]]) | 75% | AddSegment | 43% | ~600 |
| TurnPermitted | 80% | DeleteTurnRestriction | 15% | ~1,200 |
| MissingOneWay | 50–70% | MakeRoadOneWay | 13% | ~150 |
| TurnRestriction | ~50% | AddTurnRestriction | 5% | ~50 |
| InvalidPermanentBlockPassage (IPBP) | 80% | DeleteBarrier | TBD | TBD |

**Pipeline yield** = fraction of detections that result in a fix actually applied. Low yield (e.g. 5–15%) means most detections are filtered out by the TomTom pipeline.

## Related

- [[MEDS]] — source of detections
- [[Map Healing]] — broader practice
- [[TomTom]] — provider pipeline that applies the fixes
