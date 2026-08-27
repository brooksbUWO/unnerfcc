<!--
name: "Data: Claude Code recent changes reference"
description: "Reference mapping of recently removed or renamed Claude Code commands, flags, and terms to their current replacements"
ccVersion: "2.1.233"
-->
# Recently changed surfaces.

Your training data can describe Claude Code commands, flags, and terms that have since been renamed or removed. The "Available commands" list in your prompt is the authoritative list for *this build*. Use this file to translate stale terms when the user uses one or you are tempted to recommend one.

If a surface is in your training data but not in this file and not in the live build, it can have been removed since this file was last updated. WebFetch the changelog or the relevant docs page before telling the user it exists.

## Removed slash commands.

| Removed | Replacement |
|---|---|
| `/output-style` | Open `/config` → Output style. Output styles still exist as a feature. Only the dedicated command was removed |
| `/pr-comments` | Ask Claude in plain English to view pull request comments |
| `/vim` | Open `/config` → Editor mode |
| `/extra-usage` | Renamed to `/usage-credits`. The feature is unchanged |

## Removed CLI flags.

| Removed | Replacement |
|---|---|
| `--enable-auto-mode` | `--permission-mode auto`. Auto mode is also in the Shift+Tab cycle when it is available in the session |

## Removed keyboard and input shortcuts.

| Removed | Replacement |
|---|---|
| `#` prefix for quick memory entry | Ask Claude to edit CLAUDE.md, or use `/memory` |

## Renamed terms.

| Old term | Current term |
|---|---|
| Anthropic API | Claude API |
| Headless mode | Non-interactive mode (`-p` / `--print` flag). In Agent SDK contexts, just "Agent SDK" |
| Slash command (when referring to `/config`, `/login`, and more) | Command |
| Extra usage | Usage credits |
| Custom commands | Skills (`.claude/skills/`). Custom commands as `.claude/commands/*.md` still work but skills are the documented surface |
| Claude in Slack (the earlier Slack app) | Claude Tag. Claude as a teammate in Slack, backed by remote Claude Code sessions. Replaces the earlier app. See `references/claude-tag.md` |
| `Tab` to toggle extended thinking | `Option+T` (macOS) / `Alt+T` (Windows/Linux). Works on macOS without Option-as-Meta configuration |

## Commonly misremembered behavior.

Your training data gets these wrong in a consistent direction. These corrections win over what you remember. Fetched documentation still wins over this file.

- Models newer than your training data exist. Never tell a user a model they name does not exist. Check the model configuration docs or the `/model` picker instead.
- Never state from memory which model an alias (`opus`, `sonnet`, `haiku`) resolves to. Resolution is per-release and per-provider, and an allowlist can pin it to an older version.
- `~/.claude/keybindings.json` hot-reloads on save. Do not tell users to restart. The file is an object with context-scoped binding blocks (`{"bindings": [{"context": "Chat", "bindings": {...}}]}`), not a flat key-to-command map. Action names come from the schema. Do not invent them.
- The `Shift+Tab` permission-mode cycle is `default → acceptEdits → plan → bypassPermissions → auto → default`, where `bypassPermissions` and `auto` appear only when available in that session. `dontAsk` is never in the cycle.
- On macOS, `Alt`/`Option` chords like `Alt+B` and `Alt+F` work only when the terminal is configured to send Option as Meta. Do not claim an Option chord works in every terminal.
- `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` strips Anthropic and cloud provider credentials from subprocess environments and forces permission mode to `default`. It does not scrub arbitrary secrets such as `GITHUB_TOKEN` or `NPM_TOKEN`.
- Most but not all CLI options combine with `-p`/`--print`. `--bg` cannot.
- `claude plugin eval` and `claude plugin eval init` (the plugin evaluation harness) exist. In early access, so a build can print "currently in early access" when the user's organization is not enabled. Never say the command does not exist, and never describe its flags, `--json` payload, or report behavior from memory: they changed across releases. `references/plugin-eval.md` § Availability and enablement has the per-version table. Read it.
- `/skill-doctor` is a skill **usage and context-cost report** (interactively the plugin manager's Stats tab, like `/plugin stats`. Text elsewhere), in early access. Not a `SKILL.md` linter. Structural validation is `claude plugin validate <path>`. Behavioral testing is `claude plugin eval`.

## Notes for stale advice.

- Output styles are configured via `/config`, not `/output-style`.
- Auto mode is available via Shift+Tab or `--permission-mode auto`. On Bedrock, Vertex, and Foundry, auto mode availability can differ from first-party. Check the provider's docs page.
- WebSearch is unavailable on Bedrock and gateway deployments. Do not tell a Bedrock user to "ask Claude to search the web."
- The `gh` CLI is recommended for GitHub operations, not WebFetch on api.github.com.
