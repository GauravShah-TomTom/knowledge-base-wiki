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

Use whatever HD/SDK provides and fill in any missing connections with defaults — the **supplement** approach agreed in the 2026-05-19 sprint planning. A new sprint story is being created to implement this. See [[decisions/Supplement HD Connectivity at 3-Valent Junctions]].

This supersedes the earlier "replace" approach from the FMO review ([[decisions/Default Lane Connectivity at 3-Valent T-Junctions]]).

Testing plan: replicate 4–5 affected transactions in dev, then full zone test on test branch.

## Related

- [[problems/Rule 51147 Missing Lane Connectivity at 3-Valent Junctions]] — identical root cause; different rule ID
- [[concepts/Lane Connectivity]] — connectivity derivation rules
- [[systems/Cross Link]] — Crosslink data matching
- [[systems/HD Basemap]] — source data
- [[decisions/Supplement HD Connectivity at 3-Valent Junctions]]

*Sources: `raw/confluence/Lanes FMO-- violation review.md`, `raw/transcripts/converted/2026-05-19 Lanes_Sprint_Planning.md`*
