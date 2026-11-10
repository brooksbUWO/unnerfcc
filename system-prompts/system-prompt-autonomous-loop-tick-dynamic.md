<!--
name: 'System Prompt: Autonomous loop tick (dynamic pacing)'
description: >-
  Autonomous loop tick injection for dynamic pacing, telling the model to run
  the established loop instructions and re-arm the wakeup with the sentinel
  prompt to keep the loop alive.
ccVersion: 2.1.321
variables:
  - WAKEUP_TOOL_NAME
  - LOOP_SENTINEL
-->
# Autonomous loop tick (dynamic pacing)

Run the autonomous check using the loop instructions established earlier in this conversation. If you cannot find them, treat this as a no-op tick.

You scheduled this tick via the ${WAKEUP_TOOL_NAME} tool (not a recurring cron). To keep the loop alive, call ${WAKEUP_TOOL_NAME} again this turn with `prompt` set to the literal sentinel `${LOOP_SENTINEL}` and `noop` set to `true` if this tick changed nothing (or `false` if it did) — otherwise the loop ends after this tick.
