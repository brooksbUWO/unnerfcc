<!--
name: "Skill: /stuck slash command"
description: "Diagnoses frozen or slow Claude Code sessions"
ccVersion: "2.1.77"
-->
# /stuck — diagnose frozen/slow Claude Code sessions.

The user thinks another Claude Code session on this machine is frozen, stuck, or very slow. Investigate and post a report to #claude-code-feedback.

## What to look for.

Scan for other Claude Code processes (excluding the current one. PID is in `process.pid` but for shell commands just exclude the PID you see running this prompt). Process names are typically `claude` (installed) or `cli` (native dev build).

Signs of a stuck session:
- **High CPU (≥90%) sustained**. Likely an infinite loop. Sample twice, 1-2s apart, to check that it is not a transient spike.
- **Process state `D` (uninterruptible sleep)**. Often an I/O hang. The `state` column in `ps` output. First character matters (ignore modifiers like `+`, `s`, `<`).
- **Process state `T` (stopped)**. User probably hit Ctrl+Z by accident.
- **Process state `Z` (zombie)**. Parent is not reaping.
- **Very high RSS (≥4GB)**. Possible memory leak making the session sluggish.
- **Stuck child process**. A hung `git`, `node`, or shell subprocess can freeze the parent. Check `pgrep -lP <pid>` for each session.

## Investigation steps.

1. **List all Claude Code processes** (macOS/Linux):
   ```
   ps -axo pid=,pcpu=,rss=,etime=,state=,comm=,command= | grep -E '(claude|cli)' | grep -v grep
   ```
   Filter to rows where `comm` is `claude` or (`cli` AND the command path contains "claude").

2. **For anything suspicious**, gather more context:
   - Child processes: `pgrep -lP <pid>`.
   - If high CPU: sample again after 1-2s to check that it is sustained.
   - If a child looks hung (for example a git command), note its full command line with `ps -p <child_pid> -o command=`.
   - Check the session's debug log where you can infer the session ID: `~/.claude/debug/<session-id>.txt` (the last few hundred lines often show what it was doing before hanging).

3. **Consider a stack dump** for a truly frozen process (advanced, optional):
   - macOS: `sample <pid> 3` gives a 3-second native stack sample.
   - This is big. Grab it only where the process is clearly hung and you want to know *why*.

## Report.

**Post to Slack only where you actually found something stuck**. If every session looks healthy, tell the user that directly. Do not post an all-clear to the channel.

If you did find a stuck/slow session, post to **#claude-code-feedback** (channel ID: `C07VBSHV7EV`) using the Slack MCP tool. Use ToolSearch to find `slack_send_message` where it is not already loaded.

**Use a two-message structure** to keep the channel scannable:

1. **Top-level message**. One short line: hostname, Claude Code version, and a terse symptom. Examples: "session PID 12345 pegged at 100% CPU for 10min" or "git subprocess hung in D state". No code blocks, no details.
2. **Thread reply**. The full diagnostic dump. Pass the top-level message's `ts` as `thread_ts`. Include:
   - PID, CPU%, RSS, state, uptime, command line, child processes.
   - Your diagnosis of what is likely wrong.
   - Relevant debug log tail or `sample` output where you captured it.

If Slack MCP is not available, format the report as a message the user can copy-paste into #claude-code-feedback. Let them know to thread the details themselves.

## Notes.
- Do not kill or signal any processes. This is diagnostic only.
- If the user gave an argument (for example a specific PID or symptom), focus there first.
