---
type: concept
---

# PUDO — Pickup/Dropoff Location

A PUDO (Pickup/Dropoff) is a geographic location where Uber trips begin or end. Popular PUDOs — those with high trip frequency — are used by the **SegErr Detectors** in [[MEDS]] to identify missing road segments.

## Usage in MEDS SegErr Detection

1. Load popular PUDOs (high-frequency pickup or dropoff points)
2. For each PUDO, find the closest segment in [[UMM]]
3. If the distance to the nearest segment exceeds **50 metres**, flag a detection — the road serving that PUDO is likely missing from the map

**Output:** PUDO location + closest Segment ID (as an `AddSegment` candidate)

## Related

- [[MEDS]] — system that uses PUDOs for missing-segment detection
- [[UMM]] — road network searched for nearby segments
- [[Auto-Graduation]] — pipeline that may apply the resulting AddSegment fixes

*Source: `raw/scans/MEDS Overview.pdf`*
