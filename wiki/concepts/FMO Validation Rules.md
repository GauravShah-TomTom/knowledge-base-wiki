---
type: concept
---

# FMO Validation Rules

Feature Model Operator (FMO) validation rules are automated quality checks applied to map data features to detect logical errors, inconsistencies, and constraint violations in the derived lane data.

## Overview

FMO rules are identified by numeric Rule IDs and classified by severity (Error, Warning) and priority (Critical, Normal). They are run against the output of [[Genesis]] to detect derivation errors.

## Top violations in zone DEU-01 (2026-05 analysis)

| Rule ID | Count | Description | Severity |
|---|---|---|---|
| 50329 | 37,115 | Intermediate Road Element not part of Normal Intersection | — |
| 51684 | 19,409 | Missing Lane Connectivity | — |
| 51147 | 6,659 | Missing Lane Connectivity | — |
| 51059 | 5,763 | DTFR for Lane and Road not in line | — |
| 51068 | 3,710 | Invalid Lane Connectivity | — |
| 50311 | 2,497 | Incorrect Direction of Traffic Flow for Lane | Error, Critical |
| 50263 | 2,489 | Traffic Flow Conflicting with Driving Side | Warning, Critical |
| 53161 | 2,065 | Invalid Lane Connection | Rare warning, Critical |
| 51085 | 1,382 | Invalid Direction of Traffic Flow for Lane | Rare Warning, Critical |
| 51830 | 1,232 | Incorrect relationship to Lane Connectivity | Error, Critical |

## Related

- [[Lane Connectivity]] — most frequent violation category
- [[DTFR]] — second major violation category
- [[Genesis]] — system whose output is validated
- [[Lanes FMO violations DEU-01]] — problem record for the DEU-01 run
- [[Lanes FMO]] — project

*Source: `raw/confluence/Lanes FMO-- violation review.md`*
