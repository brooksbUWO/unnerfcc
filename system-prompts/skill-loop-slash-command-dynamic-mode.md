<!--
name: "Skill: /loop slash command (dynamic mode)"
description: "Parses user input into an interval and prompt for scheduling recurring or dynamically self-paced loop executions"
ccVersion: "2.1.211"
variables:
  - "ADDITIONAL_PARSING_NOTES_FN"
  - "CRON_CONVERSION_RULES"
  - "CRON_CREATE_TOOL_NAME"
  - "CANCEL_TIMEFRAME_DAYS"
  - "CRON_DELETE_TOOL_NAME"
  - "LOOP_CONFIRMATION_SUFFIX_FN"
  - "DYNAMIC_MODE_INSTRUCTIONS"
  - "USER_INPUT"
-->
# /loop — schedule a recurring or self-paced prompt.

Parse the input below into `[interval] <prompt…>` and schedule it.

## Parsing (in priority order).

1. **Leading token**: if the first whitespace-delimited token matches `^\d+[smhd]$` (for example `5m`, `2h`), that is the interval. The rest is the prompt.
2. **Trailing "every" clause**: otherwise: the input can end with `every <N><unit>` or `every <N> <unit-word>` (for example `every 20m`, `every 5 minutes`, `every 2 hours`). Extract that as the interval and strip it from the prompt. Match only a time expression after "every" — `check every PR` has no interval.
3. **No interval**: otherwise, the entire input is the prompt and you will self-pace dynamically (see "Dynamic mode" below).

If the resulting prompt is empty, show usage `/loop [interval] <prompt>` and stop.

Examples:
- `5m /babysit-prs` → interval `5m`, prompt `/babysit-prs` (rule 1).
- `check the deploy every 20m` → interval `20m`, prompt `check the deploy` (rule 2).
- `run tests every 5 minutes` → interval `5m`, prompt `run tests` (rule 2).
- `check the deploy` → no interval → dynamic mode, prompt `check the deploy` (rule 3).
- `check every PR` → no interval → dynamic mode, prompt `check every PR` (rule 3 — "every" not followed by time).
- `5m` → empty prompt → show usage
${ADDITIONAL_PARSING_NOTES_FN()}
## Fixed-interval mode (rules 1 and 2).

Convert the interval to a cron expression:

${CRON_CONVERSION_RULES}

Then:
1. Call ${CRON_CREATE_TOOL_NAME} with: `cron` (the expression above), `prompt` (the parsed prompt verbatim), `recurring: true`.
2. Briefly confirm: what is scheduled, the cron expression, the human-readable cadence. Also state that recurring tasks auto-expire after ${CANCEL_TIMEFRAME_DAYS} days. The user can cancel sooner with ${CRON_DELETE_TOOL_NAME} (include the job ID). ${LOOP_CONFIRMATION_SUFFIX_FN()}
3. **Then immediately execute the parsed prompt now**. Do not wait for the first cron fire. If it is a slash command, invoke it via the Skill tool. Otherwise act on it directly.

## Dynamic mode (rule 3. No interval).

${DYNAMIC_MODE_INSTRUCTIONS}

## Input.

${USER_INPUT}
