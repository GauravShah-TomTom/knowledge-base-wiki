---
type: index
date: 2026-05-15 16:47:15
---
# Systems - index
[[wiki/index|← Index]]

Our products, platforms, and services.

- [[wiki/systems/Airflow|Airflow]] — Apache Airflow is the workflow orchestration platform planned for the end-to-end [[Lanes]] pipeline to replace the current single-zone GitHub Actions trigger.
- [[wiki/systems/Cross Link|Cross Link]] — Cross Link is a processing component that runs on [[Databricks]] alongside [[Data Preparator]] as part of the [[Lanes]] pipeline.
- [[wiki/systems/Data Preparator|Data Preparator]] — Data Preparator is an upstream component in the [[Lanes]] pipeline that runs on [[Databricks]].
- [[wiki/systems/Databricks|Databricks]] — Databricks is the cloud data platform used by the [[Lanes]] pipeline to run [[Data Preparator]] and [[Cross Link]] at scale.
- [[wiki/systems/Genesis|Genesis]] — Genesis is a map data source referenced in the [[Lanes]] pipeline.
- [[wiki/systems/Iris|Iris]] — Iris is the task management system used by map editors to review and validate lane transactions produced by the [[Lanes]] pipeline.
- [[wiki/systems/Lanes Automator|Lanes Automator]] — Lanes Automator is the core processing service in the [[Lanes]] pipeline.
- [[wiki/systems/MCR|MCR]] — MCR (likely Map Change Repository) is the downstream system that receives map change transactions created by [[Transaction Manager]] in the [[Lanes]] pipeline.
- [[wiki/systems/Orbis|Orbis]] — Orbis is a map data source referenced in the [[Lanes]] pipeline.
- [[wiki/systems/Transaction Manager|Transaction Manager]] — Transaction Manager is a web service in the [[Lanes]] pipeline that converts output JSON files from [[Lanes Automator]] into map change transactions and sends them to [[MCR]].
