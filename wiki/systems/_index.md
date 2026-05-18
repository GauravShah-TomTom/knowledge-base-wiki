---
type: index
date: 2026-05-18 14:49:12
---
# Systems - index
[[wiki/index|← Index]]

Our products, platforms, and services.

- [[wiki/systems/Airflow|Airflow]] — Apache Airflow is the workflow orchestration platform planned for the end-to-end [[Lanes]] pipeline to replace the current single-zone GitHub Actions trigger.
- [[wiki/systems/Cross Link|Cross Link]] — Cross Link is a processing component that runs on [[Databricks]] alongside [[Data Preparator]] as part of the [[Lanes]] pipeline.
- [[wiki/systems/Data Preparator|Data Preparator]] — Data Preparator is an upstream component in the [[Lanes]] pipeline that runs on [[Databricks]].
- [[wiki/systems/Databricks|Databricks]] — Databricks is the cloud data platform used by the [[Lanes]] pipeline to run [[Data Preparator]] and [[Cross Link]] at scale.
- [[wiki/systems/Genesis|Genesis]] — Genesis is a QA and map data system used in the [[Lanes]] pipeline and the [[HD Basemap]] workflow.
- [[wiki/systems/GeoCatch|GeoCatch]] — GeoCatch is the Missing Roads detector within [[MEDS]].
- [[wiki/systems/HD Basemap|HD Basemap]] — [[TomTom]]'s HD (high-definition) map basemap product, containing detailed road geometry, lane models, and junction topology.
- [[wiki/systems/Iris|Iris]] — Iris is the task management system used by map editors to review and validate lane transactions produced by the [[Lanes]] pipeline.
- [[wiki/systems/Lanes Automator|Lanes Automator]] — Lanes Automator is the core processing service in the [[Lanes]] pipeline.
- [[wiki/systems/MCR|MCR]] — MCR (likely Map Change Repository) is the downstream system that receives map change transactions created by [[Transaction Manager]] in the [[Lanes]] pipeline.
- [[wiki/systems/MEDS|MEDS — Map Error Detection System]] — MEDS is Uber's automated map-healing platform that proactively detects, classifies, and fixes map data errors by analysing driver behaviour signals (route divergences, segment traversals, transition traversals) against the [[UMM|Uber Map Model]].
- [[wiki/systems/MIT|MIT — Map Issue Tracking]] — MIT (Map Issue Tracking) is the reporting system that receives output from [[MEDS]] detectors.
- [[wiki/systems/Map Content Portal|Map Content Portal]] — TomTom's internal portal for publishing and browsing map data releases.
- [[wiki/systems/Orbis|Orbis]] — Orbis is a map data platform and delivery layer used in TomTom's [[Lanes]] pipeline and [[HD Basemap]] workflow.
- [[wiki/systems/PTMMT|PTMMT]] — PTMMT is a system in the [[Route Divergence]] pipeline within [[MEDS]].
- [[wiki/systems/Transaction Manager|Transaction Manager]] — Transaction Manager is a web service in the [[Lanes]] pipeline that converts output JSON files from [[Lanes Automator]] into map change transactions and sends them to [[MCR]].
- [[wiki/systems/UMM|UMM — Uber Map Model]] — The Uber Map Model (UMM) is Uber's internal map data schema.
- [[wiki/systems/Viva Glint|Viva Glint]] — Microsoft's employee engagement and feedback platform, used by TomTom to run organisation-wide engagement surveys.
