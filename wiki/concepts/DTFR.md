---
type: concept
---

# DTFR (Default Turn From Rules)

DTFR refers to a set of rules in the [[Lanes]] pipeline that apply default lane connectivity and lane count when authoritative data is missing or incomplete. These rules derive turning behaviour from the surrounding road context (road class, direction, junction type) rather than relying solely on HD map data.

DTFR stories in the sprint backlog cover scenarios such as:
- Detecting and filtering lanes on non-payload roads (rule 51059)
- Providing default connectivity at 3-valid junctions when HD data is incomplete (rule 50329)
- Handling road closures in one or both directions with different vehicle restrictions (story 50329 / Route 5830)

DTFR rules generate metadata in the output JSON that identifies which rule was applied, enabling downstream [[Transaction Manager]] to create traceable transactions.

## Note on dual usage of "DTFR"

The abbreviation DTFR is used in two related but distinct senses in the Lanes codebase:

1. **Default Turn From Rules** (this page) — the derivation rules that supply default lane connectivity when authoritative data is absent.
2. **Direction of Traffic Flow for Road/Lane** — an attribute on map road elements. Rule 51059 is named "DTFR for Lane and Road not in line", meaning the traffic flow direction attribute on the lane does not match the traffic flow direction attribute on the road. See [[problems/Rule 51059 Lanes on Non-Payload Roads]] and [[problems/Rule 51085 Invalid Direction of Traffic Flow for Lane]].

*Sources: `raw/transcripts/converted/2026-05-15 Lanes_Sprint_Planning.md`, `raw/confluence/Lanes FMO-- violation review.md`*
