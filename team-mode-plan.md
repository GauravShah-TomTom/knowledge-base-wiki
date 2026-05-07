# Team-mode for `knowledge-base-wiki`

## Context

`knowledge-base-wiki` (TomTom-internal fork at `github.com/tomtom-forks/knowledge-base-wiki/`) today is a single-user vault: each engineer's `raw/` and `wiki/` live on their own laptop. The Slack thread on the repo shows team-use is the open architectural question right now: Rijn Buve has it on his roadmap, Nathan Fleming tried it for FCD and hit storage scaling pain, Sagar Khanna built a parallel team variant (`tomtom-internal/DD-Team-Wiki`). This plan describes an end-to-end design for team-mode that addresses those concerns and can be contributed back upstream.

---

## How the system works (the basics this plan rests on)

1. **Drop raw stuff into `raw/`** — transcripts, emails, PDFs/scans, web clips, plain notes. In personal mode `raw/` is a folder on your laptop; in team mode it's an Azure Blob container — engineers upload via `az blob upload` or a small wrapper script.
2. **Ingestion turns raw into wiki.** The LLM reads each new file, identifies the people, decisions, systems, projects, problems mentioned, and writes structured Markdown pages in `wiki/<type>/...`. Same thing mentioned in two files → one wiki page with two source references. Pages link to each other via WikiLinks. QMD re-indexes the new content.
3. **Three ways to use the wiki:**
   - **Use A — ask questions.** You ask in natural language; QMD finds relevant pages; the LLM answers with citations.
   - **Use B — coding agents query it themselves.** The wiki's QMD index is exposed as an MCP server. Claude Code queries it on its own while working on a Jira ticket, so it has project context before writing code. PRs cite the wiki pages they relied on.
   - **Use C — generate new artefacts from it.** Tell the LLM "draft Jira stories from yesterday's planning meeting" or "summarise this month's decisions for WMR." It produces tickets, summaries, briefs from wiki content.

Today the repo does all of this for one person. Team-mode makes the *same* engine work for the whole team.

---

## Architecture

```
Azure Blob (raw/)            ← team uploads transcripts, emails, PDFs, scans, clips
       │
       │ ingest.yml: cron-scheduled GitHub Action (every 15 min)
       ▼
For each new blob:
       ├── runs scripts/wiki-ingest-loop.sh on that blob
       ├── ingest-time semantic comparison via QMD vs existing wiki/
       │     ├── near-duplicate → merge into existing page
       │     ├── contradiction  → raise ⚠️ CONFLICT in PR body
       │     └── otherwise      → write new wiki page(s)
       └── opens its own PR with the regenerated wiki/ pages
             ├── if no ⚠️ CONFLICT → auto-merge
             └── if ⚠️ CONFLICT    → CODEOWNERS review blocks merge

       │ index-rebuild.yml: triggers on push to main
       ▼
Rebuild qmd SQLite index → upload to Azure Blob (wiki-index/)

Developer laptop
       ├── git pull         → fetches latest wiki/ Markdown
       ├── make sync        → downloads latest-index.sqlite.gz from Blob
       └── Claude Code      → talks to local qmd MCP → answers cited from wiki
```

### Three architectural decisions

1. **Cron-triggered ingestion (every 15 min), not event-driven.** Avoids the Azure Function + Event Grid bridge needed for true blob-event triggering. Up-to-15-min latency is acceptable. Event-Grid-driven triggering is the upgrade path once team-mode is stable.
2. **PR-based ingestion with conflict-only review, one PR per source blob.** Each ingested blob produces its own PR (so a conflict in one source doesn't block unrelated good pages from a different source). Auto-merge by default. CODEOWNERS review required only when the LLM raises `⚠️ CONFLICT` in the PR body. **Detection mechanism:** during ingestion, for each candidate new wiki page the LLM does a QMD top-k similarity query against existing pages above a similarity threshold; if any existing page contradicts the new content, raise `⚠️ CONFLICT` with both passages quoted; if near-duplicate without contradiction, merge into existing; otherwise write new. (This is the same QMD-based mechanism that closes Rijn's flagged dedup weakness — not a separate feature.)
3. **Local SQLite consumption.** The pre-built SQLite index is downloaded by each developer (no re-embedding locally — that step is already paid by CI). Claude Code talks to a local `qmd mcp` server reading that file. Sub-second queries, no network. A managers' cloud persona could reuse the same SQLite via a remote container — out of this design's scope.

---

## Conflict resolution policy (what the reviewer does when ⚠️ CONFLICT fires)

Detection just flags. Resolution is the human's call, guided by a fixed policy. The PR opens with a *default draft* under "Supersede"; the reviewer either merges as-is, edits the diff, or closes.

| Action | When to use | What changes on the wiki page |
| --- | --- | --- |
| **Supersede** *(default draft)* | Team genuinely changed direction. | Update existing page **in place** — URL unchanged, WikiLinks intact. New "Current decision" replaces the top of the page; previous content moves to a "Decision history" section with date and source link. |
| **Append** | Disagreement is unresolved, or both views are legitimately on the table. | Add a "Conflicting views" section to the existing page; both passages quoted with sources. The page becomes a record of the open disagreement. |
| **Reject** | New source was speculative, mistaken, or out of scope. | Close the PR. Wiki unchanged. Optionally annotate the source as "rejected on review." |

**Never do any of these:**
- Silently overwrite without preserving history.
- Delete the existing page (breaks WikiLinks and the audit trail).
- Create a duplicate page at a new URL (forks history; future ingestions can't tell which to update).

This maps Karpathy's overwrite/append/flag strategies onto a concrete reviewer action — `flag` becomes `reject` because flag-and-leave accumulates unresolved conflicts forever; humans must actually resolve.

---

## How the cron knows what's new (`log.jsonl`)

`log.jsonl` is a simple registry of files the Action has **seen and attempted** — one line per blob with its path and ETag. It says nothing about whether the resulting PR was approved or rejected; that's separately reflected in the wiki content.

Each cron run:
1. Lists everything in Azure Blob `raw/`.
2. Diffs against `log.jsonl` on `main`.
3. For each unseen blob: writes one line to `log.jsonl` **before** the LLM runs. Then ingests and opens the PR.

Because the log entry is committed before the LLM runs, the registry is independent of PR outcome. If a PR is later rejected, the log still says "seen" — the next cron skips it. No re-ingestion, no reconciliation step.

---

## Implementation tasks

The work breaks down into independently testable tasks. Each is described at the *what* level only; the *how* of each is detailed in follow-up implementation work.

1. **Ingest raw data into Blob (team web UI app).** A web app with Entra ID SSO that handles all source types via a single channel: drag-drop for files (`.md`, `.vtt`, `.eml`, `.pdf`, `.jpg`, note-with-`_resources/` bundles); URL-paste for web clips (server-side fetch + Readability/Turndown clean) and Confluence pages (per-user Atlassian OAuth). v1 drops Microsoft Graph integration entirely (Teams transcripts and Outlook search) — engineers drag-drop `.vtt` / `.eml` themselves. Replaces the personal-mode CLI / drag-drop / Obsidian-Web-Clipper setup with one channel that non-engineers can use too.
   - **Stack (verified against official docs):** Next.js + TypeScript (frontend + API routes); Auth.js v5 with `microsoft-entra-id` provider for Entra SSO **only**; standard Atlassian OAuth 2.0 (3LO) with rotating refresh tokens; `@mozilla/readability` + `jsdom` + `turndown` (Node runtime only — jsdom incompatible with Edge); `@azure/storage-blob` with `DefaultAzureCredential` + managed identity (`Storage Blob Data Contributor` role) and `uploadStream` for large files; Azure Table Storage for an `oauth_grants` table (refresh tokens envelope-encrypted with `@azure/keyvault-keys` `CryptographyClient` — Table Storage SDK's built-in client-side encryption is deprecated v1, do not use); Azure Key Vault for KEKs and other secrets; **Azure Container Apps for hosting** (App Service has no Next.js-specific support; Static Web Apps Hybrid is Preview with a 250 MB cap); Application Insights for logs.

2. **Cron Action: blobs → wiki PR.** A scheduled GitHub Action that finds new blobs, records them in `log.jsonl`, runs ingestion with QMD-based conflict *detection* (resolution stays human via PR review), and opens one PR per blob — auto-merge unless `⚠️ CONFLICT` is raised.

3. **Index-rebuild Action.** A second GitHub Action triggered on push to `main` that incrementally rebuilds the QMD SQLite index for the updated wiki and uploads it to Azure Blob `wiki-index/`.

4. **Local consumption.** Engineer-side workflow to keep the local wiki + SQLite in sync from Blob, browse the wiki in Obsidian, and query it via Claude Code through the local QMD MCP server (Use A / B / C).

5. **Team chat UI + self-updating wiki (query feedback loop).** A multi-turn chat interface for non-engineers and engineers alike to query the wiki via the QMD MCP. Conversations have history, streaming, citations to source pages. Save flow: LLM suggests filing the thread when it reaches a useful synthesis (no per-message save button); user can also explicitly say *"save this"* at any time. On save, the LLM produces a `wiki/conversations/YYYY-MM-DD <title>.md` page (synthesis at top, full conversation in a collapsible block, citations preserved) and opens a PR through the same pipeline as Task 2 — QMD-based conflict-detection runs against the synthesis, auto-merge unless `⚠️ CONFLICT` is raised. This is the *self-updating wiki* loop: queries that produce non-trivial syntheses become permanent wiki pages, growing the knowledge base with use.
   - **Stack:** Next.js + TypeScript, shipped as a `/chat` route in the **same codebase** as Task 1 (`/upload`). Forked from Vercel's AI Chatbot template (`vercel/chatbot`); uses the AI SDK's `useChat` for state, plus optional `assistant-ui` components. Shares Auth.js (Entra ID) session, Atlassian OAuth tokens, and backend services with Task 1. Default template assumes Vercel-flavoured infra (Neon Postgres + Vercel Blob + Vercel AI Gateway); for self-host on Container Apps, swap to in-house Postgres / Azure Blob and direct provider calls. Citations rendering not first-class — built on top.

6. **MCP endpoint for IDE / external-agent access.** A new HTTP MCP server route in the **same Next.js codebase** as Tasks 1 + 5, exposing wiki operations as MCP tools — usable from Claude Code, Cursor, VS Code Copilot, or any MCP client. v1 tools: `query_wiki(question)` (cited answer via QMD MCP), `post_summary(title, markdown, tags?)` (creates `wiki/conversations/...` page via the same PR pipeline as Task 5), `list_recent_pages(type?, since?)`, `get_page(path)`. Authentication: per-user bearer tokens issued from a `/settings/tokens` page (Entra SSO behind it); token hashes stored in Table Storage keyed by `entraOid`; revocable. Reuses Task 1's auth + audit + Blob client; reuses Task 5's PR opener + synthesis backend. No new infrastructure beyond the existing Container Apps deploy.
   - **Stack:** `mcp-handler` v1 (npm package; repo at `vercel/mcp-adapter`) — Streamable HTTP transport, verified non-Vercel-specific (requires Node 18+, runs on any Next.js host including Container Apps). Tool definitions in `src/app/api/[transport]/route.ts` calling shared `lib/` services. Auth middleware: hash incoming bearer header, look up in Table Storage `api_tokens`, attach `entraOid` to request context.

### Task 1 / Task 5 boundary

Tasks 1 and 5 share one Next.js codebase but have a clean contract so Task 5 can be added without refactoring Task 1.

- **Task 1 owns:** upload UI, file-type routing, clip URL fetch (Readability + Turndown), Confluence/Atlassian OAuth, auth layer (Auth.js + Entra ID), per-user OAuth-token storage (Table Storage), Blob client, audit logging.
- **Task 5 owns:** chat UI, multi-turn state, conversation-to-page synthesis, save trigger logic (LLM-suggested + user-explicit), GitHub PR client.
- **The contract:** all reusable logic lives in `src/lib/` (`auth`, `auth/grants` accessor, `azure/blob`, `azure/tables`, `atlassian`, `markdown`, `naming`, `audit`, `pipeline`). Route handlers are thin glue — no business logic. The shared abstraction between Task 1 and Task 5 is the `WikiPage` shape (path + markdown + frontmatter validator), not a single writer. Task 1 implements `lib/pipeline/writeToBlob.ts`; Task 5 implements `lib/pipeline/openWikiPr.ts` (declared as a stub by Task 1 returning `NotImplemented`). Different sinks, different content shapes — do not collapse them under one `openPr` flag.
- **`oauth_grants` table schema (Task 1 writes; Task 5 reads via `lib/auth/grants.ts` accessor only — Task 5 never writes):** `PartitionKey: entraOid`, `RowKey: provider:scopeSetId` (e.g. `atlassian:default`); columns `encryptedRefreshToken, cekWrappedKey, kvKeyId, kvKeyVersion, scopes, tenantOrCloudId, expiresAt, rotatedAt, schemaVersion`. Schema version from day one.
- **Frontmatter Zod schemas in `lib/markdown/frontmatter.ts`** carry `schemaVersion`. Task 5 imports them as a public API; do not duplicate.

### Task 1 implementation guardrails (must-do, not nice-to-have)

- **Container Apps `minReplicas: 1`** for the clip-URL container — jsdom + Turndown + Atlassian SDK make scale-to-zero cold starts unacceptable.
- **No local disk persistence.** Stream uploads directly to Blob; never buffer to `/tmp`.
- **Secrets via `secretRef:` from Key Vault** — pipeline grants `Key Vault Secrets User` to the workload identity *before* the first revision deploys.
- **Single-flight refresh per `entraOid`** for OAuth tokens — Table Storage ETag check or short-TTL lock — to handle the Atlassian 10-min concurrent-refresh window without losing tokens.
- **Logging redaction wrapper** strips fields matching `*token*` / `*secret*` and `Authorization` headers by default; refresh tokens, `code_verifier`, and access tokens must never reach App Insights.
- **KEK rotation:** lazy (re-wrap on next read/write); no batch rotator in v1.
- **Atlassian 90-day idle:** v1 accepts re-consent; no keep-alive refresh job.
- **Audit log retention:** if needed beyond Container Apps' default 30 days, route logs to Blob via diagnostic settings.
- **Audit log record shape** (defined in `lib/audit.ts`, used by both Tasks 1 and 5): `{ ts, actor: entraOid, action, resource, txnId, outcome }`.

Each task is independently testable but only delivers end-to-end value together.

---

## Infrastructure strategy

- **Two repos.** `tomtom-forks/knowledge-base-wiki` (existing fork) gets the cron Action, index-rebuild Action, CODEOWNERS, helper scripts, and the `wiki-create-import-batches.sh` flag — eventually contributed upstream. The team-wiki app (Tasks 1 + 5 + 6 in one Next.js codebase) lives in a separate new internal repo (e.g. `tomtom-internal/team-wiki-app`).
- **IaC: Terraform** in `infra/` of the team-wiki app repo. Standard `terraform init && terraform plan && terraform apply` workflow. State stored in a dedicated Storage Account container (e.g. `stteamwikitfstate`). Idempotent, version-controlled, reproducible.
- **Hosting: Azure Container Apps** (verified: Microsoft has no Next.js-specific quickstart for App Service; SWA Hybrid is Preview with a 250 MB cap that we'd hit). Public ingress + mandatory Auth.js / Entra SSO on every route. Private endpoints / VNet integration deferred to v2.
- **Storage: a fresh dedicated storage account** (e.g. `stteamwiki<suffix>`) provisioned in the Owner subscription. Managed-identity-only access, no public access. Two Blob containers (`raw/`, `wiki-index/`) and three Tables (`oauth_grants`, `api_tokens`, `audit_log`). Reusing the existing `adasdevstorageaccount` was rejected — it's network-restricted, shared/production-tagged, and would require ADAS-team coordination. Cost: ~€2–5/month at our scale.
- **Container Registry: a fresh registry** for the team-wiki Docker image. Reusing a shared sandbox ACR is fine for early dev but a dedicated registry keeps image-level RBAC clean.
- **Container App environment: a fresh `cae-team-wiki`** rather than reusing `arxiv-env` or `slack-mcp-env` — cleaner isolation, separate diagnostic settings, no risk of one app pulling another's config.
- **Key Vault: fresh `kv-team-wiki`** holding all secrets (Entra client secret, Atlassian client ID + secret, GitHub PAT, Auth.js secret) plus the KEK for envelope-encrypted refresh tokens. Container App reads via `secretRef:` with managed-identity authentication.
- **Subscription: `1799fa65-ab4d-4e95-b818-28fa7105bb12`** (Owner sub).
- **Region: West Europe**.

---

## Pre-existing setup (already in place)

- **Azure subscription Owner** on `1799fa65-...` (full deploy authority).
- **Container Apps experience** — `slack-mcp-server`, `arxiv-mcp` already running in West Europe.
- **Entra app registration "TomTom Team Wiki"** created (`appId: c7fd56d5-79f1-4dd3-95dc-20181fcca962`). Single-tenant, redirect URI `http://localhost:3000/api/auth/callback/microsoft-entra-id`. Client secret captured.
- **Entra role: Application Developer** — can create app registrations independent of tenant policy.
- **Atlassian OAuth 2.0 (3LO) app** registered at `developer.atlassian.com/console/myapps/`. Client ID + secret captured.
- **GitHub PAT** generated for `tomtom-forks/knowledge-base-wiki`.
- **DNS** — using auto-assigned `*.westeurope.azurecontainerapps.io` URL; no custom domain needed.

## What still needs to be built / provisioned

- **New internal repo `tomtom-internal/team-wiki-app`** (Next.js codebase, Tasks 1 + 5 + 6).
- **Terraform `infra/` tree** in that repo — provisions: resource group, storage account `stteamwiki<suffix>` (with Blob containers + Tables), Key Vault, Container Registry, Container App environment, Container App, Application Insights, Log Analytics workspace, user-assigned Managed Identity, RBAC bindings (`Storage Blob Data Contributor`, `Storage Table Data Contributor`, `Key Vault Secrets User`).
- **Push secrets into Key Vault** (5 × `az keyvault secret set`).
- **Add the production redirect URI** to both the Entra app and the Atlassian app once Container Apps assigns the FQDN.
- **The two GitHub Actions** + helper scripts in `tomtom-forks/knowledge-base-wiki` (see "New files to add" below).
- **The `--one-file-per-batch` flag** on `scripts/wiki-create-import-batches.sh`.
- **The QMD top-k conflict-detection logic** in `.claude/skills/wiki-ingest-per-note/SKILL.md` line 72.

---

## Out of scope (deferred)

- **Event-driven ingestion** (Azure Blob → Event Grid → Function App → `workflow_dispatch`). Cron is fine for v1. Event Grid is the latency-upgrade path.
- **Microsoft Graph integration** (Teams transcripts, Outlook search-and-pick). `OnlineMeetingTranscript.Read.All` requires tenant admin consent; deferred to v2 as a single bundled feature contingent on that consent. v1 = drag-drop `.vtt` / `.eml`.
- **Manager / cloud persona for Use A.** Remote QMD MCP in an Azure Container App for browser-based AI clients (Claude.ai, ChatGPT). Same SQLite, different transport. Adds auth, per-user filtering, audit, rate-limiting concerns.
- **Auth on remote MCP, sensitive-content classifier, Confluence-as-source-of-truth question.** Real for production rollout. Not part of v1 design.
- **Additional MCP clients** (Rovo, Copilot Chat, OpenCode). Same QMD MCP, different surface; each is its own integration once enabled at the tenant level.
- **Private endpoints / VNet integration.** v1 ships public ingress + mandatory Entra SSO.

---

## Critical files (existing — to reuse / extend)

In the upstream repo:

- `README.md` lines 181–192 — QMD + MCP registration block. The lever the whole design turns on. *No change.*
- `scripts/wiki-ingest-loop.sh` — orchestrator (convert → partition → loop batches → finalize). Called from CI per-blob via the partitioner flag below. *No change to the script itself.*
- `scripts/wiki-create-import-batches.sh` — today auto-batches un-ingested files using `wiki/log.jsonl` to compute the diff. **Extend with a `--one-file-per-batch` flag** so CI can produce one PR per blob.
- `scripts/wiki-create-index-pages.py` — rebuilds `wiki/index.md` and the per-topic `_index.md` files. *No change.* Called by the index-rebuild Action after the wiki PR lands on main.
- `scripts/qmd-sync-collections.sh` — one-time QMD collections setup. Run during repo bootstrap, not per ingest. *No change.*
- `scripts/convert-vtt-to-md.py`, `scripts/convert-eml-to-md.py` — already invoked from `wiki-ingest-loop.sh` Phase 0. *No change.*
- `.claude/skills/wiki-ingest/SKILL.md` — coordinator skill. *No change.*
- `.claude/skills/wiki-ingest-per-note/SKILL.md` — per-note ingestion. **Extend the existing line-72 placeholder** *"Check if ingestion leads to contradictions"* with: *"Before writing a new wiki page, run a QMD top-k similarity query against existing pages above threshold T. If a top hit semantically contradicts the new content, mark the proposed page with `⚠️ CONFLICT` and quote both passages in the page-level batch log so the PR body surfaces it."*
- `wiki/log.jsonl` — *generated*, not hand-edited. Created/updated by the finalize step on each ingest cycle and committed back to the repo. Team-mode reuses the existing schema (`{date, session, file, summary, pages_created, pages_updated}`). Today only `.gitkeep` exists.
- `.gitignore` — verify `.import/` and QMD cache directories are excluded; add if missing.

## New files to add

In `tomtom-forks/knowledge-base-wiki`:

- `.github/workflows/wiki-ingest-cron.yml` — cron Action (every 15 min): pulls new blobs from Azure → runs `wiki-ingest-loop.sh` per blob via the partitioner's new `--one-file-per-batch` flag → opens one PR per blob → auto-merge unless `⚠️ CONFLICT` is raised. Writes the `log.jsonl` entry before the LLM runs.
- `.github/workflows/wiki-rebuild-index.yml` — triggers on push to `main`. Sequence per run: (1) `az blob download` previous SQLite from `wiki-index/`; (2) `gunzip` to `~/.cache/qmd/index.sqlite`; (3) `qmd update && qmd embed` to patch the SQLite incrementally for changed Markdown files; (4) `gzip`; (5) `az blob upload --overwrite` back to `wiki-index/`. **Cold start:** if Blob has no index yet, run `qmd embed` over the entire wiki once (expensive but one-time); subsequent runs are incremental.
- `scripts/azure-blob-download.sh` — fetches new blobs from the Azure `raw/` container into the Action's working directory.
- `scripts/qmd-sql-upload.sh` — gzips the rebuilt SQLite and uploads to `wiki-index/`. Used by the index-rebuild Action.
- `scripts/sync-index.sh` — developer-side: `az blob download + gunzip` → `~/.cache/qmd/index.sqlite`. Hooked from a git post-merge hook so `git pull` keeps the local index fresh.
- `CODEOWNERS` — page-path-to-reviewer mapping (e.g. `wiki/decisions/* @<owner>`) so `⚠️ CONFLICT` PRs auto-route.
- `.env.example` — documents required secrets: Azure Blob SAS / connection string, Anthropic API key, GitHub token. Real `.env` stays out of git; CI uses repo secrets.
- `docs/team-mode.md` — setup guide for the upstream PR: Blob containers, Action wiring, CODEOWNERS pattern, dev-laptop sync.

In the new `tomtom-internal/team-wiki-app` repo:

- `infra/` — Terraform tree (resource group, storage account, Key Vault, ACR, CAE, Container App, App Insights, Managed Identity, RBAC).
- `src/app/upload/` — Task 1 routes.
- `src/app/chat/` — Task 5 routes.
- `src/app/api/[transport]/route.ts` — Task 6 MCP endpoint.
- `src/app/settings/tokens/` — Task 6 API token management page.
- `src/lib/` — shared services (`auth`, `auth/grants`, `azure/blob`, `azure/tables`, `atlassian`, `markdown`, `naming`, `audit`, `pipeline/{writeToBlob,openWikiPr}`).
- `Dockerfile` + `.dockerignore`.
- `.env.example`.
- `README.md` — local dev setup, deploy steps.