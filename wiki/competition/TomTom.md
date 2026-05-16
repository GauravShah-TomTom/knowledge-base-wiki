---
type: competition
---

# TomTom

TomTom is a Dutch mapping and location technology company. In Uber's context, TomTom functions both as a **map data provider** (supplying the [[UMM|Uber Map Model]] with road segments, maneuvers, and road furniture) and as the pipeline through which [[MEDS]] auto-graduated map fixes are applied.

## Role at Uber

- **Data provider**: TomTom supplies map data ingested into [[UMM]]. UMM entities carry `providersData` with `"provider": "TOMTOM"`, versioned release identifiers, and TomTom-specific feature type codes (`mnrFeatureType`).
- **Fix pipeline**: [[Auto-Graduation|Auto-graduated]] [[MEDS]] detections are sent to the TomTom pipeline, which applies corrections (AddSegment, DeleteTurnRestriction, MakeRoadOneWay, AddTurnRestriction, DeleteBarrier) to the map.
- **[[HD Basemap]]**: TomTom produces the HD Basemap product — a high-definition map with detailed road geometry, lane models, and junction topology — which is published via the [[Map Content Portal]] and available through [[Orbis]].

## Competitive Relevance

TomTom is a major player in the HD mapping market alongside HERE and others. While currently a supplier to Uber's map pipeline, TomTom's own mapping products (HD Map, navigation SDKs) compete in the autonomous vehicle and fleet navigation space.

## Related

- [[UMM]] — internal map model populated with TomTom data
- [[MEDS]] — map error detection system that sends fixes back to TomTom
- [[Auto-Graduation]] — the pipeline that routes fixes through TomTom
- [[HD Basemap]] — TomTom's HD map product used by Uber
- [[Map Content Portal]] — portal used to access TomTom map releases

*Source: `raw/scans/MEDS Overview.pdf`, `raw/slack/adas-hd-basemap-lanes-general/2026-05-13 18_20_40 - reply - 2026-05-14 09_44_31.md`*
