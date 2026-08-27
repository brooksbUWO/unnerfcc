<!--
name: "Skill: update-config (7-step verification flow)"
description: "A skill that guides Claude through a 7-step process to construct and verify hooks for Claude Code, ensuring they work correctly in the user's specific project environment."
ccVersion: "2.1.77"
-->
## Constructing a Hook (with verification).

Given an event, matcher, target file, and desired behavior, follow this flow. Each step catches a different failure class. A hook that silently does nothing is worse than no hook.

1. **Dedup check**. Read the target file. If a hook already exists on the same event+matcher, show the existing command and ask: keep it, replace it, or add alongside.

2. **Construct the command for THIS project. Do not assume**. The hook receives JSON on stdin. Build a command that:
   - Extracts any needed payload safely. Use `jq -r` into a quoted variable or `{ read -r f; ... "$f"; }`, NOT unquoted `| xargs` (splits on spaces).
   - Invokes the underlying tool the way this project runs it (npx/bunx/yarn/pnpm? Makefile target? globally-installed?)
   - Skips inputs the tool does not handle (formatters often have `--ignore-unknown`. If not, guard by extension).
   - Stays RAW for now. No `|| true`, no stderr suppression. You will wrap it after the pipe-test passes.

3. **Pipe-test the raw command**. Synthesize the stdin payload the hook will receive and pipe it directly:
   - `Pre|PostToolUse` on `Write|Edit`: `echo '{"tool_name":"Edit","tool_input":{"file_path":"<a real file from this repo>"}}' | <cmd>`.
   - `Pre|PostToolUse` on `Bash`: `echo '{"tool_name":"Bash","tool_input":{"command":"ls"}}' | <cmd>`.
   - `Stop`/`UserPromptSubmit`/`SessionStart`: most commands do not read stdin, so `echo '{}' | <cmd>` suffices.

   Check exit code AND side effect (file actually formatted, test actually ran). If it fails you get a real error. Fix (wrong package manager? tool not installed? jq path wrong?) and retest. Once it works, wrap with `2>/dev/null || true` (unless the user wants a blocking check).

4. **Write the JSON**. Merge into the target file (schema shape in the "Hook Structure" section above). If this creates `.claude/settings.local.json` for the first time, add it to .gitignore. The Write tool does not auto-gitignore it.

5. **Check syntax + schema in one shot:**

   `jq -e '.hooks.<event>[] | select(.matcher == "<matcher>") | .hooks[] | select(.type == "command") | .command' <target-file>`.

   Exit 0 + prints your command = correct. Exit 4 = matcher does not match. Exit 5 = malformed JSON or wrong nesting. A broken settings.json silently disables ALL settings from that file. Fix any pre-existing malformation too.

6. **Prove the hook fires**. Only for `Pre|PostToolUse` on a matcher you can trigger in-turn (`Write|Edit` via Edit, `Bash` via Bash). `Stop`/`UserPromptSubmit`/`SessionStart` fire outside this turn. Skip to step 7.

   For a **formatter** on `PostToolUse`/`Write|Edit`: introduce a detectable violation via Edit (two consecutive blank lines, bad indentation, missing semicolon. Something this formatter corrects. NOT trailing whitespace, Edit strips that before writing), re-read, check that the hook **fixed** it. For **anything else**: temporarily prefix the command in settings.json with `echo "$(date) hook fired" >> /tmp/claude-hook-check.txt; `. Then trigger the matching tool (Edit for `Write|Edit`, a harmless `true` for `Bash`) and read the sentinel file.

   **Always clean up**. Revert the violation, strip the sentinel prefix. Whether the proof passed or failed.

   **If proof fails but pipe-test passed and `jq -e` passed**: the settings watcher is not watching `.claude/`. It only watches directories that had a settings file at session start. The hook is written correctly. Tell the user to open `/hooks` once (reloads settings) or restart. You cannot do this yourself. `/hooks` is a user UI menu and opening it ends this turn.

7. **Handoff**. Tell the user the hook is live (or needs `/hooks`/restart per the watcher caveat). Point them at `/hooks` to review, edit, or disable it later. The UI shows "Ran N hooks" only where a hook errors or is slow. Silent success is invisible by design.
