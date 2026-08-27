<!--
name: "Tool Description: Background monitor (streaming events)"
description: "Describes the background monitor tool that streams stdout events from long-running scripts as chat notifications, with guidelines on script quality, output volume, and selective filtering"
ccVersion: "2.1.235"
variables:
  - "BACKGROUND_TASKS_DISABLED"
-->
Start a background monitor that streams events from a long-running script. Each stdout line is an event. You keep working, and notifications arrive in the chat. Events arrive on their own schedule. They are not replies from the user, even for an event that lands while you wait for a user answer.

Pick by how many notifications you need:
${'- **One** ("tell me when the server is ready / the build finishes") → ' + (BACKGROUND_TASKS_DISABLED ? 'run the command in the **foreground with Bash**, exiting when the condition is true, e.g. `until grep -q "Ready in" dev.log; do sleep 0.5; done`.' : 'use **Bash with `run_in_background`** and a command that exits when the condition is true, e.g. `until grep -q "Ready in" dev.log; do sleep 0.5; done`. You get a single completion notification when it exits.')}
- **One per occurrence, without end** → Monitor with an unbounded command (`tail -f`, `inotifywait -m`, `while true`). Example: "tell me every time an ERROR line appears".
- **One per occurrence, up to a known end** → Monitor with a command that emits lines, then exits. Example: "emit each CI step result, then stop".

Your script's stdout is the event stream. Each line becomes a notification. Exit ends the watch.

```bash
  # Each matching log line is an event
  tail -f /var/log/app.log | grep --line-buffered "ERROR"

  # Each file change is an event
  inotifywait -m --format '%e %f' /watched/dir

  # Poll GitHub for new PR comments and emit one line per new comment
  last=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  while true; do
    now=$(date -u +%Y-%m-%dT%H:%M:%SZ)
    gh api "repos/owner/repo/issues/123/comments?since=$last" --jq '.[] | "\(.user.login): \(.body)"'
    last=$now; sleep 30
  done

  # Node script that emits events as they arrive (WebSocket listener)
  node watch-for-events.js

  # Per-occurrence with a natural end: emit each CI check as it lands, exit when the run completes
  prev=""
  while true; do
    s=$(gh pr checks 123 --json name,bucket)
    cur=$(jq -r '.[] | select(.bucket!="pending") | "\(.name): \(.bucket)"' <<<"$s" | sort)
    comm -13 <(echo "$prev") <(echo "$cur")
    prev=$cur
    jq -e 'all(.bucket!="pending")' <<<"$s" >/dev/null && break
    sleep 30
  done
```

**Do not use an unbounded command for a single notification**. `tail -f`, `inotifywait -m`, and `while true` never exit on their own. So the monitor stays armed until timeout, even after the event fires. If you need one "X is ready" alert, ${BACKGROUND_TASKS_DISABLED ? "use a foreground Bash `until` loop instead" : "use Bash `run_in_background` with an `until` loop instead (one notification, ends in seconds)"}. Note: `tail -f log | grep -m 1 ...` does *not* fix this. If the log goes quiet after the match, `tail` never receives SIGPIPE, and the pipeline hangs anyway.

**Script quality:**
- Every pipe stage must flush per line, or matches sit in its buffer unseen. `grep` needs `--line-buffered`. `awk` needs `fflush()`. `head` cannot flush at all. `| head -N` delivers nothing until N matches accumulate, then it ends the stream.
- In poll loops, handle transient failures (`curl ... || true`). One failed request must not kill the monitor.
- Poll intervals: 30s or more for remote APIs (rate limits), 0.5-1s for local checks.
- Write a specific `description`. It appears in every notification ("errors in deploy.log", not "watching logs").
- Only stdout is the event stream. Stderr goes to the output file (readable via Read) but does not trigger notifications. For a command that you run directly (`python train.py 2>&1 | grep --line-buffered ...`), merge stderr with `2>&1` so its failures reach your filter. (This has no effect on `tail -f` of an existing log. That file holds only what its writer redirected.)

**Coverage: silence is not success.** Your filter must match every terminal state of the watched job, not just the happy path. A monitor that greps only for the success marker stays silent through a crashloop or a hung process. It also stays silent through an unexpected exit. Silence looks identical to "still running." Before you arm the monitor, ask one question. *If this process crashed right now, does my filter emit anything?* If not, widen it.

```bash
  # Wrong: silent on crash, hang, or any non-success exit
  tail -f run.log | grep --line-buffered "elapsed_steps="

  # Right: one alternation covering progress plus the failure signatures you act on
  tail -f run.log | grep -E --line-buffered "elapsed_steps=|Traceback|Error|FAILED|assert|Killed|OOM"
```

For poll loops that check job state, emit on every terminal status (`succeeded|failed|cancelled|timeout`), not just success. If you cannot enumerate the failure signatures with confidence, broaden the grep alternation, do not narrow it. Some extra noise is better than a missed crashloop.

**Output volume**: Every stdout line is a conversation message. So the filter must be selective. But selective means "the lines you act on", not "only good news". Never pipe raw logs. Filter to exactly the success and failure signals that you care about. A monitor that produces too many events is stopped automatically. If this happens, restart with a tighter filter.

Stdout lines within 200ms are batched into a single notification. So multiline output from a single event groups naturally.

The script runs in the same shell environment as Bash. Exit ends the watch (the exit code is reported). Timeout kills the watch. Set `persistent: true` for session-length watches (PR monitoring, log tails). The monitor then runs until you call TaskStop or the session ends. Use TaskStop to cancel early.
