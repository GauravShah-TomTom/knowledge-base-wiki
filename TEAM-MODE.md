# Team-mode for `knowledge-base-wiki`

A two-page operator's guide. What it is, what's in each repo, how the pieces glue together, what's running where.

---

## What it is

A team-shared knowledge base that ingests raw stuff (transcripts, emails, clips, screenshots, pasted notes) and turns it into structured Markdown wiki pages with citations. Two surfaces: a web chat for non-engineers, and a Claude Code MCP path for engineers. Karpathy's "wiki of yourself" — but for a team, with the ingest pipeline, retrieval index, and feedback loop in shared infrastructure.

## Repos

| Repo | What it holds |
|---|---|
| `tomtom-internal/knowledge-base-team-wiki` | The wiki content (`wiki/<topic>/*.md`), ingest-cron + index workflows, `.claude/skills/` for engineers' CLI flows. Derived from upstream personal-mode wiki at `tomtom-forks/knowledge-base-wiki` (no GitHub fork relationship; sync via `git remote add upstream`). |
| `tomtom-internal/team-wiki-app` | The Next.js app: web upload UI, chat UI, MCP server, feedback endpoints, Terraform for all Azure infra. |

## Architecture

```
              ┌─────────────────────────────────────────┐
  uploads     │         team-wiki-app  (Container App)  │
  (web)──────▶│  /upload   /chat   /api/mcp   /settings │
              │  /api/chat/feedback                     │
              └────────────┬────────────────────────────┘
                           │ writes raw/, queries Azure AI Search
                           ▼
                  ┌───────────────────────┐
                  │  Azure Blob (raw/)    │ ←──┐
                  └───────────┬───────────┘    │
                              │ cron 15 min    │  PRs (feedback,
                              ▼                │   ingest)
                  ┌───────────────────────┐    │
                  │  GitHub Actions:      │    │
                  │  ingest-cron + claude │────┘
                  │  -code-action wires   │
                  │  in wiki-ingest skill │
                  └───────────┬───────────┘
                              │ commits Markdown to wiki/
                              ▼
                  ┌───────────────────────┐
                  │  knowledge-base-wiki  │
                  │  (main)               │
                  └───────────┬───────────┘
                              │ on push to wiki/**
                              ▼
                ┌────────────────────────────────────┐
                │  Azure AI Search (BM25 + vector)   │
                │  Single index serving:             │
                │   • chat UI (server-side)          │
                │   • engineer CLI via team-wiki MCP │
                └────────────────────────────────────┘
```

## Functionality

- **Ingest.** Three input paths, all writing to Azure Blob `raw/`:
  - **Upload UI** (`/upload`): drag-drop file → routed by extension to `raw/notes/` (`.md`), `raw/transcripts/` (`.vtt`), `raw/emails/` (`.eml`), `raw/scans/` (PDF/JPG/PNG), or `raw/clips/` (web URL paste, server-side Readability + Turndown). Confluence URL paste pulls via stored per-user Atlassian PAT and lands at `raw/confluence/`.
  - **MCP add tools** from Claude Code: `wiki_add_slack_thread`, `wiki_add_note`, `wiki_add_clip`, `wiki_add_transcript` — engineer pastes content; tool writes Markdown to the corresponding `raw/<subfolder>/`.
  - A 15-min cron Action (`wiki-ingest-cron.yml`) downloads new blobs, runs `claude-code-action` on the `wiki-ingest` skill, opens a PR with the generated `wiki/` pages. Auto-merge unless the per-note skill writes `CONFLICT: ...` to `.import/conflict-status.txt`.
- **Indexing.** Single Azure AI Search index, rebuilt by `wiki-aoai-index.yml` on push to `wiki/**` — BM25 + vector via `text-embedding-3-small`, hybrid retrieval. Used by both chat UI and engineer MCP queries.
- **Chat (web).** `/chat` runs `useChat` from the AI SDK. The route handler embeds the question, runs hybrid retrieval over Azure AI Search, stuffs top-8 pages as context, streams a GPT-5-mini answer through Vercel AI Elements components (Conversation / Message / Sources / PromptInput).
- **Engineer (CLI).** Register the team-wiki MCP server with a `twk_…` token (issued at `/settings/tokens`). `mcp__team-wiki__wiki_query` and `mcp__team-wiki__wiki_get_page` hit the same Azure AI Search index the chat UI uses. Saves and feedback go through `mcp__team-wiki__wiki_feedback_up|down`.
- **Feedback.**
  - **👍** saves the conversation as `wiki/conversations/YYYY-MM-DD <slug>.md` via a PR opened with a per-server PAT (`GITHUB_TOKEN` env, sourced from Key Vault `github-pat`); auto-merges.
  - **👎** commits a frontmatter merge directly to `main` (no PR, no issue) — one commit per cited page, incrementing `feedback_count_negative` and setting `last_feedback_negative` to today. The weekly staleness sweep digests these signals.
  - Both surfaces (chat-UI buttons + CLI `/wiki-feedback-up|down` skills) share the same `lib/feedback/{save-conversation,flag-stale}.ts` code.
- **Staleness sweep.** Weekly Action (`wiki-staleness-sweep.yml`, Mondays 09:00 UTC) runs Claude Code over the wiki, prioritises pages with `feedback_count_negative > 0`, opens one PR with `⚠️ STALE` markers + a digest table for human review.

**MCP tool surface (8 tools, all `mcp__team-wiki__*`):**

| Tool | Purpose |
|---|---|
| `wiki_query(query, top_k?)` | Hybrid BM25 + vector search |
| `wiki_get_page(path)` | Fetch single page by exact path |
| `wiki_add_slack_thread` | Save Slack thread → `raw/slack/` |
| `wiki_add_note` | Save free-form note → `raw/notes/` |
| `wiki_add_clip` | Save web article → `raw/clips/` |
| `wiki_add_transcript` | Save meeting transcript → `raw/transcripts/` |
| `wiki_feedback_up` | 👍 — save conversation page |
| `wiki_feedback_down` | 👎 — flag cited pages stale |

## Tools & technology

- **Frontend:** Next.js 16 (App Router) + TypeScript, Tailwind v4, shadcn/ui, Vercel AI SDK + AI Elements (`Conversation`, `Message`, `Sources`, `PromptInput`).
- **Auth:** Auth.js v5 with Microsoft Entra ID provider (single-tenant — any TomTom employee can sign in). Per-user Atlassian access via **OAuth 2.0 (3LO)** — user clicks Connect on `/settings/atlassian`, consents on Atlassian, app stores access + refresh tokens in the `oauthgrants` Azure Table for that user. Access tokens auto-refresh in the background using the rotating refresh token. Microsoft Graph integration (Teams, Outlook) is on the v2 list, not built today.
- **LLM (chat backend):** Azure OpenAI via TomTom's gateway (`api.chatgpt.tomtom-global.com`), deployment `dep-gpt-5-mini`, embedding `dep-text-embedding-3-small`.
- **Retrieval:** Azure AI Search Free tier (50 MB, 3 indexes, hybrid BM25 + vector + semantic ranker on the `free` semantic plan — 1000 free queries/month).
- **Storage:** Azure Blob (raw/) + Tables (oauth_grants, apitokens, auditlog) on a dedicated storage account, managed-identity-only.
- **Secrets:** Azure Key Vault (`kv-team-wiki-ulkrw5`) — all 10 secrets mounted into the Container App via `secretRef:` with managed-identity auth.
- **Hosting:** Azure Container Apps (`ca-team-wiki`), `minReplicas: 1` to avoid jsdom cold-start. ACR pulls via managed identity.
- **Ingest LLM:** `anthropics/claude-code-action@v1` with the user's Claude Pro `CLAUDE_CODE_OAUTH_TOKEN`, model pinned to `claude-sonnet-4-6`.
- **Engineer-side:** team-wiki MCP server registration in Claude Code (per-user `twk_…` bearer); `wiki-ingest`, `wiki-query`, `wiki-feedback-up|down` skills in the wiki repo.
- **Bot identity:** a fine-grained **PAT** (scoped to `tomtom-internal/knowledge-base-team-wiki`, perms: Contents R/W, PRs R/W, Issues R/W). Sits in Key Vault as `github-pat`, mounted into the Container App as the `GITHUB_TOKEN` env var, used by `src/lib/github/app-auth.ts` to instantiate Octokit. **Why PAT, not a GitHub App?** Installing a third-party GitHub App on the `tomtom-internal` org requires admin approval; the PAT path is identical in capability and self-service. Trade-off: PATs expire (1 year max) and need rotation; App private keys expire too but quietly auto-rotate via the installation token API.

## Sequence (chat path)

1. User signs in to `/chat` via Entra SSO.
2. Types a question; `useChat` POSTs to `/api/chat`.
3. Server `auth()`-gates, embeds the question (`dep-text-embedding-3-small`), POSTs `search` + `vectorQueries` to Azure AI Search → top-8 hits.
4. Server stuffs hits as context, streams GPT-5-mini reply through `createUIMessageStream`. A pass-through buffer strips inline `[[wiki/...]]` markers and stray empty bullets the LLM sometimes emits.
5. After streaming ends, server emits `data-citations` with the cited page paths.
6. UI renders streamed text via Streamdown (markdown), shows citations as a collapsible Sources panel.
7. User clicks 👍 → POST `/api/chat/feedback` → `saveConversation()` → PAT (Octokit) opens a PR → auto-merge → next `wiki-aoai-index` run picks up the new `wiki/conversations/...` page.
8. User clicks 👎 → POST `/api/chat/feedback` → `flagStale()` → PAT (Octokit) commits frontmatter merge directly to `main` (one commit per cited page) → next staleness sweep prioritises these pages.

Engineer CLI path follows the same retrieval but skips steps 4–6 — `mcp__team-wiki__wiki_query` returns top-k hits as raw context for Claude Code to synthesise locally.

## Identities, apps & secrets

Five identities power the system. Each has a clear job, scope, and rotation cadence.

| Identity | What it does | Where credentials live | Rotation |
|---|---|---|---|
| **Entra app — `team-wiki` (Auth.js provider)** | Single-tenant OIDC sign-in for `/chat`, `/upload`, `/settings/*`. Issues an ID token; we extract `oid` (Entra Object ID) and use it as the user key. | App registration in Entra; client secret in Key Vault as `auth-entra-client-secret`. | Manual; secret expires per Entra policy (default 24 mo). |
| **AAD app — `team-wiki-ci` (`39a79fb6-…`)** | OIDC federation for the wiki repo's GitHub Actions. Lets workflows `az login` without storing service-principal credentials in repo secrets. Has Search Service Contributor + Search Index Data Contributor on the AI Search resource. | Federated via OIDC trust on the GitHub repo. No secret stored anywhere — the `id-token: write` workflow permission produces a short-lived token per run. | None (token-less). |
| **User-assigned managed identity — `id-team-wiki`** | The Container App's runtime identity. RBAC: Storage Blob/Table Data Contributor (raw/, the 3 tables), Key Vault Secrets User, AcrPull, Search Index Data Reader. Zero hard-coded credentials in app code. | Assigned to the Container App by Terraform; `DefaultAzureCredential` picks it up. | None (Azure-managed). |
| **GitHub PAT — wiki bot token** | Opens PRs (👍 path) and commits to `main` (👎 path) on the wiki repo. Fine-grained PAT scoped to `tomtom-internal/knowledge-base-team-wiki` only, perms Contents R/W + Pull requests R/W + Issues R/W. Previously this was the `team-wiki-feedback-bot` GitHub App, but installing a third-party App on the `tomtom-internal` org requires admin approval — the PAT path is self-service and identical in capability. | Single secret in Key Vault as `github-pat`; mounted into the Container App as `GITHUB_TOKEN` env var. `lib/github/app-auth.ts` (legacy filename) reads it and instantiates Octokit. The same PAT also fronts the cron-ingest workflow on the wiki repo (`WIKI_BOT_PAT` GHA secret). | Expires per the PAT's chosen TTL (1y max). Rotate by creating a new PAT, updating both the Key Vault secret and the GHA repo secret. |
| **Per-user MCP bearer — `twk_<64hex>`** | Engineer's Claude Code → team-wiki MCP server. Issued at `/settings/tokens` (any signed-in TomTom user can issue their own). SHA-256 hashed at rest in `apitokens` Table; validation is one O(1) `getEntity()`. | Plain token shown to the user once at issuance; nothing stored on disk by the server. | User revokes via the same page. |

**Two more credentials that aren't identities but matter:**

| Secret | Purpose | Where it lives | Rotation |
|---|---|---|---|
| **`CLAUDE_CODE_OAUTH_TOKEN`** | Authenticates `anthropics/claude-code-action@v1` against the Claude Pro/Max subscription. Used by `wiki-ingest-cron.yml` and `wiki-staleness-sweep.yml` to drive a Claude session in CI without an Anthropic API key (no project budget needed). | GitHub repo secret on `tomtom-internal/knowledge-base-team-wiki`; mirrored in Key Vault as `claude-code-oauth-token` for parity. Generated locally with `claude setup-token`. | Long-lived OAuth refresh token, ~1y validity; regenerate with `claude setup-token` and update the repo secret + KV. Internal precedent: same pattern Manan Pandya uses for the Dependabot review action across 14+ TomTom repos. |
| **Azure OpenAI + Search keys** | `azure-openai-api-key` for chat + embeddings; `azure-search-api-key` for index writes from the indexer workflow. Container App reads both via `secretRef:` from KV; the wiki repo's CI reads them as repo secrets for the indexer run. | Key Vault (Container App) + GitHub repo secrets (CI). `azure-search-api-key` is Terraform-managed (sourced from the resource itself). | Manual key rotation; update both KV and repo secret. |

**What the bot actually does, end-to-end:**

```
Chat UI 👍 click           Chat UI 👎 click
       │                          │
       ▼                          ▼
/api/chat/feedback        /api/chat/feedback
       │                          │
       ▼                          ▼
saveConversation()         flagStale()
       │                          │
       │                          ▼
       │                  for each cited page:
       │                    GET /repos/.../contents/<path>
       │                    merge frontmatter (count++, date)
       │                    PUT /repos/.../contents/<path>     ← PAT (GITHUB_TOKEN)
       │                                                          commit author = PAT owner
       ▼
openWikiPr(): create branch + PUT a file + open PR + auto-merge ← PAT (GITHUB_TOKEN)
       │                                                          commit author = PAT owner
       ▼
Auto-merge → push to main → wiki-aoai-index workflow re-embeds the new page
```

The same lib code (`lib/github/{app-auth,pr,issues}.ts` — filename retained from the App era; the implementation now reads a PAT) backs both paths. PAT auth means commits show up in `git log` under the PAT-owner's account, not a bot. Trade-off vs. an App: less clean attribution in `git log`, but no admin-approval gate and easier to manage.

## Cost (rough monthly, EUR)

| Component | ~Cost |
|---|---|
| Container App (1 replica, 0.5 vCPU, 1Gi memory) | 20–30 |
| Storage (Blob + Tables, ~50 MB) | 1–2 |
| ACR Basic | 5 |
| Key Vault (Standard, ~10 ops/min) | <1 |
| AI Search **Free** tier | 0 |
| Log Analytics + App Insights (PerGB2018, 30d retention) | 5–10 |
| **Total** | **~35–50 EUR/month** |

GitHub Actions minutes used by cron + index + staleness sweep stay well under the 2000-min/month free tier on a private org repo.

## Setup (one-time, Azure side)

```sh
# 1. Clone, configure
cd team-wiki-app/infra && terraform init && terraform plan && terraform apply

# 2. Populate Key Vault with the manually-managed secrets
#    (auth-secret, auth-entra-client-secret, atlassian-client-id/-secret,
#     github-pat, azure-openai-api-key, claude-code-oauth-token)
#    — azure-search-api-key is set by Terraform.

# 3. CI secrets on tomtom-internal/knowledge-base-team-wiki repo
#    AZURE_CLIENT_ID, AZURE_TENANT_ID, AZURE_SUBSCRIPTION_ID  (OIDC federation)
#    AZURE_OPENAI_API_KEY, AZURE_SEARCH_API_KEY               (index workflow)
#    CLAUDE_CODE_OAUTH_TOKEN                                  (ingest action)
#    WIKI_BOT_PAT                                             (cron auto-merge)

# 4. Initial deploy: GitHub Actions builds the Docker image, pushes to ACR,
#    `az containerapp update`s the revision. URL: https://ca-team-wiki.<env>.azurecontainerapps.io
```

## Setup (local dev for chat work)

```sh
cd team-wiki-app
./scripts/pull-env.sh          # writes .env.local from Key Vault
echo "AUTH_DEV_BYPASS=1" >> .env.local
npm run dev                    # http://localhost:3300/chat
# OR exercise just retrieval+LLM without UI:
node --env-file=.env.local scripts/smoke-chat.mjs "your question"
```

## Setup (engineer's local Claude Code)

```sh
# 1. Clone the wiki for local browsing (Obsidian, file edits, skills).
#    Optional: also add the upstream personal-mode wiki as an `upstream` remote
#    so you can fetch upstream changes:
git clone https://github.com/tomtom-internal/knowledge-base-team-wiki && cd knowledge-base-team-wiki
git remote add upstream https://github.com/tomtom-forks/knowledge-base-wiki.git

# 2. Issue yourself a team-wiki bearer token at
#    https://ca-team-wiki.<env>.azurecontainerapps.io/settings/tokens

# 3. Register the team-wiki MCP server in your Claude Code config
#    (~/.claude.json or via `claude mcp add`):
{
  "mcpServers": {
    "team-wiki": {
      "url": "https://ca-team-wiki.<env>.azurecontainerapps.io/api/mcp/mcp",
      "headers": { "Authorization": "Bearer twk_..." }
    }
  }
}

# 4. Try it: /wiki-query "who is leading id index improvement"
#    Behind the scenes Claude calls mcp__team-wiki__wiki_query → Azure AI Search.
```

No local SQLite, no `az login`, no post-merge hook — the MCP server fronts the same index the chat UI uses.

## Syncing from upstream

This repo is a derivative of `tomtom-forks/knowledge-base-wiki` (no GitHub-side fork relationship — when you clone, run `git remote add upstream https://github.com/tomtom-forks/knowledge-base-wiki.git` once). Upstream moves quickly. The team-mode delta is mostly net-new files (zero conflict surface), so syncing is usually clean.

```sh
git fetch upstream
git merge upstream/main
# resolve any conflicts (see below), then:
git push origin main
```

**Known recurring conflict surface (3 files):**

| File | Reason | Resolution |
|---|---|---|
| `.gitignore` | We removed upstream's `wiki/` line because we track `wiki/` as team content. (Negation `!wiki/` can't reverse a directory-level ignore.) | Always keep our version (no `wiki/` line). |
| `.claude/skills/wiki-ingest-per-note/SKILL.md` | We added a `[team-mode]` QMD-driven conflict-detection bullet *after* upstream's existing one. Pure addition — usually merges cleanly. | Keep both upstream's bullet and our `[team-mode]` block. |
| `.claude/skills/wiki-query/SKILL.md` | We appended two bullets at the end (stale-feedback awareness; prefer MCP for save). Pure addition at end of list. | Keep both upstream's bullets and our two appended ones. |

Everything else (new workflows, new scripts, new skills, all `wiki/**` content) is additive and conflict-free.

**Long term:** the team-mode bundle is meant to be contributed back upstream (per the original spec). Once that lands, this whole section goes away.

## Known gaps (v1)

- **Standalone PDFs/images.** The upload UI routes PDF/JPG/PNG to `raw/scans/`, but the `wiki-ingest-per-note` skill's Phase 0 only converts `.vtt` and `.eml`. PDFs/images are described in the skill only as note-attachment files (in `_resources/`). A standalone PDF dropped in `raw/scans/` may not be ingested unless the cron's Claude session walks the directory and converts it itself. Workaround: drop PDFs alongside an `_resources/`-style note with the same basename, or paste extracted text as a `.md` note.
- **App-level RBAC.** Single-tenant Entra means every TomTom employee can sign in, hit `/chat`, `/upload`, and click 👍 to merge a wiki page. No allow-list / group restriction. Fine for the innovation-week pilot, not for production rollout.
- **Conversation history.** The chat is ephemeral — reload nukes the thread. No server-side persistence keyed by `entraOid` yet.
- **Microsoft Graph integration.** Teams transcript browse + Outlook email search were in the original spec but not built. Engineers can still upload `.vtt`/`.eml` files manually via drag-drop.
- ~~**Atlassian OAuth (3LO).** Spec called for it; we shipped PAT instead.~~ **Now shipped (2026-05-18):** per-user OAuth 2.0 (3LO) via `/settings/atlassian` → Connect button. Access tokens auto-refresh; users re-consent only after 90 days idle.

## Out of scope (v2)

Event-driven ingest (Event Grid → Function App). Manager / cloud persona (remote MCP for ChatGPT/Claude.ai). Sensitive-content classifier on uploads. Per-blob PRs (currently per-cron-run). Mobile responsive pass.
