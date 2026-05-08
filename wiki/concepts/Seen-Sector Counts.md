---
type: concept
---

# Seen-Sector Counts

A per-sign property that records the count of vehicle observations grouped by the sector (angular bucket) from which a sign was seen. The complementary `not-seen-count-per-sector` records directions from which the sign was *not* observed. Together, these indicate the range of approach angles for a given sign.

Exposed via the [[FCD Cluster API]] as `Cluster.getSeenCountsPerSector()`.

## Motivation

At junctions, the same physical sign may be visible from multiple road directions, causing duplicate sign detections. Seen-sector counts can help disambiguate which sign belongs to which directed road element — a problem raised by [[Ian Atkinson]] on 2026-04-28 in the context of [[Sign Duplication at Junctions]].

## Usage by team

| Team | Used? | Notes |
|---|---|---|
| Speeds ([[Kenan Ozturk]], [[Tomasz Raciborowski]], [[Piotr Strzelecki]]) | Not currently | Open to exploring in future for parallel-road disambiguation |
| Map matching ([[Gaurav Shah]]) | Partially | Uses `seen_count` max value; `not_seen` not yet used |
| ML training ([[Pim Arendsen]]) | No | — |
| Guidance / Capybaras ([[Tomasz Gajewski]]) | No | Team receives pre-aggregated data from [[Localization Layer]]; sector-level data would need to be exposed by that layer |

## Related

- [[Sign Orientation]] — the companion heading-based parameter
- [[Sign-to-Road Matching]] — the matching process that could benefit from this parameter
- [[FCD Cluster API]] — API providing this data
- [[Sign Duplication at Junctions]] — problem this parameter helps address

*Source: `raw/slack/2026-05-08-sign-orientation-vs-observed-angles-for-sign-to-road-matching.md`*
