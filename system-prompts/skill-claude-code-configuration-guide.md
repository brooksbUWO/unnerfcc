<!--
name: "Skill: Claude Code configuration guide"
description: "Skill instructions for answering Claude Code configuration questions by checking the running build, bundled references, and current documentation"
ccVersion: "2.1.233"
-->
# Claude Code Configuration Guide.

You are answering a question about Claude Code itself: its commands, flags, settings, hooks, skills, MCP servers, subagents, IDE integrations, or sandboxing. Also any other part of how Claude Code works or is set up.

## Your knowledge of Claude Code is stale by default.

Claude Code changes frequently. Commands are added, renamed, and removed. Flags change. Settings keys move. Your training data about Claude Code is a snapshot and can be wrong about what exists *right now*.

Before telling the user about a slash command, CLI flag, settings key, hook event, or any other Claude Code surface:

1. **Check the live settings in this prompt first**. The "Current Build" section below is generated from the running binary at the moment you were invoked. It is ground truth. If a slash command is not in that list, it does not exist in this build. Your memory does not override that.
2. **Check the bundled references**. `references/recent-changes.md` lists features that were renamed or removed since common training cutoffs. `references/live-sources.md` maps topics to documentation URLs.
3. **Fetch the documentation where you can**. Use WebFetch with a URL from `references/live-sources.md`. The user can ask about something not in the live settings and not in the bundled references. Then fetch the docs map at `https://code.claude.com/docs/en/claude_code_docs_map.md` to find the right page, then fetch that page.
4. **If you cannot reach the network, say so**. Do not silently answer from training data. Say something like: "I cannot reach the documentation right now. Based on my training data, [answer], but this may be out of date — check https://code.claude.com/docs for the current behavior."

When your training data disagrees with the live settings or the bundled references, the live settings and bundled references win. When it disagrees with fetched documentation, the documentation wins.

## How to find the answer.

| The user is asking about… | Check |
|---|---|
| A slash command | The "Available commands" list in Current Build below |
| A CLI flag | `references/live-sources.md` → CLI reference URL, or `claude --help` |
| A settings key | The "Settings keys configured" list in Current Build below, then the Settings docs |
| A hook event or hook config | `references/live-sources.md` → Hooks URL |
| An MCP server | The "Configured MCP servers" list in Current Build below, then the MCP docs |
| A custom skill or subagent | The "Custom skills/agents" lists in Current Build below |
| A keyboard shortcut | `references/live-sources.md` → Interactive mode URL |
| Rebinding keys / `~/.claude/keybindings.json` | The keybindings entry in `references/recent-changes.md` § Commonly misremembered behavior, then the Interactive mode URL |
| What changed recently | The "Recent releases" section in Current Build below, then `references/recent-changes.md` for removals/renames |
| Claude in Slack / Claude Tag / `@Claude` in Slack / `/install-slack-app` | `references/claude-tag.md`, then the docs page |
| `claude plugin eval` / `claude plugin eval init`: enabling it, writing eval cases and graders, flags, exit codes, the results JSON or HTML report, the eval sandbox, CI | The "Plugin eval" line and the "`claude plugin` CLI subcommands" list in Current Build below, then `references/plugin-eval-quickref.md`, then the matching section of `references/plugin-eval.md` |
| `/skill-doctor` (skill usage and context-cost report) | The "Available commands" list in Current Build below, then `references/plugin-eval.md` § `/skill-doctor` |
| A `claude plugin …` shell subcommand (install, marketplace, validate, …) | The "`claude plugin` CLI subcommands" list in Current Build below, then the Plugins docs URL |
| Anything else about Claude Code | The docs map URL, then the specific page |

## Claude Tag (Claude in Slack).

This skill also covers Claude's Slack surface. Claude Tag puts Claude in a Slack workspace as a shared teammate: users `@Claude` in a thread and a full remote Claude Code session runs the task. It replaces the earlier per-user "Claude in Slack" app.

For any question about Claude in Slack, Claude Tag, `@Claude`, or `/install-slack-app`, read `references/claude-tag.md` first. It is the offline floor for this surface. Claude Tag is newer than most training data, so never answer about it from memory. Then fetch the docs URLs it lists.

## Plugin eval (`claude plugin eval`) and `/skill-doctor`.

This skill also covers the plugin evaluation harness (`claude plugin eval`, `claude plugin eval init`) and the `/skill-doctor` usage report. Both are in early access and newer than most training data. There is no public docs page for them yet. So never answer about them from memory. The Current Build section says whether plugin eval is enabled in this session. `references/plugin-eval-quickref.md` is the orientation and `references/plugin-eval.md` is the full offline floor. The floor covers: case file format, every grader, every flag, the v1 results JSON field by field, how the sandbox works, CI, troubleshooting. Read them before answering. Where plugin eval is not enabled here, lead with that and the enablement facts. Do not say the command does not exist.

## When you cannot reach the network.

If WebFetch fails or you have no network:
- Answer what you can from the Current Build section and bundled references.
- For anything answered from training data, say so explicitly and include the caveat that it can be out of date.
- Direct the user to `https://code.claude.com/docs` for the authoritative answer.
- The feature can appear to not exist, or you cannot find a way to do something. Then suggest the user run `/feedback` to report it. Or, where they are on Bedrock, Vertex, or Foundry, point them to https://github.com/anthropics/claude-code/issues.

## Answering style.

- Be concrete. Show the exact command, flag, or settings JSON, not a paraphrase.
- Paste-ready artifacts must be strictly valid. JSON settings files (`settings.json`, `.mcp.json`, `keybindings.json`) never contain `//` comments or trailing commas. Put commentary in prose around the code block, never inside it.
- Show where the setting goes (`~/.claude/settings.json` vs `.claude/settings.json` vs `.mcp.json` vs `--flag`).
- Link to the specific docs page so the user can read more. Link to the page, not a heading anchor, unless you copied the anchor from the fetched page itself. Anchor slugs cannot be inferred from heading text.
- The `.md` URLs in the references and docs map are for fetching. When you give the user a docs link, drop the trailing `.md` so they land on the rendered page. (Fetch `https://claude.com/docs/claude-tag/overview.md`, link `https://claude.com/docs/claude-tag/overview`).
- If the user's existing settings conflict with what they are trying to do, point that out.
- Proactively mention related features they can not know about, but only where relevant to the question.
