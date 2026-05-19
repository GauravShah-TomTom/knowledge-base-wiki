---
type: problem
status: open
---

# Rule 51147 — Missing Lane Connectivity at 3-Valent Junctions

## Summary

Rule 51147 fires when lane connectivity is missing at a 3-valent junction (T-junction). Shares root cause and proposed solution with [[problems/Rule 51684 Missing Lane Connectivity at 3-Valent Junctions|Rule 51684]]; the two rules capture the same failure mode under slightly different conditions.

- **Count in DEU-01 FMO run**: 6,659 occurrences; affected 5,606 unique transactions (39.89% of all QA transactions).
- **Example transactions**: `5ce352da-eb60-482d-9a3e-3e570842f16e` (54.7182322, 9.6674309), plus additional cases: `abb810b3-3352-495b-9949-57fa8cb8377e`, `041ee72e-c650-4938-a662-5f2d4de866bf` (no lane populated on side roads).

## Root Causes

1. Wrong matching of [[Cross Link|Crosslink]] data.
2. [[HD Basemap|HD]] data being incomplete.
3. Derivation issue in [[Lanes Automator]].

## Proposed Solution

Use whatever HD/SDK provides and fill in any missing connections with defaults — the **supplement** approach agreed in the 2026-05-19 sprint planning. A new sprint story is being created to implement this. See [[decisions/Supplement HD Connectivity at 3-Valent Junctions]].

This supersedes the earlier "replace" approach from the FMO review ([[decisions/Default Lane Connectivity at 3-Valent T-Junctions]]).

## Related

- [[problems/Rule 51684 Missing Lane Connectivity at 3-Valent Junctions]] — identical root cause; different rule ID
- [[concepts/Lane Connectivity]]
- [[systems/Cross Link]]
- [[decisions/Supplement HD Connectivity at 3-Valent Junctions]]

*Sources: `raw/confluence/Lanes FMO-- violation review.md`, `raw/transcripts/converted/2026-05-19 Lanes_Sprint_Planning.md`*
