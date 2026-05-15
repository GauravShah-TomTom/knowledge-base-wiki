---
type: decision
date: 2026-05-15
---

# Decision: Create Spike for Rule 51068 Before Implementing

## Context

Rule 51068 (invalid lane connectivity) involves many conflicting scenarios where [[Genesis]] and [[Orbis]] provide different lane data. The team did not know the full set of scenarios at sprint planning time, and the scenarios were described as complex with many edge cases.

## Decision

Rather than immediately implementing a fix, create a **spike story** assigned to Niranjan to analyse the different scenarios in which rule 51068 fires. The acceptance criteria for the spike is that all scenarios are documented and captured in Confluence. Implementation stories will be groomed after the spike is complete.

## Rationale

Implementing without understanding the scenario space would likely produce an incomplete or incorrect fix. The spike approach defers implementation cost until the problem is well-understood.

*Source: `raw/transcripts/converted/2026-05-15 Lanes_Sprint_Planning.md`*
