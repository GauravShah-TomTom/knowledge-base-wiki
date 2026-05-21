---
type: project
---

# Map Healing Project

*Source: raw/scans/MEDS Overview.pdf*

Map Healing is Uber's initiative to proactively detect and fix map data errors at scale, improving navigation quality for riders and drivers. The project is implemented through [[MEDS]] (Map Error Detection System).

## Goal

Detect, classify, and automatically fix map data errors before they impact trip quality — reducing navigation failures, wrong routing, and ETA inaccuracies caused by incorrect [[UMM]] data.

## Key deliverables

- **[[MEDS]]** — the Map Error Detection System platform with 7 detector types
- **[[Auto-Graduation]]** — automated fix pipeline applying thousands of map corrections per week via TomTom
- **[[MIT Reporting]]** — reporting and tracking for detections

## Impact (as of source document)

- ~2,000+ map fixes applied per week across all detector types
- TurnPermitted alone: ~1,200 fixes/week (DeleteTurnRestriction)
- MissingRoad (GeoCatch): ~600 fixes/week (AddSegment)

## Related

- [[MEDS]] — the system
- [[Map Healing]] (concept) — the broader practice
- [[Map Data Quality Issues]] — the problems being addressed
- [[Auto-Graduation]] — automated fix mechanism
