---
type: concept
---

# DTFR (Direction of Traffic Flow for Road/Lane)

A map attribute that encodes the permitted direction(s) of vehicle travel on a road element or lane. Lane-level DTFR should match or be constrained by the road-level DTFR.

## Rules

- If a road has a traffic restriction (e.g., closed for medium trucks), its lanes should carry the same restriction — but HD data often shows every lane as open for all vehicles
- A bidirectional road with only one lane populated must use a bidirectional DTFR rather than a unidirectional one
- DTFR on lanes must align with the country's driving-side convention

## FMO violations related to DTFR

| Rule ID | Description |
|---|---|
| 51059 | DTFR for Lane and Road not in line |
| 51085 | Invalid Direction of Traffic Flow for Lane |
| 50263 | Traffic Flow Conflicting with Driving Side |

## Related

- [[Lane Connectivity]] — connectivity validity depends on DTFR
- [[FMO Validation Rules]] — validation rules
- [[Genesis]] — system that should copy road DTFR to lanes

*Source: `raw/confluence/Lanes FMO-- violation review.md`*
