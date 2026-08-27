<!--
name: "Skill: Run web server API example"
description: "Example file for the Run app skill showing how to document a server or API lifecycle with background launch, readiness checks, curl verification, and shutdown"
ccVersion: "2.1.213"
-->
# Example: Web server / API.

The distinguishing concern for servers is **lifecycle**: an agent must
start the server in the background and verify it is up. Then
interact with it, and cleanly shut it down. A foreground `npm start` that blocks the shell is
useless to an agent.

## Structure to follow.

A good server run skill has:

1. **Prerequisites & setup**. Same as any project.
2. **Run** — the background-launch pattern (below), not a blocking command.
3. **Verify** — a `curl` or similar that shows the server is actually up.
4. **Stop** — how to cleanly terminate the background process.

Put a long launch/poll/smoke sequence (more
than a couple of lines) in a `smoke.sh` inside the skill directory.
Have `SKILL.md` say "run the smoke script". One command: the exit code
tells you whether the server is healthy.

## Background-launch pattern.

Do not write:

> ```bash
> npm start
> ```

That blocks. Instead, show how to launch in the background, wait for
readiness, and find the PID later:

> ```bash
> npm start &> /tmp/server.log &
> SERVER_PID=$!
>
> # Wait for the server to come up (adjust timeout/port as needed)
> for i in {1..30}; do
>   curl -sf http://localhost:3000/health > /dev/null && break
>   sleep 1
> done
> ```

Then the verification step:

> ```bash
> curl http://localhost:3000/health
> # → {"status":"ok"}
> ```

And stopping:

> ```bash
> kill $SERVER_PID
> # $! is the npm wrapper's PID and npm doesn't forward SIGTERM to the
> # server it spawned — killing the port's listener is what reliably frees it:
> lsof -ti:3000 -sTCP:LISTEN | xargs -r kill
> ```

Prefer the captured PID or the port over `pkill -f "<pattern>"`. Broad
patterns like `pkill -f "next|vite|node"` match the agent's own command
line and can kill the session that ran them.

## Details worth documenting.

- **Which port**. Make it explicit and say how to override it (`PORT=4000 npm start`).
- **What "ready" looks like**. A specific log line or a health endpoint to hit.
- **Required env vars**. Database URL, API keys, and more. With a template `.env`
  if the list is long.
- **Hot reload vs production mode**. If they differ meaningfully, say which
  to use and when.
- **Dependent services**. If the server needs Redis, Postgres, or similar,
  point at a docker-compose that brings them up. Or include the `docker run`
  command directly.

## Example snippet.

Here is what a Run section for a typical Node API can look like:

> ## Run.
> 
> Start the dev server in the background:
> 
> ```bash
> npm run dev &> /tmp/api.log &
> ```
> 
> The server listens on port 3000. Wait for it to be ready, then verify:
> 
> ```bash
> for i in {1..20}; do
>   curl -sf http://localhost:3000/health && break
>   sleep 0.5
> done
> curl http://localhost:3000/health
> # → {"status":"ok","version":"1.2.3"}
> ```
> 
> Logs are at `/tmp/api.log`. Stop by killing the port's listener (`$!`
> after `npm run dev &` is the npm wrapper, and npm does not forward.
> SIGTERM to the server it spawned):
> 
> ```bash
> lsof -ti:3000 -sTCP:LISTEN | xargs -r kill
> ```
> 
> ### Environment.
> 
> | Variable | Required | Default | Notes |
> |---|---|---|---|
> | `DATABASE_URL` | Yes | — | Postgres connection string |
> | `PORT` | No | `3000` | |
> | `LOG_LEVEL` | No | `info` | `debug` / `info` / `warn` / `error` |
