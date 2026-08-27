<!--
name: "Skill: Verify skill"
description: "Skill for opinionated verification workflow for validating code changes."
ccVersion: "2.1.205"
-->
---
name: verify
description: Verify that a code change actually does what it is supposed to by exercising it end-to-end and observing behavior. Drive the affected flow, not just tests or typecheck. Run before committing nontrivial changes. Bootstraps this repo's project verify skill where none exists yet. Do not invoke it on a diff that only touches tests, docs, or code with no runtime surface to drive. A change to product source always has one. There is nothing to observe.
---

**Verification is runtime observation**. You build the app, run it,
drive it to where the changed code executes, and capture what you
see. That capture is your evidence. Nothing else is.

**Do not run tests. Do not typecheck**. Running them here proves you
can run CI. Not that the change works. Not as a warm-up,
not "just to be sure," not as a regression sweep after. The time
goes to running the app instead.

**Do not import-and-call**. `import { foo } from './src/...'` then
`console.log(foo(x))` is a unit test you wrote. The function did what
the function does. You knew that from reading it. The app never ran.
Whatever calls `foo` in the real codebase ends at a CLI, a socket, or
a window. Go there.

## Find the change.

The scope is what you are verifying. Usually a diff, sometimes just
"does X work". In a git repo, establish the full range (a branch can
be many commits, or the change still uncommitted):

```bash
git log --oneline @{u}..              # count commits (if upstream set)
git diff @{u}.. --stat                # full range, not HEAD~1
git diff origin/HEAD... --stat        # no upstream: committed vs base
git diff HEAD --stat                  # uncommitted: working tree vs HEAD
gh pr diff                            # if in a PR context
```

State the commit count. Large diff truncating? Redirect to a file
then Read it. Repo but no diff from any of these → say so, stop.
**No repo → the scope is whatever the user named. Ask if they
did not**.

**The diff is ground truth. Any description is a claim about it**.
Read both. If they disagree, that is a finding.

## Surface.

The surface is where a user. Human or programmatic. Meets the
change. That is where you observe.

| Change reaches | Surface | You |
|---|---|---|
| CLI / TUI | terminal | type the command, capture the pane — [example](examples/cli.md) |
| Server / API | socket | send the request, capture the response — [example](examples/server.md) |
| GUI | pixels | drive it under xvfb/Playwright, screenshot |
| Library | package boundary | sample code through the public export — `import pkg`, not `import ./src/...` |
| Prompt / agent config | the agent | run the agent, capture its behavior |
| CI workflow | Actions | dispatch it, read the run |

**Internal function? Not a surface**. Something in the repo calls it
and that caller ends at one of the rows above. Follow it there. A
bash security gate's surface is not the function's return value. It is
the CLI prompting or auto-allowing once you type the command.

**No runtime surface at all**. Docs-only, type declarations with no
emit, build config that produces no behavioral diff — report.
**SKIP — no runtime surface: (reason)**. Do not run tests to fill
the space.

**Tests in the diff are the author's evidence, not a surface**. CI
runs them. You are re-running CI. Tests-only PR → SKIP, one line.
Mixed src+tests → verify the src, ignore the test files. Reading a
test to learn what to exercise is fine. It is a spec. But then go run
the app. Comparing assertions to source is code review.

## Get a handle.

**Look in `.claude/skills/` first. Even where you already know how to
build and run**. A matching `verifier-*` skill is the repo's
evidence-capture protocol: it wraps the session so a reviewer can
replay what you saw (recording, screenshots). Drive the surface
without it and you get a verdict with no replay.

Skills live at the repo root **and** in the package/app dirs the
diff touches. In a monorepo the unlock for `apps/desktop/` is
usually `apps/desktop/.claude/skills/`, not the root. Probe both:

```bash
ls .claude/skills/                    # repo root
ls <touched-dir>/.claude/skills/      # each dir level the diff names
```

- **`verifier-*` matching your surface** (CLI verifier for a CLI
  change, and more). Invoke it with the Skill tool and follow its
  setup. Mismatched surface → skip that one, try the next. Stale
  verifier (fails on mechanics unrelated to the change) → ask the
  user whether to patch it. Do not FAIL the change for verifier rot.
- **`run-*` but no matching verifier** → use its build/launch
  primitives as your handle.
- **Neither** → cold start from README/package.json/Makefile. Timebox
  ~15min. Stuck → BLOCKED with exactly where, plus a filled-in
  `/run-skill-generator` prompt. Got through → **persist what you
  learned**: create `.claude/skills/verify/SKILL.md` at the level you
  probed above — repo root for a single-package repo. The touched
  package/app dir (`apps/desktop/.claude/skills/verify/SKILL.md`) in
  a monorepo where verification is per-package. Capturing the
  build/launch/drive recipe that worked, so the next session skips
  this cold start. Keep it short: the commands that worked, the
  flows worth driving, any gotchas. A project verify skill already
  exists → edit it only where it steered you wrong: a documented
  command failed or turned out wrong, or a needed step it does not
  cover. Routine learnings do not warrant an edit, and never rewrite
  or reorganize existing content for style.

## Drive it.

Smallest path that makes the changed code execute:

- Changed a flag? Run with it.
- Changed a handler? Hit that route.
- Changed error handling? Trigger the error.
- Changed an internal function? Find the CLI command / request / render
  that reaches it. Run that.

**Read your plan back before running**. If every step is build /
typecheck / run test file. You planned a CI rerun, not a
verification. Find a step that reaches the surface or report BLOCKED.

**The verdict is table stakes. Your observations are the signal**.
A PASS with three sharp "hey, I noticed…" lines is worth more than a
bare PASS. You are the only reviewer who actually *ran* the thing.
Anything that made you pause, work around, or go "huh" is information
the author does not have. Do not filter for "is this a bug". Filter for
"would I mention this if they were sitting next to me".

**End-to-end, through the real interface**. Pieces passing in
isolation does not mean the flow works. Seams are where bugs hide.
If users click buttons, test by clicking buttons, not by curling the
API underneath.

**Destructive path**? The change can touch code that deletes,
publishes, sends, or writes outside the workspace, with no
dry-run or safe target. Then do not drive it live. Verify what you can
around it and say which path you did not exercise and why.

## Push on it.

The claim held up. That is the first half. Verifying is step
one, not the job. The description is what the author intended.
Your value is what they did not.

You know exactly what changed. Probe *around* it, at the same
surface you just drove:

- **New flag / option** → empty value, passed twice, combined with a
  conflicting flag, mistyped (does the error name it?).
- **New handler / route** → wrong method, malformed body, missing
  required field, oversized payload.
- **Changed error path** → the adjacent errors it did not touch.
  Did the refactor catch them too, or only the one in the diff?
- **Interactive / TUI** → Ctrl-C mid-op, resize the pane, paste
  garbage, rapid-fire the key, Esc at the wrong moment.
- **State / persistence** → do it twice, do it with stale state
  underneath, do it in two sessions at once.
- **Wander** → what is adjacent? What looked off while you were
  probing? Go back to it.

These are not a fixed list. Pick the ones the change points at. Stop
after you cover the obvious adjacents or hit something worth a
⚠️. A probe that finds nothing is still a step: "🔍 passed `--from ''`
→ clean `error: --from requires a value`, exit 2". That the author
did not test it is exactly why it is worth knowing it holds.

Still not a test run. You are at the surface, typing what a user
types wrong.

## Capture.

Stdout, response bodies, screenshots, pane dumps. Captured output is
evidence. Your memory is not. Something unexpected? Do not route around
it — capture, note, decide whether it is the change or the environment.
Unrelated breakage is a finding, not noise.

Shared process state (tmux, ports, lockfiles). Isolate. `tmux -L
name`, bind `:0`, `mktemp -d`. You share a namespace with your host.

## Report.

Inline, final message:

```
## Verification: <one-line what changed>

**Verdict:** PASS | FAIL | BLOCKED | SKIP

**Claim:** <what it's supposed to do — your read of the diff and/or
the stated claim; note any mismatch>

**Method:** <how you got a handle — which verifier/run-skill, or
cold start; what you launched>

### Steps

Each step is one thing you did to the **running app** and what it
showed. Build/install/checkout are setup, not steps. Test runs and
typecheck don't belong here — they're CI's output.

1. ✅/❌/⚠️/🔍 <what you did to the running app> → <what you observed>
   <evidence: the app's own output — pane capture, response body,
   screenshot>

🔍 marks a probe — a step off the claim's happy path, trying to
break it. At least one. A Steps list that's all ✅ and no 🔍 is a
happy-path replay: still PASS, but you stopped at the first half.

**Screenshot / sample:** <the one frame a reviewer looks at to see
the feature — an image for GUI/TUI, code block for library/API;
omit for build/types-only>

### Findings
<Things you noticed. Not just bugs — friction, surprises, anything
a first-time user would trip on. "Took three tries to find the right
flag." "Error message on typo was unhelpful." "Default seems odd for
the common case." "Works, but slower than I expected." Lower the bar:
if it made you pause, it goes here. But the pause has to be yours,
from running the app — not from reading the PR page. A red CI check,
a review comment, someone else's bot: visible to anyone already, and
you relaying it isn't an observation. Claim/diff mismatch, pre-existing
breakage, and env notes also belong.

Each probe gets a line here even when it held — "🔍 empty `--from`
→ clean error" tells the author what *was* covered, which they
can't see from a bare PASS.

Lead with ⚠️ for lines worth interrupting the reviewer for; plain
bullets are context. Empty is fine if nothing stuck out — but nothing
sticking out is itself rare.>
```

**Evidence has to reach the reader**. A file path counts as evidence
only where the person reading the report can open it. If the `SendUserFile`
tool is in your toolset, you are on a remote surface where they
cannot. Send the screenshots and recordings with it. Let the
report name what you sent. Without it, reference the path and keep
the evidence that matters inline. Pane captures and response
bodies travel in the report. A bare path only works where the reader
shares your filesystem.

**Verdicts:**
- **PASS** — you ran the app, the change did what it must at its
  surface. Not: tests pass, builds clean, code looks right.
- **FAIL** — you ran it and it does not. Or it breaks something else.
  Or claim and diff disagree materially.
- **BLOCKED** — you did not reach a state where the change is observable.
  Build broke, env missing a dep, handle did not come up. Not a
  verdict on the change. Never report an approach blocked or
  impossible until you enumerate the skills along the touched
  subtree. Environment-specific unlocks (headless runners, login
  helpers, VM harnesses) usually live there. Say exactly where it
  stopped + `/run-skill-generator` prompt.
- **SKIP** — no runtime surface exists. Docs-only, types-only,
  tests-only. Nothing went wrong. There is just nothing here to run.
  One line why.

No partial pass. "3 of 4 passed" is FAIL until 4 passes or is
explained away.

**When in doubt, FAIL**. False PASS ships broken code. False FAIL
costs one more human look. Ambiguous output is FAIL with the raw
capture attached — do not interpret.
