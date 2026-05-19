---
type: problem
status: open
---

# Rule 51684 — Missing Lane Connectivity at 3-Valent Junctions

## Summary

Rule 51684 fires when lane connectivity is absent at a 3-valent junction (T-junction). The pipeline is unable to create or generate connectivity at these junctions, causing violations.

- **Count in DEU-01 FMO run**: 19,409 occurrences; affected 7,440 unique transactions (52.94% of all QA transactions — highest percentage among all rules).
- **Example transaction**: `2ace5197-acb6-4032-81c0-0055aadeda5f` at 54.3737787, 9.3199749.

## Root Causes

1. Wrong matching of [[Cross Link|Crosslink]] data.
2. [[HD Basemap|HD]] data itself being incomplete.
3. Derivation issue in [[Lanes Automator]].

## Proposed Solution

For any 3-valid junction: apply HD connectivity where it is present; default all possible connections where it is missing or incomplete. Scope confirmed in 2026-05-19 sprint planning to cover any 3-valid junction, not just FOW 3 / DC Taper T-types.

See [[decisions/Default Lane Connectivity at 3-Valent T-Junctions]] for the decision record.

## Related

- [[problems/Rule 51147 Missing Lane Connectivity at 3-Valent Junctions]] — identical root cause; different rule ID
- [[concepts/Lane Connectivity]] — connectivity derivation rules
- [[systems/Cross Link]] — Crosslink data matching
- [[systems/HD Basemap]] — source data

*Sources: `raw/confluence/Lanes FMO-- violation review.md`, `raw/transcripts/converted/2026-05-19 Lanes_Sprint_Planning.md`*
