<!--
name: "Skill: Building LLM-powered applications with Claude"
description: "Guides Claude in building LLM-powered applications using the Anthropic SDK, covering language detection, API surface selection (Claude API vs Managed Agents), model defaults, thinking/effort configuration, and language-specific documentation reading"
ccVersion: "2.1.235"
-->
# Building LLM-Powered Applications with Claude.

This skill helps you build LLM-powered applications with Claude. Choose the right surface based on your needs, detect the project language, then read the relevant language-specific documentation.

## Before You Start.

Scan the target file (or, if no target file, the prompt and project) for non-Anthropic provider markers — `import openai`, `from openai`, `langchain_openai`, `OpenAI(`, `gpt-4`, `gpt-5`, file names like `agent-openai.py` or `*-generic.py`, or any explicit instruction to keep the code provider-neutral. If you find any, stop and tell the user that this skill produces Claude/Anthropic SDK code. Ask whether they want to switch the file to Claude or want a non-Claude implementation. Do not edit a non-Anthropic file with Anthropic SDK calls. (Exception: the `prompt-audit` subcommand is non-interactive and does not stop here. It records non-Anthropic provider markers in its report's stated assumptions and never proposes switching a non-Anthropic file to the Anthropic SDK.)

## Output Requirement.

The user can ask you to add, modify, or implement a Claude feature. Then your code must call Claude through one of:

1. **The official Anthropic SDK** for the project's language (`anthropic`, `@anthropic-ai/sdk`, `com.anthropic.*`, and more). This is the default whenever a supported SDK exists for the project.
2. **Raw HTTP** (`curl`, `requests`, `fetch`, `httpx`, and more). Only where the user explicitly asks for cURL/REST/raw HTTP, or the project is a shell/cURL project. Or the language lacks an official SDK.

Never mix the two. Do not reach for `requests`/`fetch` in a Python or TypeScript project just because it feels lighter. Never fall back to OpenAI-compatible shims.

**Never guess SDK usage**. Function names, class names, namespaces, method signatures, and import paths must come from explicit documentation. Either the `{lang}/` files in this skill or the official SDK repositories or documentation links listed in `shared/live-sources.md`. The binding you need can be undocumented in the skill files. Then WebFetch the relevant SDK repo from `shared/live-sources.md` before writing code. Do not infer Ruby/Java/Go/PHP/C# APIs from cURL shapes or from another language's SDK.

**If WebFetch or repository access fails** (network restricted, timeouts, clone blocked): do not keep retrying. Write code from the patterns and namespace/package tables in the `{lang}/` file. Run the compiler or interpreter on it, and iterate on the error output. For statically-typed SDKs (C#, Java, Go) a compile-fix loop against local errors reaches working code faster than blocked network research.

## Defaults.

Unless the user requests otherwise:

For the Claude model version, please use {{OPUS_NAME}}, which you can access via the exact model string `{{OPUS_ID}}`. Please default to using adaptive thinking (`thinking: {type: "adaptive"}`) for anything remotely complicated. And finally, please default to streaming for any request that can involve long input, long output, or high `max_tokens`. It prevents hitting request timeouts. Use the SDK's `.get_final_message()` / `.finalMessage()` helper to get the complete response where you do not handle individual stream events.

## ⚠️ API Drift. Your Training Prior Can Be Stale.

Several common Claude API shapes changed in 2025–2026. If you recall a pattern from training, check it against the `{lang}/` files in this skill before writing. The rows below are the most frequent drift points:

| Area | Stale prior | Current API |
|---|---|---|
| Extended thinking | `thinking: {type: "enabled", budget_tokens: N}` | On Claude 4.6+ models: `thinking: {type: "adaptive"}`. `budget_tokens` is deprecated on Opus 4.6 / Sonnet 4.6 and **rejected with a 400** on Fable 5 / Sonnet 5 / Opus 5 / 4.8 / 4.7. Pre-4.6 models still use `budget_tokens`. |
| Web search / web fetch tool type | `web_search_20250305`, `web_fetch_20250910` | `web_search_20260209`, `web_fetch_20260209` (dynamic filtering) on Opus 5/4.8/4.7/4.6, Sonnet 5, and Sonnet 4.6. Older models keep the basic variants. On Vertex AI only basic `web_search_20250305` is available (web fetch is not on Vertex). See the Server Tools QR below. |
| PHP parameter names | snake_case wire names as named args (`max_tokens`) | Top-level named args are camelCase (`maxTokens`). Nested array keys vary by feature (for example `'taskBudget'`, `'skillID'`, `'mcp_server_name'`). Copy the exact key from the documented example. Do not bulk-convert. |
| Managed Agents credentials | Keep secrets host-side via custom tools (the only option before vaults shipped) | Vault `environment_variable` credentials. Stored by Anthropic, substituted at egress, never visible in the sandbox (`shared/managed-agents-tools.md` → Vaults). Host-side custom tools remain the fallback for self-hosted sandboxes. |

The `{lang}/` files in this skill are authoritative over recalled patterns.

---

## Subcommands.

The User Request at the bottom of this prompt can be a bare subcommand string (no prose). Then search every **Subcommands** table in this document. Including any in sections appended below. And follow the matching Action column directly. This lets users invoke specific flows via `/claude-api <subcommand>`. If no table in the document matches, treat the request as normal prose.

| Subcommand | Action |
|---|---|
| `migrate` | Migrate existing Claude API code to a newer model. **Read `shared/model-migration.md` immediately** and follow it in order: Step 0 (confirm scope. Ask which files/directories before any edit), Step 1 (classify each file), then the per-target breaking-changes section. Do not summarize the guide. Execute it. If the user did not name a target model, ask which model to migrate to in the same turn as the scope question. After the per-target changes are applied, audit the in-scope prompt text, tool descriptions, and request code against `shared/prompt-audit.md`. Prompting written for the source model is part of every migration, and it does not announce itself. |
| `prompt-audit` | Audit existing prompts, skills, and tool descriptions for dated patterns ("cruft") written for older models. **Read `shared/prompt-audit.md` immediately** and follow it in order: Step 0 (establish scope and target model from the request and the repository. State the assumptions in the report, do not stop to ask), inventory, provenance, then the pattern scan. Produce both deliverables in full. The audit report (findings with `file:line`, pattern, why it is obsolete for the target model, confidence) and a proposed diff. Without pausing for confirmation. Apply edits only if the request explicitly asked for them. Do not summarize the guide. Execute it. |
<!-- TODO(prompt-audit): remaining trigger question. Whether the skill trigger description must also name auditing directly (it is eval-pinned. Re-validate before changing it). The migrate-row cross-reference above is the no-revalidation half, already applied. -->

---

## Language Detection.

Before reading code examples, determine which language the user is working in (exception: for the `prompt-audit` subcommand, skip this section's ask steps. The audit is non-interactive and its inventory is language-agnostic. When no language is inferable, proceed without asking and state the assumption in the report):

1. **Look at project files** to infer the language:

   - `*.py`, `requirements.txt`, `pyproject.toml`, `setup.py`, `Pipfile` → **Python**. Read from `python/`.
   - `*.ts`, `*.tsx`, `package.json`, `tsconfig.json` → **TypeScript**. Read from `typescript/`.
   - `*.js`, `*.jsx` (no `.ts` files present) → **TypeScript**. JS uses the same SDK, read from `typescript/`.
   - `*.java`, `pom.xml`, `build.gradle` → **Java**. Read from `java/`.
   - `*.kt`, `*.kts`, `build.gradle.kts` → **Java**. Kotlin uses the Java SDK, read from `java/`.
   - `*.scala`, `build.sbt` → **Java**. Scala uses the Java SDK, read from `java/`.
   - `*.go`, `go.mod` → **Go**. Read from `go/`.
   - `*.rb`, `Gemfile` → **Ruby**. Read from `ruby/`.
   - `*.cs`, `*.csproj` → **C#**. Read from `csharp/`.
   - `*.php`, `composer.json` → **PHP**. Read from `php/`.

2. **If multiple languages detected** (for example both Python and TypeScript files):

   - Check which language the user's current file or question relates to.
   - If still ambiguous, ask: "I detected both Python and TypeScript files. Which language are you using for the Claude API integration?"

3. **Where language inference fails** (empty project, no source files, or unsupported language):

   - Use AskUserQuestion with options: Python, TypeScript, Java, Go, Ruby, cURL/raw HTTP, C#, PHP.
   - If AskUserQuestion is unavailable, default to Python examples and note: "Showing Python examples. Let me know if you need a different language."

4. **If unsupported language detected** (Rust, Swift, C++, Elixir, and more):

   - Suggest cURL/raw HTTP examples from `curl/` and note that community SDKs can exist.
   - Offer to show Python or TypeScript examples as reference implementations.

5. **If user needs cURL/raw HTTP examples**, read from `curl/`.

### Language-Specific Feature Support.

Every SDK language above supports both the beta Tool Runner and Managed Agents (beta). Python (`@beta_tool` decorator), TypeScript (`betaZodTool` + Zod), Java (annotated classes), Go (`BetaToolRunner` in the `toolrunner` pkg), Ruby (`BaseTool` + `tool_runner`), C# (`BetaToolRunner` + raw JSON schema), PHP (`BetaRunnableTool` + `toolRunner()`). Code entry points are in the Tool Use Patterns quick reference below. cURL is raw HTTP (no SDK features) and supports Managed Agents.

> **Managed Agents code examples**: see the reading guide in the `## Managed Agents (Beta)` section below.

---

## Which Surface Must I Use?

> **Start simple**. Default to the simplest tier that meets your needs. Single API calls and workflows handle most use cases. Reach for agents only where the task genuinely requires open-ended, model-driven exploration. "Simplest" means the least code you own: for a hosted, scheduled, or memory-backed agent, Managed Agents is the simplest option, even though it is a bigger platform. (No loop code, no state files, no scheduler).

| Use Case                                        | Tier            | Recommended Surface       | Why                                                          |
| ----------------------------------------------- | --------------- | ------------------------- | ------------------------------------------------------------ |
| Classification, summarization, extraction, Q&A  | Single LLM call | **Claude API**            | One request, one response                                    |
| Batch processing or embeddings                  | Single LLM call | **Claude API**            | Specialized endpoints                                        |
| Multi-step pipelines with code-controlled logic | Workflow        | **Claude API + tool use** | You orchestrate the loop                                     |
| Custom agent with your own tools                | Agent           | **Claude API + tool use** | Maximum flexibility                                          |
| Server-managed stateful agent with workspace    | Agent           | **Managed Agents**        | Anthropic runs the loop and hosts the tool-execution sandbox |
| Persisted, versioned agent configs              | Agent           | **Managed Agents**        | Agents are stored objects. Sessions pin to a version         |
| Long-running multi-turn agent with file mounts  | Agent           | **Managed Agents**        | Per-session containers, SSE event stream, Skills + MCP       |
| Agent that runs on a schedule (cron, "every night") | Agent       | **Managed Agents**. Scheduled deployments | Deployments fire sessions autonomously. No client-side scheduler |

> **Note**: Managed Agents is the right choice where you want Anthropic to run the agent loop *and* host the tool-execution container. File ops, bash, code execution all run in the per-session workspace. Where you host the compute yourself or run your own custom tool runtime, choose Claude API + tool use. Use the tool runner for the agentic loop. Its per-turn hooks still give you approval gates, logging, error interception, and conditional execution (see `shared/tool-use-concepts.md`). Or the manual loop where you own the entire loop yourself.

> **Cloud-provider access**. **Claude Platform on AWS** is Anthropic-operated with same-day API parity. See `shared/claude-platform-on-aws.md` for client setup. For per-feature availability on **Claude Platform on AWS**, **Amazon Bedrock**, **Google Vertex AI**, and **Microsoft Foundry**, see `shared/platform-availability.md`. That table is the single source of truth in this skill. Do not infer availability from anywhere else.

### Building an Agent: Four Approaches.

Once you decided you actually need an agent (open-ended, model-driven tool use), there are four distinct ways to build one. Two independent questions separate them: **who supplies the harness** (the agent loop + context management). And **who supplies the deployment** (the infra the agent runs on). The Tool Runner and the Claude Agent SDK both supply a *harness only*. You still host and deploy them yourself. Which is why they are easy to conflate. Managed Agents (CMA) is the only option that supplies **both** the harness *and* managed deployment. The manual loop supplies neither.

| # | Approach | You write | Harness & deployment | Tools available | Use when |
|---|----------|-----------|----------------------|-----------------|----------|
| 1 | **Claude API. Manual loop** | The `while stop_reason == "tool_use"` loop yourself | You build the harness. You host | Only tools you define | You want to own the *entire* loop. No beta dependency, or a control flow the Tool Runner's per-turn hooks do not fit |
| 2 | **Claude API. Tool Runner** (`client.beta.messages.tool_runner` + `@beta_tool` / `betaZodTool`) | Just the tool functions | SDK supplies the loop (**harness only**). You host | Only tools you define | A custom-tool agent without hand-writing the loop (most cases). Per-turn hooks still give you approval gates, error interception, result modification (for example `cache_control`), retries, streaming, and compaction |
| 3 | **Managed Agents** (REST, beta) | Agent config + your tool results | Anthropic supplies the harness **and** hosts a per-session sandbox (**harness + deployment**) | Anthropic-hosted sandbox (bash, files, code exec) + Skills/MCP + your tools | You want Anthropic to run the loop *and* host the per-session workspace. Persisted/versioned configs. Long-running sessions |
| 4 | **Claude Agent SDK** — *separate product* (`claude-agent-sdk` / `@anthropic-ai/claude-agent-sdk`) | A prompt + options | SDK supplies the Claude Code harness + built-in tools (**harness only**). You host | Built-in Read/Write/Edit/Bash/Glob/Grep/WebSearch/WebFetch + MCP + subagents | You want a batteries-included coding/filesystem agent running on your own infra |

The harness/deployment split is the key mental model: options 1, 2, and 4 all **leave deployment to you**. Only option 3 (CMA) adds managed deployment. Options 1–3 are what this skill generates. Option 4 is a different library with its own docs. See the disambiguation below.

> **Tool Runner ≠ Claude Agent SDK**. These sound alike but are different packages:
> - **Tool Runner** is part of the regular Anthropic API SDK (`anthropic` / `@anthropic-ai/sdk`). It is reached via `client.beta.messages.tool_runner`. It automates the request → execute → loop cycle *for tools you define*. No built-in tools, no filesystem access, no sandbox. You supply every tool and host the compute. It is option 2 above, a thin helper over `POST /v1/messages`.
> - **Claude Agent SDK** (`claude-agent-sdk` / `@anthropic-ai/claude-agent-sdk`) is Claude Code packaged as a library. It ships built-in tools (file read/write/edit, bash, grep, web search) and the full agent loop. Also context management, hooks, subagents, permissions, and sessions. You call `query(prompt, options)` and it drives everything.
> 
> Both are **harness-only. You host and deploy them**. The difference is scope of harness: the Tool Runner loops over tools *you* define (with per-turn hooks for approval, interception, result modification, and retries. But no built-in tools). The Agent SDK is the full Claude Code harness with built-in tools. Neither provides managed deployment. That is what **Managed Agents (CMA)** adds (Anthropic hosts the loop and a per-session sandbox).
> 
> **This skill covers the Claude API and Managed Agents (options 1–3). It does not generate Claude Agent SDK code**. If the user actually wants the Claude Agent SDK, point them to its docs (`code.claude.com/docs/en/agent-sdk`). Do not substitute the API Tool Runner for it, or vice-versa.

### Must I Build an Agent?

Before choosing the agent tier, check all four criteria:

- **Complexity** — Is the task multi-step and hard to fully specify in advance? (for example "turn this design doc into a PR" vs. "extract the title from this PDF").
- **Value** — Does the outcome justify higher cost and latency?
- **Viability** — Is Claude capable at this task type?
- **Cost of error**. Can errors be caught and recovered from? (tests, review, rollback).

If the answer is "no" to any of these, stay at a simpler tier (single call or workflow).

---

## Architecture.

Everything goes through `POST /v1/messages`. Tools and output constraints are features of this single endpoint. Not separate APIs.

**User-defined tools** — You define tools (via decorators, Zod schemas, or raw JSON). The SDK's tool runner handles calling the API, executing your functions, and looping until Claude is done. For full control, you can write the loop manually.

**Server-side tools** — Anthropic-hosted tools that run on Anthropic's infrastructure. Code execution is fully server-side (declare it in `tools`, Claude runs code automatically). Computer use can be server-hosted or self-hosted.

**Structured outputs** — Constrains the Messages API response format (`output_config.format`) and/or tool parameter checking (`strict: true`). The recommended approach is `client.messages.parse()` which checks responses against your schema automatically. Note: the old `output_format` parameter is deprecated. Use `output_config: {format: {...}}` on `messages.create()`.

**Supporting endpoints** — Batches (`POST /v1/messages/batches`), Files (`POST /v1/files`), Token Counting (`POST /v1/messages/count_tokens`. See `shared/token-counting.md`), and Models (`GET /v1/models`, `GET /v1/models/{id}`. Live capability/context-window discovery) feed into or support Messages API requests.

---

## Current Models (cached: 2026-06-24).

| Model             | Model ID            | Context        | Input $/1M | Output $/1M |
| ----------------- | ------------------- | -------------- | ---------- | ----------- |
| {{FABLE_NAME}}    | `{{FABLE_ID}}`      | 1M             | $10.00     | $50.00      |
| {{MYTHOS_NAME}} (Project Glasswing only) | `{{MYTHOS_ID}}` | 1M | $10.00     | $50.00      |
| {{OPUS_NAME}}     | `{{OPUS_ID}}`       | 1M             | $5.00      | $25.00      |
| {{PREV_OPUS_NAME}} | `{{PREV_OPUS_ID}}`  | 1M             | $5.00      | $25.00      |
| Claude Opus 4.7   | `claude-opus-4-7`   | 1M             | $5.00      | $25.00      |
| Claude Opus 4.6   | `claude-opus-4-6`   | 1M             | $5.00      | $25.00      |
| Claude Sonnet 5   | `claude-sonnet-5`   | 1M             | $3.00 ($2.00 intro through 2026-08-31) | $15.00 ($10.00 intro) |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | 1M             | $3.00      | $15.00      |
| Claude Haiku 4.5  | `claude-haiku-4-5`  | 200K           | $1.00      | $5.00       |

**Partner pricing:** The prices above are Anthropic first-party API rates. They also apply to Claude on Microsoft Foundry, which is billed through the Microsoft Marketplace at standard API rates. Claude on Amazon Bedrock and Vertex AI is partner-operated with separate pricing. See [Bedrock](https://aws.amazon.com/bedrock/pricing/) or [Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/pricing#claude-models). For WebFetch, use the Pricing row in `shared/live-sources.md`.

**ALWAYS use `{{OPUS_ID}}` unless the user explicitly names a different model**. This is non-negotiable. Do not use `{{SONNET_ID}}`, `{{PREV_SONNET_ID}}`, or another model unless the user literally says "use sonnet" or "use haiku". Never downgrade for cost. That is the user's decision, not yours. Use `{{FABLE_ID}}` only where the user explicitly asks for {{FABLE_NAME}}, "fable", or Anthropic's most capable model. It has different API behavior than the Opus family (see below) and pricing that exceeds Opus-tier. **Use only the exact model ID strings from the table. They are complete as-is. Never append date suffixes** (`claude-sonnet-4-6`, never `claude-sonnet-4-6-20251114` or another date-suffixed variant recalled from training data). The user can request an older model not in the table (for example "opus 4.5", "sonnet 3.7"). Then read `shared/models.md` for the exact ID. Do not construct one yourself.

### {{FABLE_NAME}} (`{{FABLE_ID}}`). Most capable widely released model.

{{FABLE_NAME}} is Anthropic's most capable widely released model, for the most demanding reasoning and long-horizon agentic work. Everything below also applies to **{{MYTHOS_NAME}}** (`{{MYTHOS_ID}}`, Project Glasswing. Same capabilities, pricing, and API surface. Successor to the invitation-only `claude-mythos-preview`). 1M context window (the maximum is also the default), 128K max output. Key API differences from Opus-tier. See `shared/model-migration.md` → Migrating to {{FABLE_NAME}} for details:

- **Thinking is always on**. Omit the `thinking` parameter entirely (or send `{type: "adaptive"}`). Any other explicit config is rejected: `{type: "disabled"}` and `{type: "enabled", budget_tokens: N}` both return a 400. Control depth with `output_config.effort` (supports `low` through `xhigh` and `max`).
- **The raw chain of thought is never returned**. Responses carry regular `thinking` blocks (not `redacted_thinking`): `display: "summarized"` returns a readable summary, `"omitted"` (the default) leaves the `thinking` field as an empty string. Replay rules: pass thinking blocks back unchanged on the same model. Other models drop them silently (unbilled. Nothing to strip). Details in `shared/model-migration.md`.
- **Tokenizer** — same tokenizer as Opus 4.8 (introduced with Opus 4.7). Token counts are roughly unchanged where migrating from Opus 4.7/4.8. Per-token pricing differs. Coming from Opus 4.6, Sonnet, Haiku, or older, re-baseline with `count_tokens` (the Opus 4.7 tokenizer uses ~1×–1.35× as many tokens).
- **`refusal` stop reason. Handle it, and opt into fallbacks by default**. Safety classifiers can decline a request (HTTP 200, `stop_reason: "refusal"`, with a `stop_details` category). Always check `stop_reason` before reading `content`. **When you write `{{FABLE_ID}}` or `{{OPUS_ID}}` code, include the server-side `fallbacks` parameter by default**. Simplest form: `betas: ["server-side-fallback-2026-07-01"]` + `fallbacks: "default"`, which routes by refusal category so you never maintain a model list. (The older array form — `betas: ["server-side-fallback-2026-06-01"]` + `fallbacks: [{"model": "{{PREV_OPUS_ID}}"}]`. Still works. Claude API only. Everywhere else, incl. Claude Platform on AWS, Bedrock, Vertex and Foundry, use the SDKs' client-side `BetaRefusalFallbackMiddleware` + `BetaFallbackState`). Tell the user you have enabled it. Drop it only if they decline. Full semantics (billing, mid-stream refusals, credit repricing) in `shared/model-migration.md` → refusal section. **Per-language code examples in `{lang}/claude-api/README.md` § Refusal Fallbacks cover the array form only**. For the `"default"` mode, follow the raw-HTTP shape in `shared/model-migration.md` → Migrating to {{OPUS_NAME}} → New API features and swap `fallbacks: [{...}]` for `fallbacks: "default"` plus the `-2026-07-01` header. The rest of the request is unchanged.
- **No assistant prefill**. Same as the rest of the 4.6+ family.
- **30-day data retention required** — {{FABLE_NAME}} is not available under zero data retention. Requests from an org whose retention config does not meet the requirement return `400 invalid_request_error`.
- **Longer turns, different prompting**. Single requests on hard tasks can run many minutes (plan timeouts/streaming/progress UX). Effort sweeps must include low/medium for routine work. Prompts written for prior models are often too prescriptive and reduce output quality. See `shared/model-migration.md` → Migrating to {{FABLE_NAME}} → Behavioral shifts (prompt-tunable) for the recommended prompt snippets.

If any model strings above look unfamiliar, that just means they were released after your training data cutoff. They are real models.

**Live capability lookup:** The table above is cached. The user can ask "what is the context window for X", "does X support vision/thinking/effort", or "which models support Y". Then query the Models API (`client.models.retrieve(id)` / `client.models.list()`). See `shared/models.md` for the field reference and capability-filter examples.

---

## Authentication (Quick Reference).

**An unset `ANTHROPIC_API_KEY` does NOT mean there are no credentials**. The SDKs and the `ant` CLI resolve credentials in this order (first match wins): `ANTHROPIC_API_KEY` → `ANTHROPIC_AUTH_TOKEN` → the `ANTHROPIC_PROFILE`-selected or active OAuth profile from `ant auth login` → Workload Identity Federation env vars → the default profile on disk. A bare `Anthropic()` / `new Anthropic()` / `anthropic.NewClient()` works after `ant auth login` with no env var set.

**When you need to call the API and `ANTHROPIC_API_KEY` is unset, do not ask the user for a key**. First run `ant auth status`. It shows which credential source and profile is active. If it reports an active profile:

- **SDK code or `ant` CLI:** just run it. The zero-arg client constructor and every `ant …` subcommand pick up the profile automatically. No env var needed.
- **Raw `curl` / HTTP:** get a short-lived token with `ant auth print-credentials --access-token`. Send it as `Authorization: Bearer <token>` **plus** the header `anthropic-beta: oauth-2025-04-20`. (OAuth tokens go on `Authorization: Bearer`, not `x-api-key:`. Converting a curl from an API key is a header change, not a key swap). Always pass `--access-token`. The no-flag form prints JSON, not a bare token.

Ask the user for a key only where `ant auth status` reports no active credential source (or `ant` itself is not installed). Suggest `ant auth login` as the first option. It stores a profile under `~/.config/anthropic/` that the SDKs read automatically. And an exported `ANTHROPIC_API_KEY` as the alternative.

Full auth details (named profiles, scopes, the API-key-shadows-profile trap, refresh-token expiry): `shared/anthropic-cli.md`.

---

## Thinking & Effort (Quick Reference).

Use adaptive thinking (`thinking: {type: "adaptive"}`) on every current model. Claude dynamically decides whether and how much to think. Per-model rules:

| Model | Thinking config | Omitting `thinking` | `budget_tokens` | Sampling (`temperature`/`top_p`/`top_k`) | Effort levels |
|---|---|---|---|---|---|
| Fable 5 | `{type: "adaptive"}` or omit. Explicit `{type: "disabled"}` returns 400. Omit the param instead | Runs adaptive (thinking is always on) | Removed — `{type: "enabled", budget_tokens: N}` returns 400 | Removed — 400 | `low`/`medium`/`high`/`xhigh`/`max` |
| {{OPUS_NAME}} | `{type: "adaptive"}` or omit. `{type: "disabled"}` accepted **only at effort `high` or below** — 400 at `xhigh`/`max`, and see the disabled-thinking pitfall below | Runs **adaptive** (thinking is on by default. Unlike Opus 4.8/4.7) | Removed — 400 | Removed — 400 | `low`–`max` (all five) |
| Opus 4.8 / 4.7 | `{type: "adaptive"}` is the only on-mode. `{type: "disabled"}` accepted | Runs **without** thinking. Set `{type: "adaptive"}` explicitly | Removed — 400 | Removed — 400 | `low`/`medium`/`high`/`xhigh`/`max` |
| Sonnet 5 | `{type: "adaptive"}` is the only on-mode. `{type: "disabled"}` accepted | Runs adaptive | Removed — 400 | Removed — 400 | `low`/`medium`/`high`/`xhigh`/`max` |
| Opus 4.6 / Sonnet 4.6 | `{type: "adaptive"}` (recommended. Auto-enables interleaved thinking, no beta header) | Set `{type: "adaptive"}` explicitly | Deprecated. Do not use in new code. Transitional escape hatch only (see below) | Allowed | `low`/`medium`/`high`/`max` (`xhigh` arrived with Opus 4.7) |
| Older (Sonnet 4.5, Haiku 4.5, …). Only if explicitly requested | `{type: "enabled", budget_tokens: N}` | No thinking | Required for thinking. Must be less than `max_tokens`, minimum 1024. Errors otherwise | Allowed | `effort` works on Opus 4.5 (`low`/`medium`/`high` only. No `xhigh`/`max`). Errors on Sonnet 4.5 / Haiku 4.5 |

Opus 4.8 keeps the same request surface as 4.7 (no new breaking changes). See `shared/model-migration.md` → Migrating to Opus 4.8 for the behavioral re-tuning. And → Migrating to Opus 4.7 for the full breaking-change list where coming from 4.6 or earlier. With `thinking` disabled, Opus 4.8 can write longer reasoning into the visible response. Leave adaptive thinking on, or add a final-answer-only instruction (see the migration guide).

- **Effort (GA, no beta header):** `output_config: {effort: "low"|"medium"|"high"|"xhigh"|"max"}`. Inside `output_config`, not top-level. Default `high` (equivalent to omitting it). Controls thinking depth and overall token spend. Combine with adaptive thinking for the best cost-quality tradeoffs. `xhigh` (added on Opus 4.7, between `high` and `max`) is the best setting for most coding and agentic use cases on Fable 5 / Opus 4.7/4.8 / Sonnet 5, and the default in Claude Code. Effort matters more on those models than on any prior model in their tier. Re-tune it when migrating, and run long-horizon/agentic tasks at `high`/`xhigh` with the full task spec given up front. Use a minimum of `high` for intelligence-sensitive work, `max` when correctness matters more than cost, and `low` for subagents or simple tasks. Lower effort means fewer and more-consolidated tool calls, less preamble, and terser confirmations (`high` is often the sweet spot balancing quality and token efficiency).
- **Thinking display is `"omitted"` by default on Fable 5 / Mythos 5 / Opus 5 / 4.8 / 4.7 / Sonnet 5.** `display: "summarized"` returns a readable summary of the reasoning. `"omitted"` (the default on all six. A silent change from Opus 4.6 and Sonnet 4.6, where it was `"summarized"`) streams `thinking` blocks with empty text. `display` controls visibility only. Thinking happens and is billed the same under every setting. The raw chain of thought is never exposed on any model. If you stream reasoning to users, the default looks like a long pause before output. Set `thinking: {type: "adaptive", display: "summarized"}` explicitly. (Independent of display, echo thinking blocks back unchanged where continuing on the same model. Other models silently ignore them. See the migration guide.)
- **Where the user asks for "extended thinking", a "thinking budget", or `budget_tokens`**: always use Fable 5, Opus 5, 4.8, 4.7, or 4.6. Set `thinking: {type: "adaptive"}`. The fixed thinking-token-budget concept is deprecated and adaptive thinking replaces it. Do NOT use `budget_tokens` for new 4.6/4.7/4.8 code. And do NOT switch to an older model just because the user mentions it. *Gradual-migration carve-out:* `budget_tokens` is still functional on Opus 4.6 and Sonnet 4.6 only. It is a transitional escape hatch for existing code that needs a hard token ceiling before you tuned `effort`. See `shared/model-migration.md` → Transitional escape hatch. It is fully removed on Fable 5, Opus 5/4.7/4.8, and Sonnet 5.

---

## Compaction (Quick Reference).

**Beta, Fable 5, Opus 5, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 5, and Sonnet 4.6**. For long-running conversations that can exceed the 1M context window, enable server-side compaction. The API automatically summarizes earlier context once it approaches the trigger threshold (default: 150K tokens). Requires beta header `compact-2026-01-12`.

**Critical:** Append `response.content` (not just the text) back to your messages on every turn. Compaction blocks in the response must be preserved. The API uses them to replace the compacted history on the next request. Extracting only the text string and appending that will silently lose the compaction state.

See `{lang}/claude-api/README.md` (Compaction section) for code examples. Full docs via WebFetch in `shared/live-sources.md`.

---

## Prompt Caching (Quick Reference).

**Prefix match**. Any byte change anywhere in the prefix invalidates everything after it. Render order is `tools` → `system` → `messages`. Keep stable content first (frozen system prompt, deterministic tool list). Put volatile content (timestamps, per-request IDs, varying questions) after the last `cache_control` breakpoint.

**Mid-conversation operator instructions** ({{OPUS_NAME}}, {{PREV_OPUS_NAME}}, {{FABLE_NAME}}, {{MYTHOS_NAME}}. Not {{SONNET_NAME}}. No beta header): append `{"role": "system", ...}` to `messages[]` instead of editing top-level `system`. Preserves the cached history prefix and is the prompt-injection-safe operator channel. See `shared/prompt-caching.md` § Mid-conversation system messages.

**Top-level auto-caching** (`cache_control: {type: "ephemeral"}` on `messages.create()`) is the simplest option where you do not need fine-grained placement. Max 4 breakpoints per request. Minimum cacheable prefix is ~1024 tokens. Shorter prefixes silently will not cache.

**Check `usage.cache_read_input_tokens`**. Where it is zero across repeated requests, a silent invalidator is at work. Examples: `datetime.now()` in system prompt, unsorted JSON, varying tool set.

For placement patterns, architectural guidance, and the silent-invalidator audit checklist: read `shared/prompt-caching.md`. Language-specific syntax: `{lang}/claude-api/README.md` (Prompt Caching section).

---

## Fast Mode (Quick Reference).

**Research preview, {{OPUS_NAME}} / Opus 4.8 only**. Claude API and Managed Agents, not Bedrock / Google Cloud / Foundry. Opus 4.7 fast mode is removed: `speed: "fast"` on 4.7 returns an error. Fast mode on {{OPUS_NAME}} is priced at $10 / $50 per MTok. Fast mode runs the same model at up to 2.5x higher output tokens per second, at premium pricing. Three things are required on every request: use the **beta** messages endpoint (`client.beta.messages.…`) and pass the beta flag `fast-mode-2026-02-01`. Set `speed: "fast"` as a top-level request parameter (not a header, not in `extra_body`).

```python
client.beta.messages.create(
    model="{{OPUS_ID}}", max_tokens=4096,
    speed="fast", betas=["fast-mode-2026-02-01"],
    messages=[...],
)
```

| Language | Beta flag | Speed parameter |
|---|---|---|
| Python | `betas=["fast-mode-2026-02-01"]` | `speed="fast"` |
| TypeScript / Ruby | `betas: ["fast-mode-2026-02-01"]` | `speed: "fast"` |
| Go | `[]anthropic.AnthropicBeta{anthropic.AnthropicBetaFastMode2026_02_01}` | `Speed: anthropic.BetaMessageNewParamsSpeedFast` |
| Java | `.addBeta(AnthropicBeta.FAST_MODE_2026_02_01)` | `.speed(MessageCreateParams.Speed.FAST)` |
| C# | `Betas = ["fast-mode-2026-02-01"]` | `Speed = Speed.Fast` (`Anthropic.Models.Beta.Messages`) |
| PHP | `betas: ['fast-mode-2026-02-01']` | `speed: 'fast'` |
| cURL | `anthropic-beta: fast-mode-2026-02-01` header | `"speed": "fast"` in body |

`response.usage.speed` reports which speed was used. Fast mode has its own rate limit separate from standard Opus. On 429, either retry after the `retry-after` delay or drop `speed` and fall back to standard (note: switching speed invalidates prompt cache). Not available with Batch API, Priority Tier, Claude Platform on AWS, or third-party platforms.

**Priority Tier does not cover {{OPUS_NAME}}**. It is supported on every other current model, including {{FABLE_NAME}} and Opus 4.8. But {{OPUS_NAME}}, {{SONNET_NAME}}, {{MYTHOS_NAME}}, and Mythos Preview are excluded. A Priority Tier request naming one of them is rejected.

---

## Task Budgets (Quick Reference).

**Beta, {{OPUS_NAME}} / Fable 5 / Sonnet 5 / Opus 4.8 / 4.7**. A task budget gives Claude a token ceiling for an agentic loop so it paces itself and finishes gracefully instead of being cut off. Distinct from `max_tokens`, which is an enforced per-response ceiling the model is not aware of. Minimum `total`: 20,000. Set `task_budget` inside `output_config` on `client.beta.messages.stream(...)` with beta flag `task-budgets-2026-03-13`. Use streaming so the large `max_tokens` does not hit HTTP timeouts (full details: `shared/model-migration.md` → Task Budgets):

```python
with client.beta.messages.stream(
    model="{{OPUS_ID}}", max_tokens=128000,
    output_config={"effort": "high", "task_budget": {"type": "tokens", "total": 64000}},
    betas=["task-budgets-2026-03-13"],
    messages=[...], tools=[...],
) as stream:
    response = stream.get_final_message()
```

`task_budget` fields: `type` (always `"tokens"`), `total`, and optional `remaining` (defaults to `total`). The server injects a countdown marker Claude sees during generation. The budget counts what Claude generates and the tool results it reads this turn. **Not** the full history you resend each request. Not the same thing as **Managed Agents session budgets**. Those are hard, dollar-denominated, platform-enforced caps on one CMA session (`shared/managed-agents-core.md` § Session budgets). A task budget is advisory and token-denominated.

**Observing spend:** to display progress, accumulate `response.usage.output_tokens` across loop iterations. Add the token count of the tool-result blocks you append. Leave `remaining` unset in the normal loop. The server tracks the countdown itself, and passing a client-computed `remaining` while also resending full history under-reports the budget. **Pass `remaining` only** where you compact or rewrite history between requests and the server can no longer derive prior spend.

---

## Provider Clients (Quick Reference).

When targeting Claude on a third-party platform, use that platform's dedicated client class. Not the first-party `Anthropic()` client with a `base_url` override. After construction the client exposes the same `messages.create` / `.stream` surface as the first-party SDK.

### Amazon Bedrock.

Use the **Mantle** client (Messages-API Bedrock endpoint). Bedrock model IDs take an `anthropic.` prefix (for example `"anthropic.{{OPUS_ID}}"`). Region is required.

| Language | Client |
|---|---|
| Python | `from anthropic import AnthropicBedrockMantle` → `AnthropicBedrockMantle(aws_region="…")` |
| TypeScript | `import { AnthropicBedrockMantle } from "@anthropic-ai/bedrock-sdk"` → `new AnthropicBedrockMantle({ awsRegion: "…" })` |
| Go | `bedrock.NewMantleClient(ctx, bedrock.MantleClientConfig{ AWSRegion: "…" })` |
| Java | `AnthropicOkHttpClient.builder().backend(BedrockMantleBackend.fromEnv()).build()` (from `com.anthropic.bedrock.backends`) |
| C# | `new AnthropicBedrockMantleClient(new() { AwsRegion = "…" })` (package `Anthropic.Bedrock`) |
| PHP | `use Anthropic\Bedrock\MantleClient;` → `new MantleClient(awsRegion: '…')` |
| Ruby | `Anthropic::BedrockMantleClient.new(aws_region: "…")` |

`AnthropicBedrock` / `BedrockClient` / `BedrockBackend` (without `Mantle`) are the legacy `bedrock-runtime` InvokeModel path. Prefer the Mantle client for new code.

### Microsoft Foundry.

| Language | Client |
|---|---|
| Python | `from anthropic import AnthropicFoundry` → `AnthropicFoundry(api_key=…, resource="…")` |
| TypeScript | `import AnthropicFoundry from "@anthropic-ai/foundry-sdk"` → `new AnthropicFoundry({ … })` |
| Java | `AnthropicOkHttpClient.builder().backend(FoundryBackend.fromEnv()).build()` (from `com.anthropic.foundry.backends`) |
| C# | `new AnthropicFoundryClient(new AnthropicFoundryApiKeyCredentials(…))` (package `Anthropic.Foundry`) |
| PHP | `Foundry\Client::withCredentials(…)` |

The Go and Ruby SDKs do not currently support Foundry. For Ruby, use the standard `Anthropic::Client.new(base_url: "<foundry endpoint>")` as a fallback (Entra ID auth is not built in). For Claude Platform on AWS, see `shared/claude-platform-on-aws.md`.

### Google Cloud Vertex AI.

Two required constructor args: GCP `project_id` and `region`. Vertex model IDs take **no prefix**. Current-generation models (Opus 4.8/4.7/4.6, Sonnet 5, Sonnet 4.6) use the bare first-party ID (for example `"{{OPUS_ID}}"`). Dated-snapshot models use an `@` version separator (for example `claude-opus-4-5@20251101`, **not** `claude-opus-4-5-20251101`). Auth is GCP ADC (`gcloud auth application-default login`). No Anthropic API key. `region` can be `"global"` (recommended), a multi-region (`"us"`/`"eu"`), or a specific region. After construction, use the same `messages.create` / `.stream` surface.

| Language | Client |
|---|---|
| Python | `from anthropic import AnthropicVertex` → `AnthropicVertex(project_id="…", region="…")` (install `"anthropic[vertex]"`) |
| TypeScript | `import { AnthropicVertex } from "@anthropic-ai/vertex-sdk"` → `new AnthropicVertex({ projectId, region })` |
| Go | `import "github.com/anthropics/anthropic-sdk-go/vertex"` → `anthropic.NewClient(vertex.WithGoogleAuth(ctx, region, projectID))` |
| Java | `AnthropicOkHttpClient.builder().backend(VertexBackend.builder().region("…").project("…").build()).build()` (from `com.anthropic.vertex.backends`) |
| C# | `new AnthropicClient { Backend = new VertexBackend(projectId, region) }` (package `Anthropic.Vertex`) |
| PHP | `use Anthropic\Vertex;` → `Vertex\Client::fromEnvironment(location: '…', projectId: '…')`. Note `location`, not `region` |
| Ruby | `Anthropic::VertexClient.new(region: "…", project_id: "…")` |

---

## Context Editing (Quick Reference).

**Beta**. Context editing **clears** old tool results or thinking blocks from the conversation before the model sees it. It is **not compaction** (which summarizes). On `client.beta.messages.*` with beta `context-management-2025-06-27`, pass `context_management.edits` with a strategy type:

```python
client.beta.messages.create(
    model="{{OPUS_ID}}", max_tokens=4096,
    betas=["context-management-2025-06-27"],
    context_management={"edits": [{"type": "clear_tool_uses_20250919"}]},
    tools=[...], messages=[...],
)
```

Strategy types: `clear_tool_uses_20250919` (clears old tool results. Optional `clear_tool_inputs: true` also clears the tool_use params) and `clear_thinking_20251015` (clears thinking blocks). Do **not** use `compact_20260112` or beta `compact-2026-01-12`. Those are the separate compaction feature.

---

## Mid-Conversation System Messages (Quick Reference).

**{{OPUS_NAME}}, {{PREV_OPUS_NAME}}, {{FABLE_NAME}}, and {{MYTHOS_NAME}}. Not {{SONNET_NAME}}. No beta header**. Append `{"role": "system", "content": "…"}` to the `messages` array (not the top-level `system` field) to add an operator instruction mid-conversation without invalidating the cached prefix. Use the regular `client.messages.create`. There is no beta. A mid-conversation system message must follow a `user` message (or an `assistant` message ending in server-tool use), and must be either the last entry in `messages` or be followed by an `assistant` turn. It cannot be `messages[0]`. Availability: `shared/platform-availability.md`. See `shared/prompt-caching.md` § Mid-conversation system messages.

---

## Managed Agents (Beta).

**Managed Agents** is a third surface: server-managed stateful agents with Anthropic-hosted tool execution. You create a persisted, versioned Agent config (`POST /v1/agents`), then start Sessions that reference it. Each session provisions a container as the agent's workspace. Bash, file ops, and code execution run there. The agent loop itself runs on Anthropic's orchestration layer and acts on the container via tools. The session streams events. You send messages and tool results back.

Availability: `shared/platform-availability.md`. For agents on Bedrock / Vertex / Foundry (where Managed Agents is unsupported), use Claude API + tool use.

**Mandatory flow:** Agent (once) → Session (every run). `model`/`system`/`tools` live on the agent, never the session. See `shared/managed-agents-overview.md` for the full reading guide, beta headers, and pitfalls.

**Beta headers:** `managed-agents-2026-04-01`. The SDK sets this automatically for all `client.beta.{agents,environments,sessions,vaults,memory_stores,deployments,deployment_runs}.*` calls. Skills API uses `skills-2025-10-02` and Files API uses `files-api-2025-04-14`. But you do not need to explicitly pass those in for endpoints other than `/v1/skills` and `/v1/files`.

**Subcommands** — invoke directly with `/claude-api <subcommand>`:

| Subcommand | Action |
|---|---|
| `managed-agents-onboard` | Walk the user through setting up a Managed Agent from scratch. **Read `shared/managed-agents-onboarding.md` immediately** and follow its interview script: **describe → configure the agent (propose, do not interrogate) → environment → session** (same arc as the Console quickstart, auth deferred to the session step). Defaults and inline suggestions do the work, with a silent viability gate (job vs tools/credentials/data) before any code is emitted. Do not summarize. Run the interview. |

**Reading guide:** Start with `shared/managed-agents-overview.md`, then the topical `shared/managed-agents-*.md` files (core, environments, tools, events, outcomes, multiagent, webhooks, memory, scheduled-deployments, client-patterns, onboarding, api-reference). For Python, TypeScript, Go, Ruby, PHP, and Java, read `{lang}/managed-agents/README.md` for code examples. For cURL, read `curl/managed-agents.md`. **Agents are persistent. Create once, reference by ID**. Define agents and environments as version-controlled YAML applied with the `ant` CLI. This is the recommended flow (see `shared/anthropic-cli.md`): the CLI owns the control plane (creating and updating agents), your code owns the data plane (`sessions.create` with the stored agent ID). Call `agents.create()` in code only when you must provision programmatically. Either way, store the returned agent ID and pass it to every subsequent `sessions.create`. Never call `agents.create()` in the request path. If a binding you need is not shown in the language README, WebFetch the relevant entry from `shared/live-sources.md` rather than guess. C# has beta Managed Agents support via `client.Beta.Agents` and related namespaces. See `csharp/claude-api/README.md` for details, or `curl/managed-agents.md` for raw HTTP reference.

**Where the user wants to set up a Managed Agent from scratch** (for example "how do I get started", "walk me through creating one", "set up a new agent"): read `shared/managed-agents-onboarding.md` and run its interview. Same flow as the `managed-agents-onboard` subcommand.

**When the user asks "how do I write the client code for X":** reach for `shared/managed-agents-client-patterns.md`. Covers lossless stream reconnect, `processed_at` queued/processed gate, interrupt, and the `tool_confirmation` round-trip. Also the correct idle/terminated break gate, post-idle status race, stream-first ordering, file-mount gotchas, and more. For credentials, lead with vault `environment_variable` credentials. The first-class mechanism. Secrets are substituted at egress and never enter the sandbox (`shared/managed-agents-tools.md` → Vaults). Keeping credentials host-side via custom tools is the fallback where vault credentials do not fit (for example self-hosted sandboxes).

**When the user wants the agent to run on a schedule** (cron, "every night", "weekly report"): read `shared/managed-agents-scheduled-deployments.md`. Deployments fire sessions autonomously on a cron cadence, with per-firing run records and lifecycle controls (pause/unpause/archive).

**Where the agent's work fans out or one loop fills its context with reading**: read `shared/managed-agents-multiagent.md`. Fan-out examples: research across several sources, per-file or per-record work, "look into N things, then summarize". Recommend a multiagent session. Start with just `{"type": "self"}` in the roster so the agent can delegate to copies of itself. Then move reading-heavy sub-tasks to a cheaper worker agent (for example {{HAIKU_NAME}}) referenced by ID.

---

## Server Tools (Quick Reference).

Server-side tools run on Anthropic's infrastructure. No client-side execution loop. Declare in `tools`. Results arrive as content blocks in the same response. **No beta header** unless noted. **Prefer the latest type variant your model supports**. The `_20260209` web search / web fetch variants below (dynamic filtering) require Opus 5/4.8/4.7/4.6, Sonnet 5, or Sonnet 4.6. The basic variants for older models are listed after the table.

| Tool | `type` | `name` | Key optional params | Result block type |
|---|---|---|---|---|
| Web search | `web_search_20260209` | `web_search` | `max_uses`, `allowed_domains`/`blocked_domains`, `user_location` | `web_search_tool_result` → `.content` is a list of `web_search_result` |
| Web fetch | `web_fetch_20260209` | `web_fetch` | `max_uses`, `allowed_domains`/`blocked_domains`, `citations`, `max_content_tokens` | `web_fetch_tool_result` → `.content` is a `web_fetch_result` with a `document` block |
| Code execution | `code_execution_20260521` | `code_execution` | none | `bash_code_execution_tool_result` → `.content.stdout` / `.stderr` / `.return_code` |
| Tool search (regex) | `tool_search_tool_regex_20251119` | `tool_search_tool_regex` | mark other tools `defer_loading: true` | `tool_search_tool_result` |
| Tool search (BM25) | `tool_search_tool_bm25_20251119` | `tool_search_tool_bm25` | mark other tools `defer_loading: true` | `tool_search_tool_result` |

`web_search_20260209` / `web_fetch_20260209` have built-in dynamic filtering. Code execution runs under the hood, so do **not** separately declare `code_execution` in `tools` (a second execution environment confuses the model). For models older than Opus 4.6 / Sonnet 4.6, use the basic variants `web_search_20250305` / `web_fetch_20250910` instead. On Vertex AI only basic `web_search_20250305` is available. `code_execution_20260120` (REPL persistence + programmatic tool calling) runs on Opus 4.5+ / Sonnet 4.5+. **Go SDK only**: `code_execution_20260521` lives under `client.Beta.Messages.New` with `Betas: []anthropic.AnthropicBeta{"code-execution-2025-08-25"}` (other languages use plain `client.messages.create`). `code_execution_20260120` uses the non-beta `client.Messages.New` in Go like everywhere else. Web fetch only fetches URLs already present in the conversation. Provider availability varies by tool. See `shared/platform-availability.md`. See `shared/tool-use-concepts.md` for `pause_turn` handling.

## Document & File Input (Quick Reference).

**PDF (base64, no beta):** `{"type": "document", "source": {"type": "base64", "media_type": "application/pdf", "data": <b64 string>}}` in user content, placed before the text block. Base64 string must have no newlines. Limits: 32 MB request, 600 pages (100 for 200k-context models). Java: `ContentBlockParam.ofDocument(DocumentBlockParam... Base64PdfSource.builder().data(...))`.

**Files API (beta `files-api-2025-04-14`):** upload via `client.beta.files.upload(...)` → response `id` is the `file_id`. Reference it as `{"type": "document", "source": {"type": "file", "file_id": "..."}}` for PDF/text, or `{"type": "image", ...}` for images. The content-block type must match the file's MIME type. The beta header is required on **both** the upload and the `messages.create` that references the file. Availability: `shared/platform-availability.md`.

**Citations (no beta):** set `citations: {enabled: true}` on each `document` content block (all or none). Response splits into multiple `text` blocks. Cited blocks carry a `citations` array. Each citation has `cited_text`, `document_index`, `document_title`, and a location by `type`: `char_location` (`start_char_index`/`end_char_index`) for plain text, `page_location` (`start_page_number`/`end_page_number`, 1-indexed) for PDF, `content_block_location` for custom content. Incompatible with `output_config.format` (returns a 400).

## Tool Use Patterns (Quick Reference).

**Strict tool use (no beta):** set `strict: true` as a top-level field on the tool definition (alongside `name`/`description`/`input_schema`), **not** on `tool_choice`. Schema must have `additionalProperties: false` + `required`. Guarantees `tool_use.input` validates exactly. Go: `Strict: anthropic.Bool(true)` + `additionalProperties` via `InputSchema.ExtraFields`. Java: `.strict(true)` + `.putAdditionalProperty("additionalProperties", JsonValue.from(false))`.

**Parallel tool use (default on):** one assistant message can contain multiple `tool_use` blocks. Execute them concurrently, then return **all** `tool_result` blocks in a **single** user message. Splitting them across multiple messages silently trains Claude to stop making parallel calls. For a failed tool, return `tool_result` with `is_error: true`. Do not drop it.

**Tool Runner (SDK beta helper):** drives the tool-call loop for you via `client.beta.messages.*`. Python: `@beta_tool` decorator + `client.beta.messages.tool_runner(...)` → `runner.until_done()`. TypeScript: `betaZodTool({...})` from `@anthropic-ai/sdk/helpers/beta/zod` + `client.beta.messages.toolRunner(...)` → `await runner`. Go: `toolrunner.NewBetaToolFromJSONSchema(...)` + `client.Beta.Messages.NewToolRunner(...)` → `.RunToCompletion(ctx)`. Java requires `.addBeta("structured-outputs-2025-11-13")`. Ruby: `Anthropic::BaseTool` subclass + `client.beta.messages.tool_runner(...)`. PHP: `BetaRunnableTool` + `->toolRunner(...)`. C#: raw JSON-schema tools + `BetaToolRunner` via `client.Beta.Messages.ToolRunner(...)`.

**Programmatic tool calling (no beta header):** Claude calls your custom tool from inside code execution. Add `{"type": "code_execution_20260120", "name": "code_execution"}` **and** set `"allowed_callers": ["code_execution_20260120"]` on your custom tool. Opus 4.5+ / Sonnet 4.5+ (availability: `shared/platform-availability.md`). When responding to a pending programmatic call, the user message must contain **only** `tool_result` blocks (no text). Not compatible with `strict: true`, `disable_parallel_tool_use`, forced `tool_choice`, or MCP tools.

## Other API Surfaces (Quick Reference).

**Message Batches (no beta. Availability: `shared/platform-availability.md`):** `client.messages.batches.create(requests=[{custom_id, params}, ...])` → poll `client.messages.batches.retrieve(id).processing_status` until `"ended"` → stream `client.messages.batches.results(id)`. Each result has `.custom_id` + `.result.type` (`succeeded`/`errored`/`canceled`/`expired`). On success read `.result.message.content`. Python wraps requests as `Request(custom_id=..., params=MessageCreateParamsNonStreaming(...))`. Results arrive in **any order**. Key by `custom_id`, never by position.

**Models API (no beta. Availability: `shared/platform-availability.md`):** `client.models.list()` (auto-paginates) and `client.models.retrieve("{{OPUS_ID}}")`. Each model object has `id`, `display_name`, `created_at`, and. Since Mar 2026 — `max_input_tokens` (the context window), `max_tokens` (the output cap), and `capabilities`. There is no `context_window` field.

**Stop details (GA, Opus 4.7+):** `response.stop_details` is populated **only when `stop_reason == "refusal"`** (fields: `type: "refusal"`, `category`. An open set, for example `"cyber"`, `"bio"`, `"reasoning_extraction"`, `"frontier_llm"`, or `null`. See the docs for the full list. And `explanation`). It is `null` for every other `stop_reason` (`end_turn`, `max_tokens`, `tool_use`, `pause_turn`, …). Always guard before reading.

**Client config (no beta):** `timeout` default 10 min; **units differ by SDK**. Python/Ruby: seconds. TypeScript: **milliseconds**. Go `option.WithRequestTimeout(time.Duration)`. Java `Duration`. C# `TimeSpan`. TS scales the default up to 60 min for large `max_tokens` on non-streaming requests. Java does so for streaming requests (Java non-streaming scales 30s–10 min). `max_retries`/`maxRetries` default 2 (retries 408/409/429/5xx + connection errors). `base_url` (or `ANTHROPIC_BASE_URL` env). Per-request override: Python `client.with_options(timeout=5.0).messages.create(...)`. TS `client.messages.create({...}, {timeout: 5_000})`. Ruby `request_options: {timeout: 5}`. Timeouts are retried. Wall-clock can reach `timeout × (max_retries+1)`.

## Workload Identity Federation (Quick Reference).

**GA, no beta header**. Construct the normal zero-arg client (`Anthropic()` / `new Anthropic()` / `anthropic.NewClient()` / `AnthropicOkHttpClient.fromEnv()`). The SDK auto-detects WIF when **all** of `ANTHROPIC_FEDERATION_RULE_ID`, `ANTHROPIC_ORGANIZATION_ID`, `ANTHROPIC_SERVICE_ACCOUNT_ID`, and `ANTHROPIC_IDENTITY_TOKEN_FILE` (or `ANTHROPIC_IDENTITY_TOKEN`) are set, exchanges the JWT at `/v1/oauth/token`, and auto-refreshes. `ANTHROPIC_WORKSPACE_ID` does not gate activation. Required only when the federation rule spans multiple workspaces (else 400 `workspace_id_required`), optional for single-workspace rules. `ANTHROPIC_API_KEY` or `ANTHROPIC_AUTH_TOKEN` (even empty) outrank WIF, and a set `ANTHROPIC_PROFILE` also wins over the federation env vars (a missing named profile is an error, not a fall-through). Unset all three.

---

## Reading Guide.

After detecting the language, read the relevant files based on what the user needs. Every `{lang}/…`, `shared/…`, and `curl/…` path cited in this document is relative to this skill's base directory. None of those files' content is included above. Read each one on demand before relying on what it covers.

**All SDK languages use the same multi-file layout**. Directory `{lang}/claude-api/` containing `README.md` (install, client init, basic request, thinking, caching, stop details, misc), `tool-use.md` (tool definitions, agentic loop, Anthropic-defined tools, structured outputs), `streaming.md`, `batches.md`, `files-api.md`. Not every language has every file (for example Ruby has no `batches.md`). If a file is absent, that feature's example is not yet documented for that language. Fall back to the cURL shape or WebFetch the SDK repo from `shared/live-sources.md`. **cURL** → `curl/examples.md`.

The Quick Task Reference below uses the `{lang}/claude-api/FILE.md` path notation for all languages.

### Quick Task Reference.

**Single text classification/summarization/extraction/Q&A:**
→ Read only `{lang}/claude-api/README.md`. **Always read the README first** for any task (installation, quick start, common patterns, error handling).

**Chat UI or real-time response display:**
→ Read `{lang}/claude-api/README.md` + `{lang}/claude-api/streaming.md`.

**Long-running conversations (can exceed context window):**
→ Read `{lang}/claude-api/README.md`. See Compaction section.
**Migrating to a newer model (Fable 5 / Opus 5 / Opus 4.8 / 4.7 / 4.6 / Sonnet 5 / 4.6). Or replacing a retired model, or translating `budget_tokens` / prefill patterns to the current API:**
→ Read `shared/model-migration.md`.
**Prompting or tuning Fable 5 (long turns, effort, verbosity, autonomous runs, sub-agents)**:
→ Read `shared/model-migration.md` → Migrating to Fable 5 → Behavioral shifts. Also the Long-running agent recommendations there.
**Prompt caching / optimize caching / "why is my cache hit rate low":**
→ Read `shared/prompt-caching.md` (prefix-stability design, breakpoint placement, cache-invalidating anti-patterns). Plus `{lang}/claude-api/README.md` (Prompt Caching section).
**Auditing or cleaning up prompts, skills, or tool descriptions:**
("is this prompt outdated", "remove the cruft", "this was written for an older model")
→ Read `shared/prompt-audit.md`. Dated-pattern tables with greppable signals, the keep list (what NOT to delete), and the report + proposed-diff output contract.
**Count tokens in a file / prompt / diff ("how many tokens is X"):**
→ Read `shared/token-counting.md`. Use `messages.count_tokens`, never `tiktoken`.

**Function calling / tool use / agents:**
→ Read `{lang}/claude-api/README.md` + `shared/tool-use-concepts.md` (conceptual foundations: function calling, code execution, memory, structured outputs) + `{lang}/claude-api/tool-use.md` (language-specific code examples: tool runner, manual loop, code execution, memory, structured outputs).

**Agent design (tool surface, context management, caching strategy):**
→ Read `shared/agent-design.md` (bash vs. dedicated tools, programmatic tool calling, tool search/skills, context editing vs. compaction vs. memory, caching principles).

**Batch processing (non-latency-sensitive. Runs asynchronously at 50% cost):**
→ Read `{lang}/claude-api/README.md` + `{lang}/claude-api/batches.md`.

**File uploads across multiple requests (same file without re-uploading):**
→ Read `{lang}/claude-api/README.md` + `{lang}/claude-api/files-api.md`.

**Debugging HTTP errors or implementing error handling:**
→ Read `shared/error-codes.md`. Per-SDK typed exception class table and the Go `errors.As` pattern.

**Latest official documentation:**
→ WebFetch the URLs in `shared/live-sources.md`.

**Managed Agents (server-managed stateful agents with workspace):**
→ See the reading guide in the `## Managed Agents (Beta)` section above. It lists every `shared/managed-agents-*.md` file and the language-specific READMEs (`{lang}/managed-agents/README.md`, `curl/managed-agents.md`).

---

## When to Use WebFetch.

Use WebFetch to get the latest documentation when:

- User asks for "latest" or "current" information.
- Cached data seems incorrect.
- User asks about features not covered here.

Live documentation URLs are in `shared/live-sources.md`.

## Common Pitfalls.

- Do not truncate inputs while passing files or content to the API. Where the content is too long for the context window, notify the user. Discuss options (chunking, summarization, and more) rather than silently truncating.
- **Prefill removed (Fable 5, Opus 5, Sonnet 5, and the 4.6/4.7/4.8 family)**: Assistant message prefills (last-assistant-turn prefills) return a 400 error on every model in that list. Use structured outputs (`output_config.format`) or system prompt instructions to control response format instead. (One exception: the fallback-credit prefill claim. When redeeming a credit with `fallback_has_prefill_claim: true`, the server accepts the echoed assistant message. See the migration guide's refusal section.)
- **Settle migration scope before editing**: a user can ask to migrate code to a newer Claude model without naming a file, directory, or file list. Then **ask which scope to apply first**. The entire working directory, a specific subdirectory, or a specific set of files. Do not start editing until the user answers. Imperative phrasings are **still ambiguous**. Examples: "migrate my codebase", "move my project to X", "upgrade to Sonnet 4.6", or bare "migrate to Opus 4.8". They tell you what to do but not where, so ask. Proceed without asking only where the prompt names an exact file, a specific directory, or an explicit file list. ("migrate `app.py`", "migrate everything under `services/`", "update `a.py` and `b.py`"). See `shared/model-migration.md` Step 0.
- **`max_tokens` defaults:** Do not lowball `max_tokens`. Hitting the cap truncates output mid-thought and requires a retry. For non-streaming requests, default to `~16000` (keeps responses under SDK HTTP timeouts). For streaming requests, default to `~64000` (timeouts are not a concern, so give the model room). Go lower only with a hard reason: classification (`~256`), cost caps, deliberately short outputs, or **`max_tokens: 0`** for cache pre-warming (see `shared/prompt-caching.md` → Pre-warming).
- **Disabling thinking on {{OPUS_NAME}} has two failure modes. Prefer low/medium effort instead**. Only affects code that explicitly opts out. Thinking is on by default, so watch for a disabled-thinking setting carried forward from Opus 4.8. With `thinking: {type: "disabled"}`, the model occasionally writes a tool call into its **visible text** instead of a `tool_use` block: the turn succeeds, the call never runs, and no error is raised. In an agentic loop that text pollutes later turns. It can also leak `<thinking>` tags into the response. Turning thinking on and lowering `effort` fixes both and still cuts cost. Where a route must stay thinking-off: add *"You may say a brief sentence before using a tool"*. **Delete** any do not-think/do not-reason rule (it makes tag leakage worse). And use a generic *"Do not include internal or system XML tags in your response"* rather than naming thinking tags. Details: `shared/model-migration.md` → Two failure modes with thinking disabled.
- **128K output tokens:** Fable 5, Opus 5, Opus 4.6/4.7/4.8, Sonnet 5, and Sonnet 4.6 support up to 128K `max_tokens`. But the SDKs require streaming for values that large to avoid HTTP timeouts. Use `.stream()` with `.get_final_message()` / `.finalMessage()`.
- **Tool call JSON parsing (Fable 5, Opus 5, and the 4.6/4.7/4.8 family)**: those models can produce different JSON string escaping in tool call `input` fields (for example Unicode or forward-slash escaping). Always parse tool inputs with `json.loads()` / `JSON.parse()`. Never do raw string matching on the serialized input.
- **Structured outputs (all models):** Use `output_config: {format: {...}}` instead of the deprecated `output_format` parameter on `messages.create()`. This is a general API change, not 4.6-specific.
- **Do not reimplement SDK functionality:** The SDK provides high-level helpers. Use them instead of building from scratch. Specifically: use `stream.finalMessage()` instead of wrapping `.on()` events in `new Promise()`. Use typed exception classes (`Anthropic.RateLimitError`, and more) instead of string-matching error messages. Use SDK types (`Anthropic.MessageParam`, `Anthropic.Tool`, `Anthropic.Message`, and more) instead of redefining equivalent interfaces.
- **Error handling. Catch a chain, not one broad class**. A single `except APIStatusError` / `catch (AnthropicServiceException)` / `rescue APIError` loses the distinction between retryable (429, ≥500, network) and non-retryable (400/404) failures. Write a most-specific-first chain. For example `NotFoundError` → `RateLimitError` → `APIStatusError` → `APIConnectionError` (or the Go equivalent: `errors.As` into `*anthropic.Error` then `switch apierr.StatusCode { case 404: …; case 429: …; default: … }`). Per-language class names and namespaces are in `shared/error-codes.md`.
- **Do not research SDK types. Write first**. A type name can be absent from the documentation included in this skill. Then write the code file from the namespace/package tables in the language-specific doc. Let the compiler's error point you to the right name. Do not spend turns on WebFetch, SDK-repo clones, or compiling-and-running a separate reflection program to discover type names before writing. Produce the source file first, then fix what the compiler reports. A quick `strings` / `jar tf` / `javap` against the installed SDK is acceptable for locating names (it returns in seconds). But do not escalate beyond that. A file with a wrong type name is recoverable. A session spent on discovery with no file written is not.
- **Bash and text editor tools are Anthropic-defined, schema-less**. Declare `{"type": "bash_20250124", "name": "bash"}` / `{"type": "text_editor_20250728", "name": "str_replace_based_edit_tool"}`. No `input_schema`. A custom tool with your own schema named `"bash"` is a different tool. Handler paths and security checks are in `shared/tool-use-concepts.md` § Client-Side Tools.
- **Advisor tool model pairing**. The advisor tool's `model` must be at least as capable as the request's top-level `model`. For example executor `claude-sonnet-5` → advisor `claude-opus-4-8` or `claude-opus-4-7`. An invalid pair returns 400. Pairing table in `shared/tool-use-concepts.md` § Advisor. Availability: `shared/platform-availability.md`.
- **Agent Skills ≠ Managed Agents**. To have Claude generate a `.pptx`/`.xlsx`/, and more via Agent Skills, call `client.beta.messages.create` with `container={"skills": [...]}`, the `code_execution_20260521` tool, and both `code-execution-2025-08-25` + `skills-2025-10-02` betas. Do not use `client.beta.agents` / `sessions` / `environments` here. Those are the Managed Agents surface, not Agent Skills.
- **MCP connector needs both halves**. `mcp_servers=[{type:"url", url, name}]` alone is rejected as invalid. Also add `tools=[{type:"mcp_toolset", mcp_server_name:<same name>}]` with beta `mcp-client-2025-11-20`. Availability: `shared/platform-availability.md`.
- **`inference_geo` is a direct top-level request parameter** — `client.messages.create(..., inference_geo="us")` / `.inferenceGeo("us")`. Do not put it in `extra_body` / `putAdditionalBodyProperty`. (Messages API only. On Managed Agents, `inference_geo` instead nests inside the agent's `model` object, never top-level. See `shared/managed-agents-core.md` § Pinning inference geography.) Supported on Opus 4.6 / Sonnet 4.6 and later. Availability: `shared/platform-availability.md`. `response.usage.inference_geo` reports where inference ran.
- **Fine-grained tool streaming is not a beta feature**. Set `eager_input_streaming: true` on the tool definition and call the regular `client.messages.stream(...)`. There is no beta header and no `client.beta.*` path.
- **Cache diagnostics is beta**. Use `client.beta.messages.*` with beta `cache-diagnosis-2026-04-07`. Pass `diagnostics: {previous_message_id: null}` on the first turn and `diagnostics: {previous_message_id: <previous response id>}` on subsequent turns. The result is on `response.diagnostics`. Availability: `shared/platform-availability.md`.
- **Memory tool type is `memory_20250818`**. Declare `{"type": "memory_20250818", "name": "memory"}`. Go uses the beta-namespace type `{OfMemoryTool20250818: &anthropic.BetaMemoryTool20250818Param{}}` on `client.Beta.Messages.New`. Python/TypeScript/Ruby/PHP/C# use the non-beta `client.messages.create`. Java has both a non-beta `MemoryTool20250818` and a beta tool-runner path. Python/TypeScript provide `BetaAbstractMemoryTool` / `betaMemoryTool` helpers for implementing the backend.
- **Use a model the feature actually supports**. Some features are restricted to specific model tiers. Fast mode is {{OPUS_NAME}} / Opus 4.8 only (and Claude API only), task budgets (Messages API only. Managed Agents session budgets have no model-tier restriction) are {{OPUS_NAME}} / Fable 5 / Sonnet 5 / Opus 4.8 / 4.7 only. And the advisor tool requires a valid executor↔advisor pair. The user's prompt can name a model the feature does not support. Then use a supported model instead and note the substitution in the output.
- **Do not define custom types for SDK data structures:** The SDK exports types for all API objects. Use `Anthropic.MessageParam` for messages, `Anthropic.Tool` for tool definitions, `Anthropic.ToolUseBlock` / `Anthropic.ToolResultBlockParam` for tool results, `Anthropic.Message` for responses. Defining your own `interface ChatMessage { role: string; content: unknown }` duplicates what the SDK already provides and loses type safety.
- **Report and document output:** for tasks that produce reports, documents, or visualizations, use the code execution sandbox. It has `python-docx`, `python-pptx`, `matplotlib`, `pillow`, and `pypdf` pre-installed. Claude can generate formatted files (DOCX, PDF, charts) and return them via the Files API. Consider this for "report" or "document" type requests instead of plain stdout text.
- **Server-tool errors do not raise**. Web search and web fetch errors return HTTP 200. The `web_search_tool_result` / `web_fetch_tool_result` block's `content` is then a single error object (for example `{error_code: "max_uses_exceeded"}`). Not a raised exception. For web search, a success `content` is a *list*. An error `content` is an *object*. Branch on that before indexing.
- **Code execution output block type:** `code_execution_20260521` returns `bash_code_execution_tool_result` (with `.content.stdout`), **not** the legacy bare `code_execution_tool_result`. Iterate `response.content` and match on the correct type.
- **Tool search: never defer everything**. The search tool itself must not have `defer_loading: true`. And at least one tool in `tools` must be non-deferred. Otherwise the API returns 400 `All tools have defer_loading set`.
