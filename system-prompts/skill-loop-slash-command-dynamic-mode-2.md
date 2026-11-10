<!--
name: 'Skill: /loop slash command (fixed-interval mode)'
description: >-
  Fixed-interval branch of the /loop command — converts the interval to a cron
  expression, schedules the recurring task, and confirms the cadence, expiry and
  cancel path to the user.
ccVersion: 2.1.321
variables:
  - PREFIX
  - CRON_CONVERSION_RULES
  - CRON_CREATE_TOOL_NAME
  - RECURRING_EXPIRY_DAYS
  - CRON_DELETE_TOOL_NAME
-->
${PREFIX}
## Fixed-interval mode (rules 1 and 2)

Convert the interval to a cron expression:

${CRON_CONVERSION_RULES}

Then:
1. Call ${CRON_CREATE_TOOL_NAME} with: `cron` (the expression above), `prompt` (the parsed prompt verbatim), `recurring: true`.
2. Confirm thoroughly: what's scheduled, the cron expression, the human-readable cadence, any rounding you applied and why, that recurring tasks auto-expire after ${RECURRING_EXPIRY_DAYS} days, and that the user can cancel sooner with ${CRON_DELETE_TOOL_NAME} (include the job ID). Give the user enough information to understand exactly what will run and when.
