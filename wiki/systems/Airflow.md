---
type: system
---

# Airflow

Apache Airflow is the workflow orchestration platform used to schedule and execute the [[projects/Uber ACI Flow]] pipeline.

## Usage in Uber ACI Flow

- Uses the **HTTP operator** for polling results and calling the Dumbo/[[Dumbo]] execution service
- HTTP connections and Airflow variables are configured per environment (dev vs. production)
- Production scheduling: Veritas for Uber ACI will initially be triggered **manually** after deployment; once the timing relative to [[BFrost]] (Thursday run) is understood, it will be scheduled for **Mondays**
- Environment-specific topic names and other settings are stored as Airflow variables

## Environment differences

| Setting | Dev | Production |
|---|---|---|
| Topic names | Dry-run prefix | No prefix |
| Trigger | Manual | Monday schedule (planned) |
| Variables/connections | Dev values | Must be added for prod |

*Source: `raw/notes/Sprint grooming_ Quality improvement - PC restrictions.docx` — sprint grooming meeting 2026-05-12*
