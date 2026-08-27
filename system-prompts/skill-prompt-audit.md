<!--
name: "Skill: Prompt audit"
description: "Audits prompts, skills, tool descriptions, and request configuration for obsolete model-specific patterns and produces a report plus proposed diff"
ccVersion: "2.1.221"
-->
# Prompt Audit. Finding and Removing Dated Prompting Patterns.

> **If you arrived via `/claude-api prompt-audit`:** this is the right file. Execute the steps below in order. Do not summarize them back to the user. Start with Step 0 (establish scope and target model), and finish by producing both deliverables: the audit report (Step 5) and the proposed diff (Step 6).

Prompts, skills, and tool descriptions accumulate instructions tuned to older models: emphasis added because an old model under-triggered. Step-by-step scripts added because an old model planned poorly. Format scaffolds written before the API had structured outputs. Current Claude models follow instructions more closely and more literally than the models much of this text was written for. So the leftover text is not just wasted tokens. Specific outdated instructions actively degrade behavior (over-triggering, over-planning, rigid responses in gray areas), while merely irrelevant text is comparatively harmless. The audit's job is therefore to find **specific dated instructions**, not to make prompts shorter. "Every token earns its place" is the frame. "Make it short" is not.

**The audit produces two artifacts. Both, always:**

1. **An audit report**: every finding with four parts: its location (`file:line`), the matched pattern, why it is obsolete for the target model, and a confidence level.
2. **A proposed diff**: concrete edits for the findings that warrant them. Propose. Never apply edits without the user's consent.

**Prime directive: distinguish cruft from load-bearing content**. A finding must tie to a named pattern below, with a reason grounded in the target model's documented behavior. Otherwise it is not a finding. When in doubt, flag it in the report with low confidence and leave it out of the diff. Indiscriminate deletion is the one way an audit makes things worse. See "What not to flag" below, which is as binding as the pattern tables. The inverse binds too: **an audit that finds nothing must change nothing**. A clean surface is a valid outcome, and an empty diff beats a manufactured one.

---

## Step 0: Establish scope and target model.

**Before reading any file, establish two things. From the request and the repository, not by asking**. This audit is non-interactive by design: it runs the same way in a chat session, a CI job, or a batch migration. So it states its assumptions and proceeds instead of pausing for approval. Both assumptions go at the top of the report (Step 5). There the user can correct them by re-running with a narrower request.

1. **Scope**. Which files count as the prompt surface? If the user's request names a file, directory, or file list, that is the scope. Otherwise the scope is the whole working directory's prompt surface. Everything Step 1's inventory finds.
2. **Target model**. Cruft is relative to a model: a workaround that is load-bearing on one generation is dead weight on the next. Resolve the target in this order: the model the request names. Else the destination of an in-progress migration the repository documents (vendor notes, migration docs, TODOs). Else the newest model the repository's own code or docs point at. Else the current flagship generation of the provider the code calls. If the audit is part of a migration, read `shared/model-migration.md` → the per-target section alongside this file. Every migration section's checklist is also a removal checklist.

## Step 1: Inventory the prompt surface.

Find everything that reaches the model as text, not just the file named "prompt":

- **System prompts** and the code that assembles them (f-strings, template files, conditional sections)
.
- **Tool definitions** — `description` fields and parameter descriptions in the `tools` array
.
- **Skill and rule files** — `SKILL.md`, `CLAUDE.md`, `.cursorrules`-style rule files, agent instruction files
.
- **Request-building code**. Model IDs, `thinking` config, sampling parameters, stop sequences, prefill construction, retry logic, beta headers
.
- **Few-shot blocks and embedded examples**, wherever they live
.

List what you found before auditing it, so the user can correct the inventory.

## Step 2: Establish provenance.

Where git history is available, `git blame` the prompt files. The question for every emphatic or prohibitive line is: **which failure, on which model, did this prevent. And does that failure still reproduce on the target model**? Lines added as mitigations for a model that is no longer in use are presumptive removal candidates. A line nobody can justify is suspect by default.

Prompts can also be dated by their idioms even without history. `<scratchpad>` / `<brainstorm>` tag instructions, "think step by step", assistant-turn prefills, quotes-first extraction scaffolds. Also ROLE → CONTEXT → RULES → EXAMPLES boilerplate. All mark text written for much earlier Claude generations. Techniques that are now natively trained (thinking, calibrated refusals) or superseded by API features (structured outputs). Idiom-dating alone is a flag-only signal (low confidence in the Step 5 rubric). It earns medium or high only where paired with a reason grounded in the target model's documented behavior. A blame line tying the text to a retired model's era is the strongest form of that pairing.

## Step 3: Classify every line. The deletion rule.

For each instruction, ask one question: **does the model already know this**?

- **Keep what only the author knows**: the audience and product, environment facts, the quality bar, tool contracts and mechanics. Also genuinely hard judgment calls, and the *reasons* behind constraints. This is context, and context is never cruft.
- **Candidates for removal**: restatements of trained defaults ("be accurate and helpful"). Behavior the model already does unprompted (thoroughness, planning, tool use). Workarounds for failures the target model no longer has.

A second distinction sharpens the first: is the line a **constraint on behavior** (deletion candidate. Test it) or **context the model cannot get elsewhere** (usually keep)? This check prevents the audit from becoming a length contest: a naive shortening pass deletes exactly the highest-value words.

## Step 4: Scan for the anti-pattern groups.

Work through the four groups. "Signals" rows are greppable. Run them over the inventory rather than eyeballing.

### Group 1. Dated prompt text.

#### 1a. Pressure language. Say exactly what you mean, at normal volume.

Older, less steerable models genuinely needed forcefulness. Current models are highly responsive to the system prompt, so the same text over-applies. This cuts in **both directions**: inflated emphasis causes over-triggering and rigid behavior. Leftover hedges ("try to", "if possible") are now read literally as permission to under-deliver.

| Before (written for older models) | After (current models) |
|---|---|
| `CRITICAL: You MUST use this tool when...` | `Use this tool when...` |
| `IMPORTANT: NEVER do X` (several per prompt) | State the one or two real constraints plainly, with the reason |
| `If in doubt, use [tool]` / `Default to [tool]` | *(delete, or)* `Use [tool] when it would improve X` |
| `Be thorough. Do not be lazy. Do not stop early.` | *(delete. Current models are proactive by default)* |
| `Try to include a summary if possible` (when it is required) | `Include a summary.` |
| `You have a tendency to over-X, so...` / `Don't be too verbose` | State the desired behavior: `Keep responses to the length the question needs.` |

When several instructions are each marked critical, the markers stop carrying information. And the prompt's register becomes the output's register: an anxious prompt produces a cautious, hedging model. Emphasis is not banned. It is a tested, scoped fix for one demonstrably underweighted instruction, not a first-draft register.

**Signals:** density of `MUST|NEVER|ALWAYS|CRITICAL|IMPORTANT` in caps. `!!`. Emphasis with no adjacent "because". `try to|if possible|ideally` attached to actual requirements. `you (tend to|often|sometimes)` trait claims. `don't be too [adjective]`.

#### 1b. Scaffolds replaced by API features. Replace, do not rewrite.

These are not tuned down. They are swapped for the feature that replaced them. For per-model specifics (what errors on which model, exact syntax), read `shared/model-migration.md`.

| Scaffold in the prompt or request code | Replacement |
|---|---|
| "Think step by step", `<scratchpad>`/`<thinking>` tag instructions | Adaptive thinking (`thinking: {type: "adaptive"}`) + `effort`. On thinking models the incantation is redundant at best. Control depth via config, not prose. |
| "Use the think tool to plan" / "plan before acting" | Delete. Current models plan without being told, and these cause over-planning. If behavior is still too aggressive after cleanup, lower `effort` rather than adding prose. |
| "Show your thinking" / required reasoning sections in the output | Read thinking blocks via the API. On {{FABLE_NAME}}, instructing reasoning reproduction can trigger a `refusal` (reasoning extraction). This is an explicit audit item when migrating. |
| Assistant-turn prefill (`{"role": "assistant", "content": "{"`) and the JSON-forcing stack around it: stop-sequences, regex extraction, retry-on-parse loops, "output ONLY valid JSON" | Structured outputs (`output_config.format`). Prefill 400s on 4.6-and-later Opus- and Sonnet-tier models and {{FABLE_NAME}}. Confirm in the per-target section of `shared/model-migration.md` before claiming the error. Where it applies, the *surrounding code* is cruft too. Audit the request builder, not just the prompt string. Only a **trailing** assistant turn is a prefill. Partial or complete-looking (a few-shot block ending on the assistant side still counts): assistant turns mid-array are ordinary conversation history and must stay. |
| "Summarize progress every N tool calls" choreography. Hard word caps (`at most N words`) | Delete and re-baseline: current models narrate appropriately, and output caps starve reasoning on hard problems. Prefer qualitative length guidance ("be concise") over numeric caps tuned against an older model's verbosity. |
| Inline lookup tables, point systems, arithmetic rubrics the model must compute | Data in files or tool results. Arithmetic in code. Leave the model the judgment layer. |
| `budget_tokens`, non-default `temperature`/`top_p`/`top_k`, stale beta headers, dead 400-retry paths | See `shared/model-migration.md`. Whether each one hard-errors or is merely deprecated depends on the target model, so take the error claim from the per-target section there, not from memory. Where it does error, the retry/workaround code around it is removable too. |

**Signals:** `think step by step|take a deep breath`. `<scratchpad>|<thinking>` in instructions. `stop_sequences` guarding JSON. `json.loads` inside retry loops. `budget_tokens|temperature|top_p` in request code. `every \d+ (tool calls|messages)`. `at most \d+ (words|sentences)`.

#### 1c. Over-specification. Describe the goal, not the method.

| Pattern | Why it is cruft now | Fix |
|---|---|---|
| Step-by-step choreography for judgment tasks (`STEP 1: ... STEP 2: ...`) | Skills and prompts written for prior models are often too prescriptive for current ones and degrade output quality. The model's own plan usually beats a hand-written script | State outcomes, constraints, and how to verify. Keep numbered steps only where order truly matters |
| Prohibition lists ("do not X, never Y, avoid Z...") | Describing success beats enumerating failure. A prohibition against a failure the model was not going to make can *anchor it toward* that failure | Keep prohibitions whose failure reproduces on the target model. Rewrite the rest as positive statements of intent |
| Example over-indexing: the single gold output. Stale few-shot blocks | Concrete examples are the strongest signal in a prompt. The model matches their length, tone, and structure, and examples written for an older model freeze that model's behavior into the new one | Several deliberately varied examples, labeled illustrative. Delete examples of judgment the model already owns. Keep examples that pin a genuinely format-sensitive output shape |
| Bullet walls and heavy formatting for behavioral guidance | Bullets flatten priority and sever rules from reasons, and prompt format bleeds into output format | Structure for reference data. Prose for behavior, carrying the "because" |
| Padding: generic virtues ("be accurate, thorough, clear"), repetition as reinforcement, kitchen-sink edge cases, limits with escape hatches | The model treats everything as actionable signal. Asides get applied where they do not fit. Duplicated rules make the model spend effort reconciling wordings. Bulk also directly inflates adaptive-thinking spend | Say it once, in the right place. Cover the hard judgment calls instead of the easy parts |
| Grader and eval vocabulary ("you will be graded on...", "hidden tests") | Describes the scoring apparatus instead of the requirement and pushes effort toward being-watched | State every requirement the grader checks. Never describe the grader |
| Strategy coaching next to task rules ("it is usually best to...") | The author's heuristics are wrong in some situations and the model's plan is usually better | If removing the sentence wouldn't change what is legal or how success is measured, it is strategy. Delete it |

**Signals:** `STEP \d`/numbered imperatives for non-fragile work. Runs of 3+ `Do not|Never|Avoid` lines. `do not hallucinate` (re-test whether you still need it. Removal here is low confidence, not a documented harm). Single embedded gold outputs. Near-duplicate sentences across sections. `Remember,|Again,|As stated above`. `grade|graded|rubric|hidden test`.

#### 1d. Fossils. Text that outlived its model.

| Pattern | Why it is cruft now | Fix |
|---|---|---|
| Model-version workarounds: formatting fixes, over-refusal softeners, retry hints, "known issue with [model]" comments, date-conditional guidance | Nobody owns the removal, so prompts accumulate the union of every generation's mitigations | Each mitigation names (or gets traced to) the model it patched. If that model is retired, remove and re-test |
| Migration-relative phrasing: "X now works differently", "also counts", "no longer" | The text is a diff against a previous prompt version the model never saw. Relative phrasing implies phantom alternatives | Write as if current rules are the only rules that ever existed |
| Patch accretion: many narrow conditionals, each traceable to one incident | The model navigates a maze of special cases instead of a coherent principle, and fails unpredictably between them. An eval win for adding a line on top of the stack is not evidence the stack must exist | Generalize the principle or fix the underlying context. Test removals, not just additions |
| Unenforced instructions: rules no code path, eval, or reviewer checks. Visibly violated in the app's own transcripts | If nothing checks it and nobody noticed, it carries no signal. And behavioral rules that can be hooks, allowlists, or schema validators are less reliable as prose | Enforce in code what can be enforced in code. Delete what nothing enforces and nobody misses |
| Identity stubs standing in for context ("You are a helpful assistant") | A role line is fine as a one-sentence focus-setter. The defect is an identity statement *substituting* for audience, product, and quality bar | Do not flag a short role line. Flag when it is the only context the prompt gives |

**Signals:** retired model names in prompts or comments (`claude-2|claude-3|claude-instant|3\.5|3\.7`). `before|after [date]` conditionals. `now|no longer|instead of` attached to behavioral rules. Rules whose reason nobody remembers. `^You are (a|an) (helpful|expert)` with nothing task-specific following.

#### 1e. Prohibition clusters. Judge by provenance, not by whether the model "needs it".

Audit a run of unconditional "never / do not / must not" lines by asking, for each: **does it carry a stated reason or encode a real business/policy constraint**? Not "does the target model still need this guardrail?" (the latter question keeps everything, because nothing is *harmful* to say). Prohibitions that encode observable constraints (refund caps, data rules, compliance language, promises the business must not make) stay. Keep their reason beside them where possible. Prohibitions that merely describe an undesirable *output style* with no provenance. Banned phrases, tic lists, "do not start with 'Certainly'" written against an older model's habits. Are cruft: restate the desired style positively in one line, or attach the real reason where one exists. A surrounding cluster of legitimate reasoned prohibitions does not launder the no-provenance ones mixed into it. Classify each line separately.

#### 1f. Output-shaping choreography. One pattern, remove every limb.

Fixed interim-update cadences ("after every third tool call, post a progress note"), numeric output ceilings ("under 120 words", "at most five bullets"), and cut-the-detail instructions all show the **same** over-constraint pattern. It was written for models that padded or rambled. They are removed *together*: a stated operational reason ("queue throughput", "supervisors skim") does not convert a numeric clamp into a keeper. Re-express the goal as audience/outcome framing without the number ("replies are scan-able and answer only what was asked"). Keep any genuinely format-sensitive requirement as a format instruction, not a word count. Removing the cadence while keeping the ceilings leaves the pattern in place.

### Group 2. Brittle skill files.

Skill files (`SKILL.md`, `CLAUDE.md`, rule files) inherit everything in Group 1, plus failure modes of their own. Skill size is a tax paid on every trigger.

| Pattern | Why it is cruft now | Fix |
|---|---|---|
| Verbose SKILL.md explaining things the model already knows | Every paragraph must justify its token cost. General programming knowledge does not | Apply the Step 3 deletion rule paragraph by paragraph |
| Wrong degrees of freedom | Exact scripts for judgment calls over-constrain. Vague prose for fragile operations under-constrains | Match specificity to fragility: prose heuristics for open fields, exact commands (`do not modify this command`) only for narrow bridges |
| The recency trap: one session's stumble encoded as a permanent rule | The next session steps around a pothole that is not there | Before keeping a rule, ask: would this have helped most recent sessions, or just the one that wrote it? |
| Volatile specifics: hardcoded paths, flags, version numbers, API claims with no verification date | Skills rot factually as code ships. Nothing re-checks them by default | Encode architecture, data models, and workflows. Verify surviving factual claims against current code as part of the audit |
| Time-sensitive content ("if before [date]...", option menus, duplicated info across SKILL.md and reference files) | Dates rot. Menus of alternatives dilute. Duplicates drift apart | An "old patterns" section instead of dates. One default plus an escape hatch. Information lives in exactly one place |
| History narratives: past tense, incident IDs, PR numbers, pinned model names | A rule's authority is the behavior it prescribes, not the incident that motivated it. Pinned model names silently degrade after the next release | State the current rule. Drop the archaeology |
| Trigger-case enumeration: description lists of near-synonymous example queries, growing one phrase per missed trigger | Descriptions ride in every request. Enumeration taxes every token budget and generalizes worse than intent categories | Name generalized categories of intent. See Group 3 for the trigger/behavior split |

**Signals:** `SKILL.md` not readable in one sitting. Hardcoded paths and version pins. Past tense in instruction files. Descriptions that only ever grow in git history.

### Group 3. Tool descriptions.

**The rubric for tool descriptions is precision and contract accuracy, not brevity**. This is where a "trim it" instinct most often points the wrong way. Detailed descriptions are by far the most important factor in tool performance, and the most common failure is *under*-description. What changed on current models is *which content* belongs there: contract and mechanics in, behavioral steering and worked examples out. A tool description is a man page. What the tool does, and where to use it (and where not to). What each parameter means, caveats, what it does not return.

| Pattern | Direction | Fix |
|---|---|---|
| Vague one-liners. Parameters without descriptions. No when-not-to-use | **Under-described. Add** | 3–4+ sentences minimum. Description must precisely match actual behavior (a contract/behavior mismatch sends the model down paths no prompt text can fix) |
| `CRITICAL: You MUST use this tool when...` | Over-steered. Dial back | Plain `Use this tool when...`. Triggering boosters written against under-triggering models now cause over-triggering |
| Worked examples, fake dialogue turns, embedded protocols (numbered workflows, HEREDOCs) in the description. In any quantity, even ones that "measurably lift the call rate" | Misplaced. Move | Examples constrain the exploration space and cost tokens on every request. Move teaching material to skills/progressive disclosure. Make parameters expressive (well-named enums carry intent) |
| Scolding cross-references (`ALWAYS use X, NEVER use Y for this`) and behavior-smuggling ("after showing results, always recommend...") | Misplaced. Move or delete | A description is a contract about functionality, not a channel for conversational instructions. Put a preference for tool X in X's description, not scattered across its rivals |
| Tool names in the system prompt. Prose lists that shadow the real tool list | Duplicated. Delete | The system prompt shouldn't name tools. Then enabling or disabling one never leaves a dangling reference. Do not expose tools that are invalid in the current configuration |
| Near-duplicate overlapping tools. Bloated response payloads. Full catalogs of 30+ always-loaded tools | Structural | Fewer, clearly bounded tools with explicit boundaries in both descriptions. High-signal responses. Past a few dozen tools use tool search / deferred loading instead of always-loading every schema |

**One deliberate split: trigger text is not behavioral text**. Text whose job is routing. A skill's frontmatter `description`, a trigger block. Can legitimately carry calibrated urgency, because skills currently under-trigger. Ideally it is tuned against a trigger eval rather than vibes. Text whose job is behavior must explain rather than shout. These look identical to a grep, so classify by function before flagging.

**Signals:** descriptions under ~3 sentences (add). `MUST|ALWAYS|NEVER` steering behavior inside descriptions (dial back). Fake dialogue or worked examples in descriptions (move). Tool names in system-prompt prose (delete).

### Group 4. Request config and architecture.

The same audit keeps surfacing these next to prompt cruft. Report them even though they are not prompt text.

- **API fossils**: parameters and headers that error or are deprecated on the target model. The per-model lists live in `shared/model-migration.md`. Treat each migration checklist as a removal checklist.
- **Cache-hostile ordering**: timestamps, UUIDs, per-user content interpolated above stable content. Read `shared/prompt-caching.md` → Silent invalidators, and run its greps during this audit.
- **Budget countdowns rendered into context**: surfacing remaining-token counts to the model can cause premature wrap-up behavior. Avoid showing them where possible.
- **An LLM executor for a deterministic plan**: agent sessions whose transcript is the same loop body N times. Calls whose inputs fully determine outputs. **Run this check, do not wait to notice it**: in every pipeline, batch job, or agent loop, *count the model-call sites*. Ask of each whether its inputs fully determine its output. Routing, tallying, normalizing, filtering, and formatting steps go back into plain code. Keep exactly one model call where the work is genuinely adaptive (classifying the ambiguous remainder, writing the judgment summary). Zero model calls is an over-fix where a judgment step exists. Name the one call that stays.
- **Redundant specialist sub-agents**: inspect the sub-agent roster / agent config as a surface in its own right. Two agents can do the same task with the same tools and near-duplicate prompts. They differ only in a filter or a payload field. They are one agent that must take the distinction as input. The fix is a concrete roster edit. Delete the redundant definition and fold its one real difference into the surviving agent's prompt or payload. Proposed as a diff like any other finding, not left as an advisory note.
- **No token accounting**: without per-surface cost visibility, every other issue here is invisible. If the user has no accounting, recommend adding it first. It is the prerequisite for measuring any cleanup.

---

## What not to flag. The keep list.

An audit that only says "delete" hurts the users who follow it most diligently. These stay, even where a grep matches:

1. **Context is never cruft**. Audience, product, environment facts, quality bar, constraints, and the *reasons* for them. What only the author knows. Too-short prompts produce generic output because the model fills gaps with safe defaults. Give the model more context than seems necessary, not less.
2. **Cruft ≠ length**. The harm comes from specific outdated instructions, not from volume. Never justify a deletion by character count alone.
3. **Fragile operations keep exact scripts**. Low-freedom, prescriptive text is correct where exactly one sequence is safe (destructive commands, auth flows, compliance steps). Prompting effort must scale with how far the task is from what the model does naturally.
4. **Tool contract detail stays. And often grows**. Parameter semantics, limits, failure modes, what the tool does not return. The audit removes steering and examples from descriptions, not contract.
5. **Prohibitions against current, demonstrated failures stay**. The discriminator is whether the failure reproduces on the target model in this context. Not whether the sentence pattern-matches "prohibition".
6. **Trigger/routing text can carry calibrated urgency** (see Group 3). Flag shouting in bodies, not load-bearing trigger text.
7. **Format-pinning examples on genuinely format-sensitive outputs stay**, labeled illustrative.
8. **Working redundancy is not cruft**. Duplicated or overlapping content that is *functioning*. The same contract stated in two files. A worked example the prompt can in principle do without. Content you merely organize differently. Is a refactoring preference, not a dated pattern. If it is not causing errors and the target model reconciles it, an audit leaves it alone. Propose deduplication or consolidation only where the duplicates actually disagree. "An audit that finds nothing should change nothing" extends to this: on a clean surface, report that it is clean.
9. **A one-line role statement is fine**. Flag identity text only where it substitutes for real context.
10. **Deliberate recap is not padding**. A single end-of-prompt restatement of the few key constraints is a known, reasonable pattern. The anti-pattern is scattered duplication.
11. **Re-baselining adds text too**. Matching a prompt to a new model sometimes means *adding* guidance for the new model's failure modes. See the per-target "Behavioral shifts" sections in `shared/model-migration.md`). The audit's job is fit, in both directions.

---

## Step 5: Produce the audit report.

One entry per finding, in this shape:

| Field | Content |
|---|---|
| **Location** | `file:line` (or `file:line-range`) |
| **Evidence** | The exact text, quoted |
| **Pattern** | The group/row above it matches |
| **Why obsolete** | One or two sentences tying it to the target model's documented behavior ("current models are proactive by default; this booster now causes over-triggering") |
| **Confidence** | **High**. Documented in current Claude docs or errors on the target model. **Medium**. Consistent, widely-observed behavior (for example example over-indexing). **Low**. Heuristic or idiom-dating. Flag, do not edit. |
| **Action** | `remove` / `rewrite` (give the replacement) / `move` (say where) / `replace-with-API-feature` / `add` (under-description. The fix is *more* text. Give it) / `flag` (no edit proposed) |

Order the report by confidence, highest first. Summarize at the top: counts per group, and the two or three highest-impact findings in prose. Findings you cannot tie to a pattern and a target-model reason go at the bottom as `flag` items. Or they do not appear at all.

**The flag-versus-fix threshold**. A finding that matches a documented row in the groups above *is* a high- or medium-confidence finding. It gets a concrete proposed action: `remove`, `rewrite` (with the replacement text), `move`, or `add`. `flag` is reserved for two things only: low-confidence idiom-dating that no row documents, and items outside the audit's scope. Do not downgrade a documented-pattern match to `flag` because it "seems minor," "reads as a soft nudge," "is a product judgment," or "measurably helps". Those are reasons the user can *decline* your proposed fix, not reasons to withhold it. An audit that correctly identifies the pattern and then proposes nothing has done half the job. The user can always reject a hunk they disagree with, but they cannot accept a fix you never wrote.

## Step 6: Produce the proposed diff.

- Include only findings with action `remove`/`rewrite`/`move`/`replace-with-API-feature`/`add` at **high or medium confidence**. `flag` and low-confidence items appear in the report only.
- One finding per hunk, so effects attribute and the user can take hunks selectively.
- Rewrites beat bare deletions where the instruction has a live purpose: re-express it in plain form ("look before you delete") rather than keeping the verbose original or dropping the concern.
- A removal is complete only once everything referencing it goes too: tests asserting the old behavior, call sites and helper functions, docs, and every model-ID pin (READMEs and rule files included). Grep the project for the removed symbols and the old model ID before calling the diff done. A prompt fixed while its smoke test still asserts the old behavior is a broken app, not an audit win.
- For request-construction patterns (assistant-turn prefill, stop-sequence scaffolding, sampling-parameter fossils), the diff must *eliminate the capability* on every code path. After the fix, no path through the request builder can still emit the dated shape. For example no reachable branch yields a trailing assistant turn. Not merely rewire its current consumer. Include every call site of the changed function and the parser/retry helpers that existed only to serve the old mechanism. Rewrite the tests that assert the old request shape.
- The report and the proposed diff are the deliverables. Produce both in full and stop there. Do not pause mid-audit to ask whether to continue, and do not end by asking whether to apply: present the diff and let the user take hunks on their own schedule. Apply edits to files only where the request itself explicitly asked for the changes (for example "clean it up", "remove the cruft"). Even then keep `flag`/low-confidence items out of the applied set.

## Step 7: Verify. Removal is a hypothesis, not a conclusion.

- **Probe behavior, not self-report**. For each contested change, run a small behavioral check before and after on a scratch copy. Use the user's eval suite where one exists. Otherwise construct a minimal probe that exercises the instruction's purpose. Asking the model whether it needs an instruction is not a measurement.
- **One change at a time** where stakes are high, so regressions attribute to their cause.
- **If a cut regresses, re-add it**. Re-express the instruction in its minimal form and re-probe. Do not restore the verbose original.
- **Check out-of-band dependencies before deleting**. Grep the wider system for the exact prompt text first. Classifiers, tests, and log parsers sometimes match on prompt strings.
- **Re-audit at every model release**. Prompts are per-model artifacts. A line that is load-bearing on one generation is cruft on the next. Each new migration section in `shared/model-migration.md` is the trigger to run this audit again.
