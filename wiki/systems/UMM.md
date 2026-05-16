---
type: system
---

# UMM — Uber Map Model

The Uber Map Model (UMM) is Uber's internal map data schema. It is the canonical representation of the road network used by navigation, routing, and map-quality systems including [[MEDS]].

## Schema

Each UMM entity has:
- `uuid` — globally unique identifier
- `geometry` — lat/lng in E7 integer format (e.g. `"latE7": -234799350`)
- `data` — entity-type-specific payload (e.g. maneuver, segment reference)
- `providersData` — array of provider records (e.g. TomTom version, mnrFeatureType)
- `countryCode` — ISO country code (e.g. `"BR"`)

## Entity Types

| Entity | Description |
|---|---|
| **Segments** | Directed road segments connecting two junctions |
| **Junctions** | Intersection nodes at which segments meet |
| **Maneuvers** | Turn instructions and turn restrictions at junctions |
| **Road furniture** | Physical features on roads: barriers (permanent blockages), signs, traffic lights |

## Provider Data

UMM entities carry `providersData` from map suppliers. The primary provider is [[TomTom]] (`"provider": "TOMTOM"`), with versioned data (e.g. `"1106820223 – 1106820716"`) and feature type codes (`mnrFeatureType`). Key mnrFeatureType values used in [[MEDS]] filtering:

- `21031` — implicit turn (excluded from TurnPermitted detector)
- `2101` — calculated turn (excluded from TurnPermitted detector)
- `2103` — referenced in maneuver data

## Usage in MEDS

[[MEDS]] queries UMM to:
- Retrieve maneuver records for the TurnPermitted and TurnRestriction detectors
- Retrieve permanent barrier records for the IPBP detector
- Check topological connectivity (junction sharing, 3-hop connectivity) for the GeoCatch detector

## Related

- [[MEDS]] — main consumer of UMM data for map error detection
- [[TomTom]] — primary UMM data provider
- [[Route Divergence]] — signal that MEDS overlays against UMM topology

*Source: `raw/scans/MEDS Overview.pdf`*
