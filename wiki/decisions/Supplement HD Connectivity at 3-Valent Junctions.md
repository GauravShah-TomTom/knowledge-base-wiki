---
type: decision
date: 2026-05-19
---

# Decision: Supplement HD Connectivity at 3-Valent Junctions (Fill Gaps)

## Context

When processing lane connectivity at 3-valid (T-junction) junctions, the pipeline can encounter junctions where HD/SDK provides partial connectivity data — some connections exist but others are missing. The question is whether to:
1. **Replace** — ignore all HD connectivity and default all possible connections (the approach in [[decisions/Default Lane Connectivity at 3-Valent T-Junctions]]).
2. **Supplement** — use whatever HD/SDK provides and fill in any missing connections with defaults.

## Decision

Use the **supplement approach**: apply connectivity from the HD/SDK data when it is present, and add default connections for any that are missing. A new sprint story will be created specifically for this work.

Acceptance criteria: all possible connections are created in the transaction for 3-valid junctions, without discarding valid HD-provided connectivity.

## Rationale

Speaker 4 noted: "The reason I would say mostly it's we are missing some connectivity either from our logic or due to HD missing it's information." Since HD may provide correct partial data, discarding it would introduce errors. The supplement approach preserves correct HD connections and fills only the gaps.

## ⚠️ CONFLICT with existing decision

> **Existing passage** (`wiki/decisions/Default Lane Connectivity at 3-Valent T-Junctions.md`): "For simple T-type 3-valent junctions (FOW 3 or DC Taper), ignore the lane connectivity proposed by HD data and by default populate all possible lane connections at such junctions."

> **New passage** (this decision, from `raw/transcripts/converted/2026-05-19 Lanes_Sprint_Planning.md`): "wherever we are getting connectivity from SD, we'll apply it OK. If anything is missing, we'll put a default connection." (Gaurav: "not ignore, but just fill the gap")

These two decisions contradict each other for cases where HD provides partial connectivity. The scope of each decision (FOW 3/DC Taper T-junctions vs "any 3 valid junctions") may overlap. Resolution: review whether the two decisions target different scenarios or whether the May 2026-05-19 discussion supersedes the earlier FMO-based decision.

## Related

- [[decisions/Default Lane Connectivity at 3-Valent T-Junctions]] — conflicting earlier decision
- [[problems/Rule 51684 Missing Lane Connectivity at 3-Valent Junctions]]
- [[problems/Rule 51147 Missing Lane Connectivity at 3-Valent Junctions]]
- [[concepts/Lane Connectivity]]

*Source: `raw/transcripts/converted/2026-05-19 Lanes_Sprint_Planning.md`*
