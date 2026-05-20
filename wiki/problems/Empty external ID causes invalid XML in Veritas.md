---
type: problem
status: in-progress
---

# Empty external ID causes invalid XML in Veritas

When [[Veritas]] generates the transition metadata XML for [[Camunda]], it emits an empty `<externalId>` tag if no external ID value is set. This results in invalid XML and causes the Camunda workflow to fail.

## Impact

- Any Veritas lead that has no external ID value will generate invalid XML.
- This was discovered during testing of story 5952 (add external ID to Veritas model).

## Root Cause

The XML generator includes all configured metadata fields unconditionally, even when their values are empty.

## Resolution

- Add a null/empty check in the XML metadata builder: if a field value is absent or empty, omit the tag entirely. See [[Guard Veritas XML against empty transition metadata fields]].
- Additionally, evaluate whether the `externalId` field is even needed if the task ID can serve as the restriction ID. See [[Use task ID as restriction ID instead of external ID in Veritas]].

## Related

- [[Veritas]]
- [[Camunda]]
- [[Guard Veritas XML against empty transition metadata fields]]
- [[Use task ID as restriction ID instead of external ID in Veritas]]
