<!--
name: "Skill: Run browser-driven web app example"
description: "Example file for the Run app skill showing how to start a web dev server, drive it with chromium-cli, capture screenshots, and document app-specific gotchas"
ccVersion: "2.1.213"
-->
# Example: Browser-driven web app.

You have a dev server that serves HTML to a browser. An agent in a
headless container cannot open a browser window. So "run the app" means three things:
launch the dev server, drive a headless Chromium against it, and
produce a screenshot that proves the page rendered.

Do not write a browser driver. Use `chromium-cli`.

## Dev server.

Find the dev command (`package.json` `scripts.dev`, `Makefile`,
README). Start it in the background, and wait for it to actually serve:

```bash
npm run dev &   # or yarn dev, pnpm dev, make serve, ./dev.sh
timeout 30 bash -c 'until curl -sf http://localhost:3000 >/dev/null; do sleep 1; done'
```

Do not `sleep 5`. Poll the port. Stop by killing the port's listener
— `lsof -ti:3000 -sTCP:LISTEN | xargs -r kill`. Before relaunching,
or the next run hits `EADDRINUSE`. (`$!` after `npm run dev &` is only
the npm wrapper. Npm does not forward SIGTERM to the server it spawned,
so the port kill is what actually frees it). Avoid `pkill -f` with a
broad pattern. It can match the agent's own command line and kill the
session.

## Drive.

`chromium-cli` is a headless-Chromium REPL. Pipe a script to stdin:

```bash
chromium-cli --session app <<'EOF'
nav http://localhost:3000
wait-for text=Dashboard
screenshot
click button:has-text("New item")
fill input[name="title"] Smoke test
press Enter
wait-for text=Smoke test
screenshot
console --errors
EOF
```

Screenshots land in `chromium_cli/sessions/app/screenshots/` (latest
symlinked as `screenshot.png`). That is the whole loop: `nav` →
`wait-for` the element you need → act (`click` / `fill` / `type` /
`press`) → `screenshot`. Then `console --errors` to check nothing threw.
Full command reference: `chromium-cli` skill, or `help` at the prompt.

For iterative debugging, run it under tmux and `send-keys` one command
at a time. Same commands, same session.

**If `chromium-cli` is not available:** adapt
[electron.md](electron.md)'s REPL driver. The structure and commands
transfer, but it is `_electron`-specific:
import `{ chromium }` instead, launch with
`chromium.launch({ args: ['--no-sandbox'] })`, and acquire the page via
`(await app.newContext()).newPage()` then `goto()` your dev URL. Also
drop the Electron-only window introspection
(`.windows()`/`.firstWindow()`/the `windows` command).

## What to put in the skill.

The project-specific bits only. `chromium-cli` handles the mechanics.

- **Dev command + port + stop**. The exact start line, any env vars it
  needs, and the `kill` to stop it.
- **Auth**. Whatever gets a logged-in session. A `set-cookie` line, or a
  `fill`/`click` login sequence. Or a helper script that does the API
  dance and emits the cookie.
- **One representative interaction**. Not the whole app. One path that
  proves it is running, ending in a screenshot.
- **App-specific gotchas**. Only the ones you actually hit.

## Gotchas that recur.

- **React controlled inputs**. `eval el.value = '…'` does not fire
  React's onChange. Use `fill` / `type`. They go through Playwright's
  input pipeline.
- **Websockets / long-poll**. `wait-idle` never settles. `wait-for` the
  element you actually need.
- **Slow first paint**. Vite/Next compile routes on demand. The first
  `nav` can take 10s+. `wait-for` handles it. Raw `sleep` does not.
- **`screenshot-element <sel>`** crops to one element. Use it where the
  diff is in a specific component, not the whole page.
- **Check `console --errors` before declaring success**. A page can
  render its shell while every data fetch 500s.
