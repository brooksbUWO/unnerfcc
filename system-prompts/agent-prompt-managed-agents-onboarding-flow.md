<!--
name: "Agent Prompt: Managed Agents onboarding flow"
description: "Interactive interview script that helps users configure a Managed Agent by describing the task, proposing tools and resources, setting up the environment and session, testing access, and emitting integration code"
ccVersion: "2.1.224"
-->
# Managed Agents. Onboarding Flow.

> **Invoked via `/claude-api managed-agents-onboard`**? You are in the right place. Run the interview below. Do not summarize it back to the user, ask the questions.

Claude Managed Agents is a hosted agent: Anthropic runs the agent loop and provisions a sandboxed container per session where the agent's tools execute. (Or use your own worker, with a `self_hosted` environment. See `shared/managed-agents-self-hosted-sandboxes.md`). You supply an **agent config** (tools, skills, model, system prompt. Reusable, versioned) and an **environment config** (the sandbox. Reusable across agents). Each run is a **session**.

The flow is four beats — **describe → agent → environment → session**. The same arc as the Console quickstart, and the same philosophy: **value before credentials**. The user goes from idea to a runnable session before any auth ask. Each credential is *flagged* at the moment the design makes it relevant (§2). It is *collected* once, at session setup (§4), where it binds (`sessions.create()`) and gets exercised (smoke-test). Read `shared/managed-agents-core.md` alongside this. It has full detail for each knob. This doc is the interview script.

---

## 1. Describe the task.

**Open with a one-breath signpost and a single open prompt. Do not guess, do not questionnaire**. In your own words:

> Managed Agents is hosted. Anthropic runs the agent loop, the sandbox, and the infrastructure. You just define the agent. We will do this in three moves: the agent, the environment it runs in, then a live test session. So: describe the agent you want. What must it do, and what kicks it off (a person, an event, a schedule)?

Let them answer in full before configuring anything.

## 2. Configure the agent. Propose, do not interrogate.

Their description does the interview's work. Draft the agent config from it and **present it as a proposal with your suggestions inline**. The user reacts to a concrete config instead of answering a question list. At most one batched follow-up for true gaps. Suggest where the description gives you an opening:

- **Tools** — enable the full prebuilt toolset by default (`agent_toolset_20260401`: `bash`, `read`, `write`, `edit`, `glob`, `grep`, `web_fetch`, `web_search`). **Suggest MCP servers** for any third-party service the job names (GitHub, Linear, Slack, …). And flag the credential each one implies as you suggest it ("Linear MCP → you will need a Linear API token at kickoff"). Then §4's auth step is a formality, not a surprise. Collection itself waits for §4. Custom tools only where the user's own app must answer calls (name, description, input schema. Their handler code is theirs. Do not generate it).
- **Skills** — **suggest** prebuilt `xlsx`/`docx`/`pptx`/`pdf` where the job produces those artifacts. Custom by `skill_id` (max 20 total per agent, prebuilt + custom combined).
- **Outcome** — where the description implies checkable "done" criteria (or you can elicit them in the follow-up: not "a good report" but "a CSV with a numeric `price` column per SKU"), **suggest an Outcome kickoff**. The harness grades and iterates against a rubric (`shared/managed-agents-outcomes.md`).
- **On-hand resources**. Repos on disk (`github_repository`: URL, optional `mount_path`/`checkout`. Token comes in §4), files to seed (Files API upload → `{type: "file", file_id, mount_path}`. Read-only), where the job references them.
- **Model** — default `{{OPUS_ID}}`. `{{FABLE_ID}}` for the hardest long-horizon work (`shared/model-migration.md` → Migrating to {{FABLE_NAME}}).

> ‼️ **PR creation needs the GitHub MCP server too**. A `github_repository` mount is filesystem-only. Edit in the mount → push branch via `bash` → open the PR via the MCP `create_pull_request` tool.

Full detail per knob: `shared/managed-agents-tools.md` (toolset, MCP, custom tools, skills), `shared/managed-agents-environments.md` (repos, files).

## 3. Environment.

Usually zero or one question:

- **Reuse or create**? Environments are shared across agents. Check for an existing one first.
- **Networking** — default unrestricted egress. Switch to `limited` only where the user wants egress control. Then set `allow_mcp_servers: true` or list every MCP server domain in `allowed_hosts`, or those tools fail silently.
- **Suggest `self_hosted`** where the signals are there: tools must run on their own infra, or secrets cannot leave it. Or they need binaries/data the cloud container lacks (`shared/managed-agents-self-hosted-sandboxes.md`. Not available on Claude Platform on AWS). Otherwise `cloud`. Do not raise it unprompted for simple jobs.

## 4. Session. Auth, then test run.

**Auth happens here. Collect the credentials flagged in §2, now that the config is settled**: a vault (existing or `vaults.create()`) + `vaults.credentials.create()` for each MCP server declared in §2. Add `environment_variable` credentials for API keys the job uses (substituted at egress. The sandbox sees a placeholder), and the `authorization_token` for each repo mount. Credentials are write-only. MCP credentials match servers by URL and auto-refresh. See `shared/managed-agents-tools.md` → Vaults.

**Silent viability gate. Run this yourself before emitting anything. Surface only the gaps**. Walk the job clause by clause: every verb maps to an enabled tool or MCP server ("open a PR" → GitHub MCP, not just the mount). Every MCP server and repo mount has its credential from the auth step. Every external host is reachable under the networking choice. Every file/repo/dataset the job references is mounted. "done" is checkable. If something's missing, say so and resolve it. Do not emit a config you already know is under-resourced.

**Kickoff — pick one, never both:**
- `user.message` — conversational.
- `user.define_outcome` + rubric. When §2 settled on an Outcome. The harness iterates and grades until the rubric passes.
- **Scheduled shape**? Skip per-session kickoff entirely. Create a **deployment** (`deployments.create()` with `schedule` + `initial_events`). Each firing creates the session autonomously. See `shared/managed-agents-scheduled-deployments.md`.

Mechanics to bake into the runtime code: session creation resolves resources (a bad mount surfaces there, before tokens) but does not itself provision the sandbox. Open the event stream *before* sending the kickoff. Break on `session.status_terminated`, or `session.status_idle` with any non-`requires_action` `stop_reason`. Terminal, or `budget_reached`, which is not terminal (only a budget change/removal resumes it) (`shared/managed-agents-client-patterns.md` Pattern 5). Usage lands on `span.model_request_end`. Artifacts land in `/mnt/session/outputs/` (`files.list({scope_id: session.id, ...})`).

## 5. Integrate. Emit the code.

Go straight from the last answer to the code. No preamble, no lecture about setup-vs-runtime. The two-block structure shows it. Generate **two clearly-separated blocks**:

**Block 1 — Setup (run once, store the IDs)**. Prefer **YAML files + `ant` CLI**. Agents and environments are version-controlled definitions users must check in and apply from CI:

1. `<name>.agent.yaml` (flat: `name`, `model`, `system`, `tools`, `mcp_servers`, `skills`) and `<name>.environment.yaml`.
2. ```sh
   AGENT_ID=$(ant beta:agents create < <name>.agent.yaml --transform id -r)
   ENV_ID=$(ant beta:environments create < <name>.environment.yaml --transform id -r)
   # CI sync: ant beta:agents update --agent-id "$AGENT_ID" --version N < <name>.agent.yaml
   ```

SDK fallback where the user asks. And **required on Claude Platform on AWS**, where auth is SigV4 and the `ant` CLI has no SigV4 mode. (Use the platform client from `shared/claude-platform-on-aws.md`): label it `# ONE-TIME SETUP — run once, save the IDs` and call `environments.create()` → `agents.create()`.

> ⚠️ **Deployments are newer than the rest of the MA surface**. Before emitting `ant beta:deployments …` or `client.beta.deployments` / `client.beta.deployment_runs` calls, verify the user's installed CLI/SDK exposes them (`ant beta:deployments --help`. `hasattr(client.beta, "deployments")`). If not, emit raw HTTP against `POST /v1/deployments` with the `managed-agents-2026-04-01` beta header. Add `oauth-2025-04-20` where you authenticate with a Bearer token from `ant auth print-credentials`. Leave an upgrade note marking what simplifies to SDK calls.

**Scheduled shape? The deployment is setup, not runtime**. Create it in Block 1, after the agent/environment IDs exist (`deployments.create()` with `schedule` + `initial_events`). Block 2 is then **not** a session loop. There is no per-run kickoff to send. Emit instead: a manual-run trigger (`POST /v1/deployments/{id}/run`) so the user can test now rather than wait for the first firing. The manual run doubles as the smoke test. Plus a fetch helper (latest `deployment_runs` entry → `session_id` → Console URL + `files.list(scope_id=session_id)` for the artifacts).

**Block 2 — Runtime (every invocation. Conversational and Outcome shapes)**. SDK code in the detected language (Python/TS/cURL. SKILL.md → Language Detection). Do not emit shell loops here:

1. Load `agent_id` + `env_id` from config/env.
2. `sessions.create(agent=AGENT_ID, environment_id=ENV_ID, resources=[...], vault_ids=[...])`, then print the Console URL so the user can watch live: `https://platform.claude.com/workspaces/default/sessions/{session.id}` (swap `default` for their workspace slug).
3. **Smoke-test where the job depends on MCP servers, credentials, or locked-down hosts**. Those failures do not surface at `sessions.create()`, only on first use. One cheap probe turn ("Confirm you can reach <service> and list 1–2 items; do not start the task"). Check the result, then send the real kickoff. Skip where there are no external dependencies.
4. Open stream → send the §4 kickoff → loop with the terminal gate from §4.

> ⚠️ **Never emit `agents.create()` and `sessions.create()` in the same unguarded block**. That teaches creating a new agent per run, the #1 anti-pattern. Single-script requests: wrap creation in `if not os.getenv("AGENT_ID"):`.

Pull exact syntax from `{lang}/managed-agents/README.md` for your detected language (cURL and C#: use `curl/managed-agents.md` as the wire-level reference). Do not invent field names.
