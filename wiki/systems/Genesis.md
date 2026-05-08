---
type: system
---

# Genesis

Lane derivation system that processes [[HD Map|HD]] and [[Orbis]] source data to generate lane-level map features, including lane connectivity, direction of traffic flow, and divider types.

## Context

Genesis is responsible for building and maintaining lane data in the [[Core DB]]-adjacent pipeline. Its output is validated against [[FMO Validation Rules]] to detect errors in derived lane features.

## Known issues

Multiple FMO violations (see [[Lanes FMO violations DEU-01]]) are attributable to Genesis derivation logic, including:
- Incorrect lane connectivity at 3-valent junctions (rules 51684, 51147)
- Incorrect DTFR on lanes vs roads (rules 51059, 51085)
- Haphazard lane connectivity at complex junctions (rule 51830)
- Z-level sequencing errors in lane connectivity (rule 52124)

## Related

- [[Orbis]] — upstream data source
- [[Lanes FMO]] — project validating Genesis output
- [[HD Map]] — source data concept
- [[Lane Connectivity]] — key derived attribute

*Source: `raw/confluence/Lanes FMO-- violation review.md`*
