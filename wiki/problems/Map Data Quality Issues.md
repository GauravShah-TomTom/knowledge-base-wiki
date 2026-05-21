---
type: problem
---

# Map Data Quality Issues

*Source: raw/scans/MEDS Overview.pdf*

Map data quality issues are errors in [[UMM]] (and its upstream provider data) that cause navigation to suggest routes drivers cannot or do not follow. Left undetected, these errors degrade ETA accuracy, increase driver confusion, and reduce trip quality.

## Known error categories

| Error type | Detector | Description |
|---|---|---|
| Missing road segments | GeoCatch | Roads that exist physically but are absent from the map |
| Invalid turn restrictions | TurnPermitted | Turn restrictions in the map that are not physically enforced |
| Invalid permanent barriers | IPBP | Barrier road furniture that drivers are passing through |
| Missing one-way restrictions | OneWay | Bidirectional segments that should be one-way |
| Missing turn restrictions | TurnRestriction | Physical turn prohibitions absent from the map |
| Missing blockpassage attributes | Blocked Road | Road segments blocked in both directions with no blockpassage flag |
| Missing segments near PUDOs | SegErr | Road segments absent near popular pickup/dropoff locations |

## Mitigation

[[MEDS]] proactively detects all of the above error categories and feeds them into [[Auto-Graduation]] for automated correction via TomTom, and [[MIT Reporting]] for tracking.

## Related

- [[MEDS]] — detection and healing system
- [[Map Healing]] — the initiative addressing these issues
- [[UMM]] — the map model where errors manifest
