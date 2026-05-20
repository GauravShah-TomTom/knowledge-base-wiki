---
type: decision
date: 2026-05-12
deciders: [Aditya Krishna, Sunil Jaiswal]
---

# Guard Veritas XML against empty transition metadata fields

**Decision:** Add a guard in the [[Veritas]] XML generator so that fields with no value are omitted from the transition metadata XML output rather than emitted as empty tags.

## Context

During sprint grooming on 2026-05-12, [[Sunil Jaiswal]] noted that the XML generator currently emits empty tags for fields with no value (specifically the `externalId` field). This results in invalid XML and causes the downstream [[Camunda]] workflow to fail.

## Rationale

The XML consumer requires all included fields to have a non-empty value. Emitting an empty tag is invalid and causes a hard failure. The fix is to simply skip the field if its value is not present.

## Implementation

- Add a null/empty check in the XML metadata generator for each optional field.
- If the value is absent or empty, do not include the field in the transition metadata XML.
- Specifically relevant to the `externalId` / external ID field (story 5952).

## Related

- [[Veritas]]
- [[Empty external ID causes invalid XML in Veritas]]
- [[Use task ID as restriction ID instead of external ID in Veritas]]
