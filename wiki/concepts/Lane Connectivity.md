---
type: concept
---

# Lane Connectivity

A map data attribute that describes which lane on one road element connects to which lane on an adjacent road element, particularly at junctions. A core feature of HD lane maps.

## Key rules

- A "from" lane must have traffic flow **towards** the junction
- A "to" lane must have traffic flow **away from** the junction
- Connected lanes departing from the same road element must not cross each other
- Lane connectivity must respect lane direction categories (e.g., "Only Left" must connect only to left-turn lanes)

## Common FMO violations related to lane connectivity

| Rule ID | Description |
|---|---|
| 51684 / 51147 | Missing Lane Connectivity — especially at 3-valent junctions |
| 51068 | Invalid Lane Connectivity — connectivity populated despite restrictions (BP, DTFR, maneuvers, GR) |
| 50311 | Incorrect Direction of Traffic Flow for connected lanes |
| 53161 | Invalid Lane Connection — connected lanes cross each other |
| 51830 | Incorrect relationship to Lane Connectivity (haphazard connectivity) |
| 52379 | Incorrect Lane Connectivity Relationship — connectivity to non-existent lanes |
| 51062 | Incorrect Lane Connection |
| 52124 | Incorrect Z-Levels for Lane Connectivity |
| 53887 | Lane Connectivity conflicts with Lane Direction Category |

## Related

- [[DTFR]] — traffic flow restriction affecting lane connectivity validity
- [[FMO Validation Rules]] — validation rules that check connectivity
- [[Genesis]] — system that derives lane connectivity
- [[Orbis]] — upstream data source for connectivity

*Source: `raw/confluence/Lanes FMO-- violation review.md`*
