---
type: system
---

# Eagle

TomTom's probe vehicle firmware/platform used for roadway data collection. Eagle vehicles observe traffic signs, road geometry, and other map features by driving instrumented vehicles.

## Sign data collection

Eagle records sign orientations (headings) and observation angles as vehicles pass signs. The newest Eagle firmware (as of 2026-04) includes additional messages that may improve sign bearing accuracy — decoding and assessment are ongoing ([[Ian Atkinson]]).

## Related

- [[Sign Orientation]] — sign heading data captured by Eagle vehicles
- [[Seen-Sector Counts]] — sector-observation data captured by Eagle
- [[FCD Cluster API]] — API that exposes aggregated Eagle observations
- [[Sign-to-Road Matching]] — downstream use of Eagle-captured data

*Source: `raw/slack/2026-05-08-sign-orientation-vs-observed-angles-for-sign-to-road-matching.md`*
