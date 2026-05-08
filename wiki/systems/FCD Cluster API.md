---
type: system
---

# FCD Cluster API

Java API within TomTom's Floating Car Data (FCD) library that exposes aggregated sign cluster properties to downstream consumers. Part of the `com.tomtom.trace.fcd.event` package.

## Key methods

- `Cluster.getSeenCountsPerSector()` — returns per-sector observation counts (how many times a sign was seen from each angular bucket).
- Complementary not-seen-count equivalent also available (name not specified in source).

Javadoc hosted at GitHub Pages (internal/preview): `sturdy-disco-gq7vvz1.pages.github.io`

## Visualisation

The seen/not-seen sector data can be visualised in [[WMS]] (green = "seen", red = "not seen") at the FCD test-demo WMS endpoint.

## Related

- [[Seen-Sector Counts]] — the concept this API exposes
- [[Sign Orientation]] — companion data also available through FCD
- [[Eagle]] — upstream data source
- [[WMS]] — visualisation tool for FCD data

*Source: `raw/slack/2026-05-08-sign-orientation-vs-observed-angles-for-sign-to-road-matching.md`*
