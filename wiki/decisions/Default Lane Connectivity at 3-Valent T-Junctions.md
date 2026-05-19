---
type: decision
---

# Default Lane Connectivity at 3-Valent Junctions

## Decision

For any 3-valid junction (not limited to T-type / FOW 3 / DC Taper): apply whatever lane connectivity [[systems/HD Basemap|HD]] / [[systems/Cross Link|Crosslink]] provides. Where connectivity is missing or incomplete, fill the gap by defaulting all possible lane connections for that junction.

This "fill the gap" approach was clarified in the 2026-05-19 sprint planning — the strategy is to *supplement* HD data, not to ignore it entirely.

## Scope clarification (2026-05-19)

The initial framing (2026-05-15 FMO review) described only "simple T-type 3-valent junctions (FOW 3 or DC Taper)". The sprint planning on 2026-05-19 confirmed the scope is **any 3-valid junction**: "wherever we are getting connectivity from HD, we'll apply it; if anything is missing, we'll put a default connection."

[[Gaurav Shah]] noted the team will start with T-junctions and address more complex cases (dual carriageways, etc.) in follow-up stories if they arise.

## Rationale

Rules [[problems/Rule 51684 Missing Lane Connectivity at 3-Valent Junctions|51684]] and [[problems/Rule 51147 Missing Lane Connectivity at 3-Valent Junctions|51147]] together account for over 26,000 occurrences in the DEU-01 FMO run (52.94% and 39.89% of QA transactions respectively). The root causes — wrong Crosslink matching, incomplete HD data, derivation issues — are difficult to fix at the source. Defaulting missing connections is expected to be correct in roughly 90% of cases.

## Trade-offs

- Default connectivity may not be correct in all cases (estimated ~90% accuracy).
- Preserves HD-provided connectivity where it exists.

## Context

Identified during the Lanes FMO violation review of zone DEU-01 (Schleswig-Holstein); approach refined in 2026-05-19 sprint planning.

*Sources: `raw/confluence/Lanes FMO-- violation review.md`, `raw/transcripts/converted/2026-05-19 Lanes_Sprint_Planning.md`*
