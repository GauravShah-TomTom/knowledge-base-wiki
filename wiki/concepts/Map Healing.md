---
type: concept
---

# Map Healing

Map Healing is the discipline of automatically detecting, classifying, and correcting errors in map data using real-world driver behaviour as a signal. Rather than relying solely on manual cartographic review, map healing systems observe where drivers deviate from navigation suggestions and infer what map data is wrong.

At Uber, the primary map healing system is [[MEDS]] (Map Error Detection System). Corrections discovered by MEDS are automatically graduated to the [[TomTom]] pipeline via [[Auto-Graduation]].

## Why It Matters

Map errors cause navigation to suggest incorrect routes, leading to driver confusion, longer trips, and poor ride experience. Because the road network is large and constantly changing, manual QA alone cannot maintain quality at scale. Map healing closes the feedback loop from real trips back to the map.

## Key Signal: Route Divergence

The core signal is the [[Route Divergence]] — when a driver's actual path diverges from the suggested route. Aggregated across many trips, divergences reveal systematic map errors rather than individual driver choices.

## Related

- [[MEDS]] — Uber's map healing platform
- [[Route Divergence]] — primary input signal
- [[Auto-Graduation]] — automated pathway from detection to map fix
- [[UMM]] — the map model that is corrected
- [[TomTom]] — external provider that applies the fixes

*Source: `raw/scans/MEDS Overview.pdf`*
