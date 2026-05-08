---
type: system
---

# Orbis

HD map data source system that provides lane geometry, centerlines, trajectories, and connectivity information used as input for lane derivation in the [[Lanes FMO]] pipeline.

## Role in lane derivation

- Provides HD areas, centerlines, and trajectories at junctions
- Crosslink data from Orbis is used to match and derive lane connectivity
- Known limitation: does not currently indicate the number of lanes on intermediate road elements inside junctions

## Proposed improvements

Several [[Lanes FMO violations DEU-01|FMO violations]] could be reduced by Orbis enhancements:
- Indicate lane counts on junction interior roads
- Account for maneuvers, DTFR, and geometric restrictions when generating connectivities
- Provide better lane direction category data

## Related

- [[Genesis]] — lane derivation system consuming Orbis data
- [[Lanes FMO]] — project that validates lane output against FMO rules
- [[HD Map]] — concept
- [[DTFR]] — traffic flow restriction concept

*Source: `raw/confluence/Lanes FMO-- violation review.md`*
