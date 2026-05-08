---
type: concept
---

# Sign-to-Road Matching

The process of associating a detected traffic sign with a specific directed road element in the map. Correct matching is necessary for deriving lane-level or road-level attributes (e.g. speed limits, turn restrictions) from sign observations.

## Key parameters

Two parameters are available for matching:

1. **[[Sign Orientation]]** — the estimated heading of the sign face (absolute angle). Used as the primary parameter by most teams.
2. **[[Seen-Sector Counts]]** — counts of observations grouped by angular sector, indicating from which directions a sign has been seen. Used less widely but has potential for resolving ambiguous cases (e.g. parallel roads, slip roads).

## Challenges

- Signs at junctions can be seen from multiple directions, causing **[[Sign Duplication at Junctions]]**.
- Signs on near-parallel roads (e.g. slip roads) may have similar orientations, making heading alone insufficient for disambiguation.

## Team approaches (as of 2026-04-30)

| Team | Heading | Seen-sector counts |
|---|---|---|
| Speeds | Primary matching parameter | Not used |
| Map matching ([[Gaurav Shah]]) | Threshold-based | `seen_count` max used |
| Guidance / Capybaras ([[Tomasz Gajewski]]) | Used | Not used (pre-aggregated data from [[Localization Layer]]) |
| ML training ([[Pim Arendsen]]) | — | Not used |

## Related

- [[Sign Orientation]] — heading-based parameter
- [[Seen-Sector Counts]] — observation-direction parameter
- [[FCD Cluster API]] — exposes both parameters
- [[Eagle]] — probe vehicle system that captures raw observations

*Source: `raw/slack/2026-05-08-sign-orientation-vs-observed-angles-for-sign-to-road-matching.md`*
