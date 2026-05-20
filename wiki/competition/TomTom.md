---
type: competition
---

# TomTom

TomTom is an external mapping and location technology company that provides map data and edit pipelines used by Uber for map correction workflows.

*Source: raw/scans/MEDS Overview.pdf*

## Role in Uber's Map Stack

TomTom serves as a **map data provider** in Uber's ecosystem. [[MEDS]] [[Auto-Graduation]] feeds verified map error detections into the TomTom pipeline, which applies the actual corrections to the map:

| Fix type | TomTom action |
|---|---|
| Missing road | `AddSegment` |
| Invalid turn restriction | `DeleteTurnRestriction` |
| Missing one-way | `MakeRoadOneWay` |
| Missing turn restriction | `AddTurnRestriction` |
| Invalid permanent barrier | `DeleteBarrier` |

TomTom provider data is also embedded in [[UMM]] entities (via `providersData`) and is used in maneuver feature type classification (`mnrFeatureType`).

## Related

- [[MEDS]] — produces detections fed into TomTom pipeline
- [[Auto-Graduation]] — pipeline that sends fixes to TomTom
- [[UMM]] — contains TomTom provider data
