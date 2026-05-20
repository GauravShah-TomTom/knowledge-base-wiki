---
type: system
---

# Airflow

Apache Airflow is the workflow scheduler used to orchestrate the [[Veritas]] processing pipeline for the [[Veritas Uber ACI Flow Integration]].

## Usage in Veritas Pipeline

- An Airflow DAG triggers [[Veritas]] to consume leads from [[Camunda]] after [[BFrost]] completes.
- The DAG was first deployed to a dry-run (dev) environment.
- For production, Airflow variables and HTTP connections configured in dev must be replicated to the production environment.

## Configuration

| Config type | Notes |
|---|---|
| HTTP connections | Used for polling result and for Dumbo execution (Docker image) |
| Variables | Environment-specific (topic names differ between dry-run and production) |

## Schedule

- Initially run **manually** after production deployment to validate the first few runs.
- Planned schedule: **Mondays** (to process BFrost output from Thursday runs).

## Related

- [[Veritas]]
- [[BFrost]]
- [[Veritas Uber ACI Flow Integration]]
