<!--
name: 'System Prompt: /loop tick (loop.md absent, dynamic pacing)'
description: >-
  Loop tick injection for dynamic self-paced autonomous checks while loop.md is
  absent, telling the model to re-arm the wakeup with the sentinel prompt so a
  recreated loop.md is picked up.
ccVersion: 2.1.321
variables:
  - WAKEUP_TOOL_NAME
  - LOOP_SENTINEL
-->
# /loop tick — loop.md absent (dynamic pacing)

loop.md is not currently present. Run the autonomous check using the loop instructions established earlier in this conversation.

You scheduled this tick via the ${WAKEUP_TOOL_NAME} tool (not a recurring cron). To keep the loop alive — and to pick up loop.md if it is recreated — call ${WAKEUP_TOOL_NAME} again this turn with `prompt` set to the literal sentinel `${LOOP_SENTINEL}` and `noop` set to `true` if this tick changed nothing (or `false` if it did) — otherwise the loop ends after this tick.
