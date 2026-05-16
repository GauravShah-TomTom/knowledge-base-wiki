---
type: system
---

# MEDS — Map Error Detection System

MEDS is Uber's automated map-healing platform that proactively detects, classifies, and fixes map data errors by analysing driver behaviour signals (route divergences, segment traversals, transition traversals) against the [[UMM|Uber Map Model]].

Detected issues are reported via MIT (Map Issue Tracking) and can be automatically graduated into map corrections through the [[TomTom]] pipeline.

## Purpose

Drivers frequently diverge from navigation-suggested routes when the underlying map data is wrong (missing roads, incorrect turn restrictions, wrong one-way markings, blocked roads). MEDS turns these divergence signals into actionable map corrections at scale — without requiring manual human review for every fix.

## Input Signals

| Signal | Description |
|---|---|
| **Route Divergences** | When a driver takes a different segment than the one suggested by navigation. Produced by comparing PTMMT segment sequences against Navigation Route Suggestions via a Divergence Calculator. |
| **Segment Traversals** | Count of actual traversals per segment per direction, per time window. Used to measure how often drivers use a given segment. |
| **Transition Traversals** | Count of actual 3-segment transitions (from → via → to). Used to detect problematic turn behaviour. |
| **[[UMM]]** | The Uber Map Model: road segments, junctions, maneuvers, and road furniture (barriers, signs, traffic lights). |

## Detectors

MEDS has 7 detectors, each targeting a class of map error:

| # | Detector | Error Class | Key Threshold |
|---|---|---|---|
| 1 | **[[GeoCatch]]** | Missing Roads | ≥ 12 trips diverging; segments not sharing junction; not connected within 3 hops |
| 2 | **TurnPermitted** | Invalid Turn Restrictions | Restricted transitions ≥ 21 AND ≥ 5% of first-segment traffic |
| 3 | **IPBP** | Invalid Permanent Barriers | Actual traversals through barrier ≥ 20 |
| 4 | **OneWay** | Missing One-Way Restrictions | Problem direction: suggestions ≥ 10 AND traversal% ≤ 15%; opposite direction: traversals ≥ 10 AND traversal% ≥ 80% |
| 5 | **TurnRestriction** | Missing Turn Restrictions | ALL of: suggestions ≥ 20, traversal rate ≤ 20%, alt rate ≥ 80%, alt count ≥ 100 |
| 6 | **Blocked Road Detector** | Missing Permanent Barriers | Both directions: suggestions ≥ 10 AND traversals = 0 |
| 7 | **SegErr Detectors** | Missing Segments | Popular PUDO > 50 m from nearest segment |

## Auto-Graduation Stats

Detections that pass confidence thresholds are automatically graduated to [[TomTom]] pipeline map fixes:

| Detector | Internal OPS accuracy | TomTom fix type | Pipeline yield | Applied fixes/week |
|---|---|---|---|---|
| MissingRoad | 75% | AddSegment | 43% | ~600 |
| TurnPermitted | 80% | DeleteTurnRestriction | 15% | ~1 200 |
| MissingOneWay | 50–70% | MakeRoadOneWay | 13% | ~150 |
| TurnRestriction | ~50% | AddTurnRestriction | 5% | ~50 |
| InvalidPermanentBlockPassage | 80% | DeleteBarrier | TBD | TBD |

TurnPermitted has the highest throughput (1 200 fixes/week) due to its high internal OPS accuracy (80%), even though its pipeline yield is only 15%.

## Architecture

```
transition traversals ─┬─► MissingRoad Detector (GeoCatch) ─┐
segment traversals     ├─► TurnRestriction Detector          ├─► MIT reporting
Route Divergences      ├─►     ...                           │
UMM                    └─► OneWay Detector ──────────────────┘
```

## Related

- [[UMM]] — internal map data model that MEDS queries
- [[GeoCatch]] — missing-roads detector within MEDS
- [[TomTom]] — map data provider; applies auto-graduated fixes
- [[Map Healing]] — the broader concept MEDS implements
- [[Route Divergence]] — primary input signal
- [[Auto-Graduation]] — automated detection-to-fix pipeline

*Source: `raw/scans/MEDS Overview.pdf`*
