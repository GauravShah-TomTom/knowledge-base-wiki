---
type: problem
---

# Lanes FMO Violations — DEU-01

Analysis of top FMO validation violations found when running [[Lanes FMO]] on zone DEU-01 (Schleswig-Holstein, Germany).

## Top violations summary

| Rule ID | Count | Root cause category |
|---|---|---|
| 50329 | 37,115 | Missing lanes on intermediate road elements in junction areas |
| 51684 | 19,409 | Missing Lane Connectivity at 3-valent junctions |
| 51147 | 6,659 | Missing Lane Connectivity at 3-valent junctions |
| 51059 | 5,763 | DTFR mismatch between lanes and roads |
| 51068 | 3,710 | Invalid Lane Connectivity (ignoring existing restrictions) |
| 50311 | 2,497 | Incorrect traffic flow direction for connected lanes |
| 50263 | 2,489 | Traffic flow conflicts with country driving side |
| 53161 | 2,065 | Crossing lane connectivities at junctions |
| 51085 | 1,382 | Invalid DTFR on lanes |
| 51830 | 1,232 | Haphazard/incorrect lane connectivity |

## Key root causes

1. **Junction interior roads lacking lanes (50329)**: HD provides trajectories instead of centerlines; [[Genesis]] skips lane population on these roads
2. **Missing connectivity at 3-valent junctions (51684, 51147)**: Crosslink matching failures or incomplete HD data; proposed fix: default to all-possible connections at simple T-junctions
3. **DTFR mismatch (51059, 51085)**: HD does not carry vehicle-type restrictions at lane level; [[Genesis]] does not copy road restrictions to lanes
4. **Invalid connectivity due to existing restrictions (51068)**: [[Orbis]] generates connectivities ignoring maneuvers/DTFR/GR

## Proposed solutions

- Rule 50329: Default lanes on junction interior roads to same count as main road, or request [[Orbis]] improvement
- Rules 51684, 51147: Ignore HD connectivity for simple 3-valent junctions; populate all possible connections
- Rules 51059, 51085: Modify lane DTFR to match road restrictions
- Rule 51068: Ask [[Orbis]] to consider restrictions when generating connectivities
- Rule 52261: Proposed to be skipped (carriageways-too-close rule, not derivation-dependent)

## Related

- [[FMO Validation Rules]] — full rule catalogue
- [[Lane Connectivity]] — most violated concept
- [[DTFR]] — second major violation area
- [[Genesis]] — system generating the violating output
- [[Orbis]] — upstream data source
- [[Lanes FMO]] — project

*Source: `raw/confluence/Lanes FMO-- violation review.md`*
