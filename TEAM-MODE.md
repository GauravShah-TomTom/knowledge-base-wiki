# Team-mode for `knowledge-base-wiki`

A two-page operator's guide. What it is, what's in each repo, how the pieces glue together, what's running where.

---

## What it is

A team-shared knowledge base that ingests raw stuff (transcripts, emails, clips, screenshots, pasted notes) and turns it into structured Markdown wiki pages with citations. Two surfaces: a web chat for non-engineers, and a Claude Code MCP path for engineers. Karpathy's "wiki of yourself" — but for a team, with the ingest pipeline, retrieval index, and feedback loop in shared infrastructure.

## Repos

| Repo | What it holds |
|---|---|
| `GauravShah-TomTom/knowledge-base-wiki` | The wiki content (`wiki/<topic>/*.md`), ingest-cron + index workflows, `.claude/skills/` for engineers' CLI flows. Forked from upstream personal-mode wiki. |
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
  - **👍** saves the conversation as `wiki/conversations/YYYY-MM-DD <slug>.md` via a PR opened by the `team-wiki-feedback-bot` GitHub App; auto-merges.
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
- **Auth:** Auth.js v5 with Microsoft Entra ID provider (single-tenant — any TomTom employee can sign in). Per-user Atlassian access via stored PAT. Microsoft Graph integration (Teams, Outlook) is on the v2 list, not built today.
- **LLM (chat backend):** Azure OpenAI via TomTom's gateway (`api.chatgpt.tomtom-global.com`), deployment `dep-gpt-5-mini`, embedding `dep-text-embedding-3-small`.
- **Retrieval:** Azure AI Search Free tier (50 MB, 3 indexes, hybrid BM25 + vector, no semantic re-ranker).
- **Storage:** Azure Blob (raw/) + Tables (oauth_grants, apitokens, auditlog) on a dedicated storage account, managed-identity-only.
- **Secrets:** Azure Key Vault (`kv-team-wiki-ulkrw5`) — all 10 secrets mounted into the Container App via `secretRef:` with managed-identity auth.
- **Hosting:** Azure Container Apps (`ca-team-wiki`), `minReplicas: 1` to avoid jsdom cold-start. ACR pulls via managed identity.
- **Ingest LLM:** `anthropics/claude-code-action@v1` with the user's Claude Pro `CLAUDE_CODE_OAUTH_TOKEN`, model pinned to `claude-sonnet-4-6`.
- **Engineer-side:** team-wiki MCP server registration in Claude Code (per-user `twk_…` bearer); `wiki-ingest`, `wiki-query`, `wiki-feedback-up|down` skills in the wiki repo.
- **Bot:** dedicated GitHub App `team-wiki-feedback-bot` (Contents R/W, PRs R/W, Issues R/W). Authenticates per request via `@octokit/auth-app` using App ID + Installation ID + private key from Key Vault.

## Sequence (chat path)

1. User signs in to `/chat` via Entra SSO.
2. Types a question; `useChat` POSTs to `/api/chat`.
3. Server `auth()`-gates, embeds the question (`dep-text-embedding-3-small`), POSTs `search` + `vectorQueries` to Azure AI Search → top-8 hits.
4. Server stuffs hits as context, streams GPT-5-mini reply through `createUIMessageStream`. A pass-through buffer strips inline `[[wiki/...]]` markers and stray empty bullets the LLM sometimes emits.
5. After streaming ends, server emits `data-citations` with the cited page paths.
6. UI renders streamed text via Streamdown (markdown), shows citations as a collapsible Sources panel.
7. User clicks 👍 → POST `/api/chat/feedback` → `saveConversation()` → GitHub App opens a PR → auto-merge → next `wiki-aoai-index` run picks up the new `wiki/conversations/...` page.
8. User clicks 👎 → POST `/api/chat/feedback` → `flagStale()` → GitHub App commits frontmatter merge directly to `main` (one commit per cited page) → next staleness sweep prioritises these pages.

Engineer CLI path follows the same retrieval but skips steps 4–6 — `mcp__team-wiki__wiki_query` returns top-k hits as raw context for Claude Code to synthesise locally.

## Identities, apps & secrets

Five identities power the system. Each has a clear job, scope, and rotation cadence.

| Identity | What it does | Where credentials live | Rotation |
|---|---|---|---|
| **Entra app — `team-wiki` (Auth.js provider)** | Single-tenant OIDC sign-in for `/chat`, `/upload`, `/settings/*`. Issues an ID token; we extract `oid` (Entra Object ID) and use it as the user key. | App registration in Entra; client secret in Key Vault as `auth-entra-client-secret`. | Manual; secret expires per Entra policy (default 24 mo). |
| **AAD app — `team-wiki-ci` (`39a79fb6-…`)** | OIDC federation for the wiki repo's GitHub Actions. Lets workflows `az login` without storing service-principal credentials in repo secrets. Has Search Service Contributor + Search Index Data Contributor on the AI Search resource. | Federated via OIDC trust on the GitHub repo. No secret stored anywhere — the `id-token: write` workflow permission produces a short-lived token per run. | None (token-less). |
| **User-assigned managed identity — `id-team-wiki`** | The Container App's runtime identity. RBAC: Storage Blob/Table Data Contributor (raw/, the 3 tables), Key Vault Secrets User, AcrPull, Search Index Data Reader. Zero hard-coded credentials in app code. | Assigned to the Container App by Terraform; `DefaultAzureCredential` picks it up. | None (Azure-managed). |
| **GitHub App — `team-wiki-feedback-bot`** | Opens PRs (👍 path) and commits to `main` (👎 path) on the wiki repo. Uses an *App identity*, not a PAT, so it's revocable without affecting any user. Permissions: Contents R/W, Pull requests R/W, Issues R/W. Installed only on `GauravShah-TomTom/knowledge-base-wiki`. | App ID, Installation ID, private key (PEM) live in Key Vault as `github-app-id`, `github-app-installation-id`, `github-app-private-key`. `lib/github/app-auth.ts` exchanges these for a short-lived installation access token per request via `@octokit/auth-app`. | Private key expires 1y by default; rotate via the App's settings page. |
| **Per-user MCP bearer — `twk_<64hex>`** | Engineer's Claude Code → team-wiki MCP server. Issued at `/settings/tokens` (any signed-in TomTom user can issue their own). SHA-256 hashed at rest in `apitokens` Table; validation is one O(1) `getEntity()`. | Plain token shown to the user once at issuance; nothing stored on disk by the server. | User revokes via the same page. |

**Two more credentials that aren't identities but matter:**

| Secret | Purpose | Where it lives | Rotation |
|---|---|---|---|
| **`CLAUDE_CODE_OAUTH_TOKEN`** | Authenticates `anthropics/claude-code-action@v1` against the Claude Pro/Max subscription. Used by `wiki-ingest-cron.yml` and `wiki-staleness-sweep.yml` to drive a Claude session in CI without an Anthropic API key (no project budget needed). | GitHub repo secret on `knowledge-base-wiki` only. Generated locally with `claude setup-token`. | Long-lived OAuth refresh token, ~1y validity; regenerate with `claude setup-token` and update the repo secret. Internal precedent: same pattern Manan Pandya uses for the Dependabot review action across 14+ TomTom repos. |
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
       │                    PUT /repos/.../contents/<path>     ← App identity
       │                                                          commit author = bot
       ▼
openWikiPr(): create branch + PUT a file + open PR + auto-merge ← App identity
       │                                                          commit author = bot
       ▼
Auto-merge → push to main → wiki-aoai-index workflow re-embeds the new page
```

The same lib code (`lib/github/{app-auth,pr,issues}.ts`) backs both paths. App-based auth means commits show up in `git log` as `team-wiki-feedback-bot[bot]`, not as a human — useful for filtering.

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

# 2. Populate Key Vault with the 9 manually-managed secrets
#    (auth-secret, auth-entra-client-secret, atlassian-client-id/-secret,
#     github-pat, github-app-id/-installation-id/-private-key,
#     azure-openai-api-key) — azure-search-api-key is set by Terraform.

# 3. CI secrets on knowledge-base-wiki repo
#    AZURE_CLIENT_ID, AZURE_TENANT_ID, AZURE_SUBSCRIPTION_ID  (OIDC federation)
#    AZURE_OPENAI_API_KEY, AZURE_SEARCH_API_KEY                (index workflow)
#    CLAUDE_CODE_OAUTH_TOKEN                                   (ingest action)

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
# 1. Clone the wiki for local browsing (Obsidian, file edits, skills)
git clone GauravShah-TomTom/knowledge-base-wiki && cd knowledge-base-wiki

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

This repo is a fork of `tomtom-forks/knowledge-base-wiki`, which moves quickly. The team-mode delta is mostly net-new files (zero conflict surface), so syncing is usually clean.

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
- **Atlassian OAuth (3LO).** Spec called for it; we shipped PAT instead. PATs don't rotate; users must re-paste when expired.

## Out of scope (v2)

Event-driven ingest (Event Grid → Function App). Manager / cloud persona (remote MCP for ChatGPT/Claude.ai). Sensitive-content classifier on uploads. Per-blob PRs (currently per-cron-run). Mobile responsive pass.
