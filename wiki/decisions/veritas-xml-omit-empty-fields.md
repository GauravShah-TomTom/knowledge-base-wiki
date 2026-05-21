---
type: decision
date: 2026-05-12
participants: [Aditya Krishna, Sunil Jaiswal]
---

# Decision: Omit Empty Fields from Veritas XML Metadata Output

## Context

[[Veritas]] emits XML with transition metadata. Story 5952 originally planned to add an `external_id` field to the [[Veritas]] model to facilitate [[Camunda]] task closure. Testing revealed that an empty `external_id` tag generates invalid XML (see [[problems/Veritas Empty XML Tag Invalid Output]]).

## Decision

1. **Do not emit empty XML tags** — modify the XML metadata generator to skip any field that has no value
2. **Reassess external ID necessity** — [[Sunil Jaiswal]] will check whether the Camunda task ID can be used directly as a restriction ID to close tasks, making the `external_id` field unnecessary. If it works, story 5952 (add external ID to Veritas model) can be closed without adding the field

## Rationale

- Empty tags were found to cause downstream XML validation failures
- Using the existing task ID as the closure identifier avoids introducing a new model field entirely

*Source: `raw/notes/Sprint grooming_ Quality improvement - PC restrictions.docx` — sprint grooming meeting 2026-05-12*
