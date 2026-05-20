---
type: system
---

# Uber ACI Service

The Uber ACI (Access Control Interface) Service is an external Uber API that submits PC restriction leads to the organisation's workflow for verification. Also referenced as "Uber SEI status service" in meeting transcripts.

## Role

- Uber ACI sends restriction leads (e.g. maneuver type restrictions: can-left, no-left) to [[Camunda]] for processing.
- After [[Veritas]] verifies the leads, status updates flow back through the [[Camunda]] workflow.

## Integration

An existing Uber restriction rate project in [[Camunda]] production handles Uber leads specifically.

## Related

- [[Veritas]]
- [[Camunda]]
- [[Veritas Uber ACI Flow Integration]]
