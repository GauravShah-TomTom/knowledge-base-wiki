---
type: problem
status: open
---

# Missing Country Driving Direction in Derivation

## Summary

The [[Lanes Automator]] post-processing task (Route 5832) requires knowing the country driving direction (left-hand traffic vs right-hand traffic) to correctly apply lane rules. This information is not yet available in the derivation pipeline.

## Workaround

[[Gaurav Shah]] added a property in application configuration (`application.properties`) as a placeholder, operating under the assumption that the value will be populated from an upstream source. A separate task will be created to wire up the actual upstream population of this property.

## Status

Not a current blocker for Route 5832 implementation, but must be resolved before the rule can be applied correctly in production.

*Source: `raw/transcripts/converted/2026-05-15 Lanes_Sprint_Planning.md`*
