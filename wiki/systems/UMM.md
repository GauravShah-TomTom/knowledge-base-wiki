---
type: system
---

# UMM — Uber Map Model

The Uber Map Model (UMM) is the internal structured representation of road network data used across Uber's mapping and navigation systems.

*Source: raw/scans/MEDS Overview.pdf*

## Data Model

UMM entities include:

- **Segments** — directed road links between junctions
- **Junctions** — intersection/endpoint nodes
- **Maneuvers** — turn restrictions and allowed movements at junctions
- **Road furniture:**
  - Barriers (permanent or temporary blockages)
  - Signs
  - Traffic lights

## Schema

Each UMM entity has:

| Field | Description |
|---|---|
| `uuid` | Unique identifier |
| `geometry.point.latE7` / `lngE7` | Lat/lng encoded as integer × 10^7 |
| `data.maneuver` | Maneuver type and segment references |
| `providersData` | Provider (e.g. TomTom) version, tags, provider ID |
| `countryCode` | ISO country code (e.g. `BR`) |

Example maneuver data references two directed segments with `direction` fields and UUIDs; `mnrFeatureType` codes identify maneuver classification (e.g. `2103` = standard, `21031` = implicit, `2101` = calculated).

## Usage

UMM is a primary input to [[MEDS]] for barrier detection (IPBP) and turn restriction detection (TurnPermitted). Provider data from TomTom is embedded in UMM entities.

## Related

- [[MEDS]] — consumes UMM for map error detection
