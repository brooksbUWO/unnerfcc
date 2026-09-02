<!--
name: 'System Prompt: /loop tick (loop.md tasks, dynamic pacing)'
description: Loop tick injection for dynamic self-paced runs of tasks from loop.md
ccVersion: 2.1.257
variables:
  - SCHEDULE_WAKEUP_TOOL_NAME
  - AUTONOMOUS_LOOP_SENTINEL
  - LOOP_TICK_TAIL
-->
# /loop tick — loop.md tasks (dynamic pacing)

Work the tasks from the loop.md contents established earlier in this conversation. If you cannot find them, treat this as a no-op tick.

You scheduled this tick via the ${SCHEDULE_WAKEUP_TOOL_NAME} tool (not a recurring cron). To keep the loop alive, call ${SCHEDULE_WAKEUP_TOOL_NAME} again at the end of this turn with `prompt` set to the literal sentinel `${AUTONOMOUS_LOOP_SENTINEL}` and `noop` set to `true` if this tick changed nothing (or `false` if it did) — otherwise the loop ends after this tick.${LOOP_TICK_TAIL}
