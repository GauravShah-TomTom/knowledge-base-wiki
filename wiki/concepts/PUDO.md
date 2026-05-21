---
type: concept
---

# PUDO — Pickup / Dropoff Location

*Source: raw/scans/MEDS Overview.pdf*

A PUDO (Pickup/Dropoff) is a geographic location where Uber rides start or end. Popular PUDOs are used as a ground-truth signal in [[MEDS]]'s SegErr detector: if a high-traffic PUDO is more than 50 meters from any mapped road segment, it suggests a missing segment in the map.

## Usage in MEDS SegErr detector

1. Load popular PUDOs (filtered by trip frequency)
2. Find the closest road segment in [[UMM]] for each PUDO
3. If distance > 50 meters → produce a "Missing Segment" detection

## Related

- [[MEDS]] — uses PUDOs to detect missing road segments
- [[UMM]] — the map model against which PUDO proximity is checked
