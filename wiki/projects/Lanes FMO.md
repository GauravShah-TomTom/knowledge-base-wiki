---
type: project
---

# Lanes FMO

Project to derive and validate HD lane map features — including lane connectivity, direction of traffic flow, and divider types — and measure quality via FMO (Feature Model Operator) validation rules.

## Overview

The project runs [[Genesis]] to derive lane-level features from [[Orbis]]/HD data, then validates the output against [[FMO Validation Rules]] to detect and fix quality issues.

## Zone coverage

Currently running on zone DEU-01 (Schleswig-Holstein, Germany) as a test/analysis zone.

## Quality analysis

See [[Lanes FMO violations DEU-01]] for the top-20 violation analysis from the DEU-01 run, including root causes and proposed solutions.

## Related

- [[Genesis]] — lane derivation system
- [[Orbis]] — upstream data source
- [[FMO Validation Rules]] — validation ruleset
- [[Lane Connectivity]] — primary derived attribute
- [[DTFR]] — traffic flow restriction attribute
- [[HD Map]] — source data concept
- [[Lanes FMO violations DEU-01]] — problem record

*Source: `raw/confluence/Lanes FMO-- violation review.md`*
