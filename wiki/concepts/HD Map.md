---
type: concept
---

# HD Map (High-Definition Map)

A highly detailed digital map that includes lane-level geometry, connectivity, and attributes — beyond the road-level detail of standard navigation maps. HD maps are used for advanced driver assistance systems (ADAS) and autonomous driving.

## Relevance in lane derivation

HD map data (from [[Orbis]]) provides:
- Lane centerlines and trajectories at junctions
- HD areas delineating junction boundaries
- Source lane connectivity information (Crosslink data)

## Limitations of source HD data

- Does not capture lane-level traffic restrictions (DTFR mismatches with road level)
- Incomplete lane connectivity at some junction types (3-valent junctions)
- Trajectories present instead of centerlines on some road elements inside junction areas

## Related

- [[Orbis]] — HD data provider
- [[Genesis]] — system consuming HD data
- [[Lane Connectivity]] — key derived attribute
- [[DTFR]] — traffic flow restriction concept

*Source: `raw/confluence/Lanes FMO-- violation review.md`*
