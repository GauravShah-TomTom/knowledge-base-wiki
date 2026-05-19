---
type: decision
contradiction: true
---

# Default Lane Connectivity at 3-Valent T-Junctions

⚠️ CONFLICT

> **This passage** (from `raw/confluence/Lanes FMO-- violation review.md`): "ignore the lane connectivity proposed by HD data and by default populate all possible lane connections at such junctions."

> **Conflicting passage** (from `raw/transcripts/converted/2026-05-19 Lanes_Sprint_Planning.md`): "wherever we are getting connectivity from SD, we'll apply it. If anything is missing, we'll put a default connection." (Gaurav Shah: "not ignore, but just fill the gap")

These two passages describe different approaches to HD data at 3-valent junctions. The 2026-05-19 sprint planning decision to supplement rather than replace HD connectivity may supersede this earlier FMO-derived decision. See [[decisions/Supplement HD Connectivity at 3-Valent Junctions]] for the newer decision.

## Decision

For simple T-type 3-valent junctions (FOW 3 or DC Taper), ignore the lane connectivity proposed by [[systems/HD Basemap|HD]] data and by default populate all possible lane connections at such junctions.

## Rationale

Rules [[problems/Rule 51684 Missing Lane Connectivity at 3-Valent Junctions|51684]] and [[problems/Rule 51147 Missing Lane Connectivity at 3-Valent Junctions|51147]] together account for over 26,000 occurrences in the DEU-01 FMO run (52.94% and 39.89% of QA transactions respectively). The root causes — wrong Crosslink matching, incomplete HD data, derivation issues — are difficult to fix at the source. Defaulting all connections is expected to be correct in roughly 90% of cases.

## Trade-offs

- Connectivity may not be correct in all cases (estimated ~90% accuracy).
- Bypasses HD-provided connectivity which is sometimes correct.

## Context

Identified during the Lanes FMO violation review of zone DEU-01 (Schleswig-Holstein).

*Sources: `raw/confluence/Lanes FMO-- violation review.md`, `raw/transcripts/converted/2026-05-19 Lanes_Sprint_Planning.md`*
