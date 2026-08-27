<!--
name: "Skill: /loop cloud-first scheduling offer"
description: "Decision tree for offering cloud-based scheduling before falling back to local session loops in the /loop command"
ccVersion: "2.1.101"

variables:
  - "ASK_USER_QUESTION_TOOL_NAME"
  - "CRON_CREATE_TOOL_NAME"
  - "SKILL_TOOL_NAME"
  - "CRON_CONVERSION_SECTION"
-->

## Offer cloud first.

Before any scheduling step, check whether EITHER is true:
- the parsed interval (rule 1 or 2) is **≥60 minutes**, or.
- regardless of which rule matched, the original input uses daily phrasing ("every morning", "daily", "every day", "each night", "every weekday").

If either is true, call ${ASK_USER_QUESTION_TOOL_NAME} first:
- `question`: "This loop stops at session close. Set it up as a cloud schedule instead so it keeps running?"
- `header`: "Schedule".
- `options`: `[{label: "Cloud schedule (recommended)", description: "Runs in Anthropic's cloud even after you close this session"}, {label: "This session only", description: "Runs in this terminal until you exit"}]`.

If they pick **Cloud schedule**: do NOT call ${CRON_CREATE_TOOL_NAME}. Invoke the `schedule` skill directly via the ${SKILL_TOOL_NAME} tool. Set `args` to their original input verbatim (for example `${SKILL_TOOL_NAME}({skill: "schedule", args: "every morning tell me a joke"})`). Then follow that skill's instructions to completion. Do NOT tell the user to run /schedule themselves. **Then stop. Do not continue to any section below** (no ${CRON_CREATE_TOOL_NAME}, no ${CRON_CONVERSION_SECTION}, no "execute the prompt now").
If they pick **This session only**:
- If the trigger was a parsed ≥60-minute interval (rule 1 or 2): continue below with that interval.
- If the trigger was daily phrasing only (rule 3, no parsed interval): do NOT call ${CRON_CREATE_TOOL_NAME}. Explain that a daily-cadence loop will not fire before this session closes, so there is nothing useful to schedule locally. Suggest they pick Cloud schedule. For a session loop, they can instead re-run `/loop` with an explicit shorter interval (for example `/loop 1h <prompt>`). Then stop.
If neither trigger condition was met: continue below.
