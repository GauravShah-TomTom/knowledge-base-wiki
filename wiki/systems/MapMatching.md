---
type: system
stub: true
---

# MapMatching

MapMatching is a service that takes raw GPS driver traces and matches them to road segments in the map network. It is an upstream step in the [[MEDS]] [[Route Divergence]] pipeline.

*Source: raw/scans/MEDS Overview.pdf*

## Pipeline Position

Raw Driver Traces → **MapMatching** → [[PTMMT]] → Divergence Calculator

## Related

- [[MEDS]] — consumes MapMatching output
- [[PTMMT]] — downstream component
- [[Route Divergence]] — signal produced downstream
