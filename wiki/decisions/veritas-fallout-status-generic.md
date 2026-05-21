---
type: decision
date: 2026-05-12
participants: [Aditya Krishna, Sunil Jaiswal, Souvik Mudi]
---

# Decision: Use Generic Fallout Status for CoreDB Lookup Failures in Veritas

## Context

[[Veritas]] needs to set an explicit status for leads that are currently skipped silently when a road ID or maneuver ID is not found in [[CoreDB]] (see [[problems/Veritas Silent Lead Skipping]]). The team discussed whether to introduce one status per failure type or a single generic status.

## Options considered

1. **Per-exception status** — e.g., "road ID missing", "maneuver ID missing", separate statuses for each CoreDB exception type
2. **Generic "fallout missing feature" status** — a single status for any CoreDB feature lookup failure

## Decision

Use a **generic "fallout missing feature"** status to cover all CoreDB lookup failures (missing road ID, missing maneuver ID, and similar). A separate "not verified" status continues to be used for runtime/processing exceptions.

## Rationale

- [[Aditya Krishna]] judged that propagating the CoreDB exception type (e.g., "4DB exception") in the verification result is sufficient for downstream handling — individual exception descriptions are not necessary
- [[Sunil Jaiswal]] agreed: "generic status should be sufficient"
- The fallout reason detail (which specific feature was missing) was discussed but deemed lower priority; sending it was deferred or removed from scope for now

*Source: `raw/notes/Sprint grooming_ Quality improvement - PC restrictions.docx` — sprint grooming meeting 2026-05-12*
