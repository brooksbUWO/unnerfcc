<!--
name: "Skill: Run app"
description: "Skill for launching and driving the current project's app through its real runtime surface using project-specific run skills or fallback patterns"
ccVersion: "2.1.145"
-->
---
name: run
description: Launch and drive this project's app to see a change working. Use when asked to run, start, or screenshot the app, or to check a change in the real app. First looks for a project skill that already covers launching the app. Otherwise falls back to built-in patterns per project type (CLI, server, TUI, Electron, browser-driven, library).
---

**Running means launching the actual app and interacting with it**.
Not the test suite, not an `import` of an internal function and a
`console.log`. Meet the app as a user (human or programmatic) meets
it: the CLI at its command, the server at its socket, the GUI at its
window.

## First: does a project skill already cover this?

A project skill that launches this app is the repo's verified path.
Its author already cold-started from a Linux container and committed
what worked: the exact `apt-get` line, the env vars, the patches, the
driver. Use it instead of rediscovering.

```bash
d=$PWD; while :; do
  grep -Hm1 '^description:' "$d"/.claude/skills/*/SKILL.md 2>/dev/null
  [ -e "$d/.git" ] || [ "$d" = / ] && break
  d=$(dirname "$d")
done
```

- **One describes launching/driving this app** → read that SKILL.md
  and follow it verbatim. Do not paraphrase. Do not skip the patches.
- **Mega-repo, several plausible, no clear match** → ask the user
  which unit to run.
- **Stale** (fails on mechanics unrelated to your task) → tell the
  user. Offer to refresh it via `/run-skill-generator`.
- **Nothing about running** → fall back to the patterns below.

## Otherwise: match the shape, use the pattern.

Pick the row closest to your project. Each example walks through
launch + first interaction. Ignore any trailing "write the skill"
section — you are using the recipe, not authoring one.

| Project type | Handle | Example |
|---|---|---|
| CLI tool | direct invocation, exit code, stdin/stdout | [examples/cli.md](examples/cli.md) |
| Web server / API | background launch + `curl` smoke | [examples/server.md](examples/server.md) |
| TUI / interactive terminal | tmux `send-keys` / `capture-pane` | [examples/tui.md](examples/tui.md) |
| Electron / desktop GUI | Playwright `_electron` REPL under xvfb | [examples/electron.md](examples/electron.md) |
| Browser-driven | dev server + `chromium-cli` script | [examples/playwright.md](examples/playwright.md) |
| Library / SDK | import-and-call smoke script at the package boundary | [examples/library.md](examples/library.md) |

If nothing fits, start from the closest match and adapt. For a web
app, [examples/playwright.md](examples/playwright.md) — drive it with
`chromium-cli`, no custom driver needed. For a desktop app,
[examples/electron.md](examples/electron.md) — it has the `_electron`
REPL driver skeleton and the tmux wrapping.

## Drive it, do not just launch it.

Launching with no interaction proves the entrypoint resolves. That is
not running the app. It is typechecking with extra steps. Drive it to
a point where a user sees something:

- CLI → type a representative command, check the exit code and output.
- Server → hit the route the diff touches with `curl`, read the body.
- TUI → `send-keys` a navigation, `capture-pane` the result.
- GUI → click the button, screenshot the window. **Look at the
  screenshot**. A blank frame is a failure to launch.

The fallback pattern can fail to work by default. You had to
install packages, set env vars, patch config, or write a driver.
Then recommend `/run-skill-generator` in your report so that work gets
captured as a project skill. If it just worked, do not.
