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

## Supersedes

This decision supersedes [[decisions/Default Lane Connectivity at 3-Valent T-Junctions]] (FMO violation review, May 2026), which proposed *replacing* HD connectivity with defaults at FOW 3 / DC Taper T-junctions. The newer supplement approach preserves valid HD connections and only fills gaps, which the team agreed avoids discarding correct HD-provided data.

## Related

- [[decisions/Default Lane Connectivity at 3-Valent T-Junctions]] — superseded earlier decision
- [[problems/Rule 51684 Missing Lane Connectivity at 3-Valent Junctions]]
- [[problems/Rule 51147 Missing Lane Connectivity at 3-Valent Junctions]]
- [[concepts/Lane Connectivity]]

*Source: `raw/transcripts/converted/2026-05-19 Lanes_Sprint_Planning.md`*
