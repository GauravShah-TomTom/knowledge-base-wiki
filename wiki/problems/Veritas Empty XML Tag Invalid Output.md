---
type: problem
---

# Veritas Empty XML Tag Invalid Output

[[Veritas]] generates XML output containing transition metadata fields. When the `external_id` field (or any metadata field) has no value, Veritas emits an empty XML tag for it. This produces invalid XML that causes downstream failures.

## Observed behaviour

Story 5952 (add external ID field to Veritas model) revealed the issue: testing an empty `external_id` tag directly resulted in a failure — "invalid XML".

## Resolution (story 5952)

Add a guard in the XML metadata generation code: if a metadata field has no value, omit it entirely from the XML output rather than emitting an empty tag.

See [[decisions/veritas-xml-omit-empty-fields]].

*Source: `raw/notes/Sprint grooming_ Quality improvement - PC restrictions.docx` — sprint grooming meeting 2026-05-12*
