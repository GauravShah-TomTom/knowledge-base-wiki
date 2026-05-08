---
type: concept
---

# Sign Orientation

The estimated direction (heading/bearing) that a traffic sign face points, as recorded by a data-collection vehicle at the time of observation. Sign orientation is expressed as an absolute angle and is one of the two main parameters used in [[Sign-to-Road Matching]].

## How it is captured

[[Eagle]] probe vehicles record the heading of detected signs. The newest Eagle firmware (as of 2026-04) provides additional messages that may improve sign bearing accuracy, though decoding and assessment are still in progress ([[Ian Atkinson]] — 2026-04-28).

## Usage by team

| Team | Used? | Notes |
|---|---|---|
| Speeds ([[Kenan Ozturk]], [[Tomasz Raciborowski]], [[Piotr Strzelecki]]) | Yes | Primary parameter for sign→road road matching |
| Map matching ([[Gaurav Shah]]) | Yes | Applied with a distance/angle threshold |
| ML training ([[Pim Arendsen]]) | Not currently | — |
| Guidance / Capybaras ([[Tomasz Gajewski]]) | Yes | Receive pre-aggregated data from [[Localization Layer]] |

## Related

- [[Sign-to-Road Matching]] — matching process that consumes this parameter
- [[Seen-Sector Counts]] — complementary parameter based on observation directions
- [[Eagle]] — system that captures orientation data
- [[FCD Cluster API]] — API surface exposing `Cluster.getSeenCountsPerSector()` alongside heading

*Source: `raw/slack/2026-05-08-sign-orientation-vs-observed-angles-for-sign-to-road-matching.md`*
