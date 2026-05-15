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

*Source: `raw/transcripts/converted/2026-05-15 Lanes_Sprint_Planning.md`*
