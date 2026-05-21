---
type: index
date: 2026-05-21 08:24:06
---
# Systems - index
[[wiki/index|← Index]]

Our products, platforms, and services.

- [[wiki/systems/Airflow|Airflow]] — Apache Airflow is the workflow orchestration platform used to schedule and execute the [[projects/Uber ACI Flow]] pipeline.
- [[wiki/systems/BFrost|BFrost]] — BFrost is an upstream process in the [[projects/Uber ACI Flow]] pipeline that runs on a **Thursday schedule**.
- [[wiki/systems/Camunda|Camunda]] — Camunda is the BPMN workflow engine used to manage restriction-change tasks in the Uber ACI pipeline.
- [[wiki/systems/CoreDB|CoreDB]] — CoreDB is the core map database that stores road IDs and maneuver IDs used during restriction verification.
- [[wiki/systems/Dumbo|Dumbo]] — Dumbo is a job execution service used in the [[projects/Uber ACI Flow]] pipeline, invoked from [[Airflow]] via a Docker image.
- [[wiki/systems/MEDS|MEDS — Map Error Detection System]] — *Source: raw/scans/MEDS Overview.pdf*
- [[wiki/systems/MIT Reporting|MIT Reporting]] — *Source: raw/scans/MEDS Overview.pdf*
- [[wiki/systems/PTMMT|PTMMT]] — *Source: raw/scans/MEDS Overview.pdf*
- [[wiki/systems/UMM|UMM — Uber Map Model]] — *Source: raw/scans/MEDS Overview.pdf*
- [[wiki/systems/Uber ACI Service|Uber ACI Service]] — The Uber ACI (Automatic Change Identification) Service is an external Uber API that provides maneuver restriction data (turn restrictions such as "can left" / "no left") for map quality verification.
- [[wiki/systems/Veritas|Veritas]] — Veritas is the internal verification pipeline for maneuver (turn) restriction leads.
