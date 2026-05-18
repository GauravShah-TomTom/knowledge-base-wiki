---
type: decision
---

# Skip Rule 52261 from Lanes Project Scope

## Decision

Rule 52261 ("Carriageways too close based upon number of lanes") is a candidate for removal from the [[projects/Lanes|Lanes project]] scope — no pipeline action is required.

## Rationale

Rule 52261 is a geometric validation rule that fires when carriageway spacing is narrower than expected for the number of lanes. This is not dependent on the derivation pipeline or HD data quality; it reflects actual road geometry. The [[Lanes Automator]] cannot improve this, and attempting to do so would introduce incorrect data.

## Context

Identified during the Lanes FMO violation review of zone DEU-01. The rule had 335 occurrences in that run.

## Related

- [[problems/Rule 52261 Carriageways Too Close Based on Number of Lanes]]

*Source: `raw/confluence/Lanes FMO-- violation review.md`*
