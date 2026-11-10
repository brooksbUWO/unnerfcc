<!--
name: 'Skill: Schedule recurring cron and run immediately'
description: >-
  Converts an interval to a cron expression, schedules the recurring task with
  the sentinel prompt, confirms it, and then runs the task at once without
  waiting for the first cron fire.
ccVersion: 2.1.321
variables:
  - PREFIX
  - INTERVAL
  - CRON_CREATE_TOOL_NAME
  - LOOP_SENTINEL
  - SENTINEL_EXPLANATION
  - CONFIRMATION_DETAILS
  - TICK_INSTRUCTIONS_NAME
  - TICK_INSTRUCTIONS
  - EXTRA_SECTION
  - TRAILING_NOTE
-->
${PREFIX}

## Action

1. Convert `${INTERVAL}` to a 5-field cron expression. Supported suffixes: `s` → ceil to nearest minute, `m` (minutes), `h` (hours), `d` (days). Examples: `5m` → `*/5 * * * *`, `1h` → `0 * * * *`, `1d` → `0 0 * * *`. If the interval doesn't cleanly divide its unit, round to the nearest clean interval and tell the user what you rounded to.
2. Call ${CRON_CREATE_TOOL_NAME} with:
   - `cron`: the expression from step 1
   - `prompt`: the literal string `${LOOP_SENTINEL}` — ${SENTINEL_EXPLANATION}
   - `recurring`: `true`
3. Confirm thoroughly: ${CONFIRMATION_DETAILS}
4. **Then immediately run ${TICK_INSTRUCTIONS_NAME} now**, following the instructions inlined below. Don't wait for the first cron fire.
${TICK_INSTRUCTIONS}
${EXTRA_SECTION}

${TRAILING_NOTE}
