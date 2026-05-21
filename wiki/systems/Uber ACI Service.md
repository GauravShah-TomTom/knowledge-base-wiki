---
type: system
---

# Uber ACI Service

The Uber ACI (Automatic Change Identification) Service is an external Uber API that provides maneuver restriction data (turn restrictions such as "can left" / "no left") for map quality verification.

## Role

- Sends restriction leads to the organisation's pipeline via the [[projects/Uber ACI Flow]]
- Leads flow through [[BFrost]] → [[Veritas]] → [[Camunda]] for verification and task management
- There is a dedicated production project configured specifically for Uber restriction leads (separate from other sources)
- The Uber ACI Service also exposes an "Uber SEI status service" endpoint used for pushing test data during dev testing

*Source: `raw/notes/Sprint grooming_ Quality improvement - PC restrictions.docx` — sprint grooming meeting 2026-05-12*
