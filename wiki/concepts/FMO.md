---
type: concept
---

# FMO (Feature Model Output / Quality Run)

FMO refers to a quality validation run performed on a geographic zone in the [[projects/Lanes|Lanes]] pipeline. An FMO run executes a set of validation rules against the derived lane data for a specific zone and reports violations per rule ID.

## Usage in Lanes

FMO runs are used to identify and prioritise quality issues before a zone's output is published. Results are analysed rule-by-rule to determine root causes and proposed solutions.

**Example**: The DEU-01 FMO run on zone DEU-01 (Schleswig-Holstein) identified 14,055 transactions with QA violations across 20 top rules.

## Key rules observed in DEU-01 FMO run

| Rule ID | Description | Unique Txns | % of Total |
|---|---|---|---|
| 51684 | Missing Lane Connectivity | 7,440 | 52.94% |
| 51147 | Missing Lane Connectivity | 5,606 | 39.89% |
| 50329 | Intermediate Road Element not part of Normal Intersection | 5,129 | 36.4% |
| 51059 | DTFR for Lane and Road not in line | 3,346 | 23.8% |
| 51068 | Invalid Lane Connectivity | 2,097 | 14.91% |

See individual [[problems/]] pages for each rule.

## Related

- [[projects/Lanes]] — pipeline on which FMO runs are executed
- [[systems/Genesis]] — QA system
- [[concepts/Lane Connectivity]] — key concept validated by FMO rules

*Source: `raw/confluence/Lanes FMO-- violation review.md`*
