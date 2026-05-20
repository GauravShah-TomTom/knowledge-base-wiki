---
type: system
---

# Veritas

Veritas is the internal verification pipeline for PC (physical constraint) restrictions. It consumes leads from a Camunda task queue, verifies them against [[CoreDB]] road and maneuver data, and outputs a verification result status that drives downstream [[Camunda]] workflow routing.

## Purpose

Veritas processes maneuver-type restriction leads (e.g. "can-left", "no-left") submitted via the [[Uber ACI Service]] integration. For each lead it:

1. Looks up road IDs and maneuver IDs in [[CoreDB]].
2. Runs the verification logic (SDO and LLM-based implicit/restriction checks).
3. Sets a `verification_result` status on the lead.
4. Outputs a Veritas result record consumed by the [[Camunda]] BPMN/DMN routing scripts.

## Veritas Status Values

| Status | Meaning |
|---|---|
| `VERIFIED` | Lead passed verification |
| `NOT_VERIFIED` | Lead failed verification (runtime exception path) |
| `FALLOUT_MISSING_FEATURE` | Lead skipped — road ID or maneuver ID not found in [[CoreDB]] |

As of May 2026, a new `FALLOUT_MISSING_FEATURE` status (or similarly named generic status) is being introduced to replace the previous silent-skip behaviour. See [[Veritas silently skipping leads]] and [[Use generic CoreDB exception status for Veritas fallouts]].

## Output Format

Veritas produces an XML output (transition metadata) consumed by [[Camunda]]. Each field included in the XML must have a non-empty value; empty fields cause invalid XML and runtime failures. See [[Guard Veritas XML against empty transition metadata fields]].

## Integration with BFrost

[[BFrost]] runs on Thursdays to mark leads as non-overlapping. Only after BFrost completes are leads picked up by Veritas. The Veritas Airflow workflow is triggered manually at first, then scheduled to run Mondays. See [[Veritas Uber ACI Flow Integration]].

## Related

- [[CoreDB]]
- [[Camunda]]
- [[BFrost]]
- [[Airflow]]
- [[Uber ACI Service]]
- [[Veritas Uber ACI Flow Integration]]
- [[Veritas silently skipping leads]]
