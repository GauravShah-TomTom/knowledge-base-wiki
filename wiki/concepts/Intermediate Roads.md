---
type: concept
---

# Intermediate Roads

Roads that form the interior of a junction area (connector/filler segments between approach legs). In [[HD Basemap]] output, intermediate roads often lack lane count data, which causes [[Genesis]] QA to flag them as errors — particularly when a junction is very large (see [[problems/Large Junctions Missing Lane Count]]).

## Role in Rule 50329

Rule 50329 ("Intermediate Road Element not part of Normal Intersection") fires specifically when the [[Lanes]] pipeline skips populating lane information on intermediate roads inside junction areas, because [[HD Basemap]] models those junctions as large areas with trajectories instead of standard centerlines. This was the top rule by occurrence count in the DEU-01 [[FMO]] run (5,129 unique transactions, 36.4% of total).

**Proposed solutions** (see [[problems/Rule 50329 Intermediate Road Element Not Part of Normal Intersection]]):
1. Default lane count from the main road (determined by FRC/N2C).
2. Derive from parallel HD trajectories assumed to be centerlines.
3. Request [[Orbis]] to provide lane count on such road elements.

## Related

- [[problems/Rule 50329 Intermediate Road Element Not Part of Normal Intersection]]
- [[problems/Large Junctions Missing Lane Count]]
- [[systems/HD Basemap]]
- [[systems/Genesis]]
- [[concepts/FMO]]

*Sources: `raw/slack/adas-hd-basemap-lanes-general/2026-05-13 18_20_40 - reply - 2026-05-14 09_44_31.md`, `raw/confluence/Lanes FMO-- violation review.md`*
