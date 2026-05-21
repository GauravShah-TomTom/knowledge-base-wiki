---
type: concept
---

# Map Healing

*Source: raw/scans/MEDS Overview.pdf*

Map Healing is the practice and initiative at Uber of proactively detecting, classifying, and fixing errors in map data before they degrade navigation and routing quality for riders and drivers. It is the overarching goal that [[MEDS]] (Map Error Detection System) was built to achieve.

## Problem

Map data providers (e.g., TomTom) inevitably contain errors: missing roads, incorrect turn restrictions, wrong one-way designations, phantom barriers, and missing segments near pickup/dropoff points. These errors cause navigation to suggest routes that drivers cannot or do not follow, degrading ETA accuracy and trip quality.

## Approach

1. **Detect** — use real driver behaviour (GPS traces, traversal patterns) to identify divergences from the map model ([[UMM]]).
2. **Classify** — route divergence signals through specialized detectors (GeoCatch, TurnPermitted, IPBP, OneWay, TurnRestriction, Blocked Road, SegErr) to determine the type of map error.
3. **Fix** — apply corrections automatically via [[Auto-Graduation]] or through the [[MIT Reporting]] pipeline for human review.

## Related

- [[MEDS]] — the system implementing map healing
- [[Auto-Graduation]] — automated fix application pipeline
- [[Route Divergence]] — primary detection signal
