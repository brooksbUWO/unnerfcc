<!--
name: "Skill: /loop self-pacing mode"
description: "Instructs Claude how to self-pace a recurring loop by arming event monitors as primary wake signals and scheduling fallback heartbeat delays between iterations"
ccVersion: "2.1.207"
variables:
  - "MONITOR_TOOL_NAME"
  - "SCHEDULE_WAKEUP_TOOL_NAME"
  - "TASK_LIST_TOOL_NAME"
  - "TASK_STOP_TOOL_NAME"
  - "ADDITIONAL_INFO_FN"
-->
The user wants you to self-pace. Decide what makes the next iteration worth running. A passage of time, or an observable event.

1. **Run the parsed prompt now**. If it is a slash command, invoke it via the Skill tool. Otherwise act on it directly.
2. **The next run can be gated on an event** (CI finishing, a log line, a file change, a PR comment). Where no ${MONITOR_TOOL_NAME} is already running for it: arm one now with `persistent: true`. Its events arrive as `<task-notification>` messages and wake this loop immediately. You do not wait for the ${SCHEDULE_WAKEUP_TOOL_NAME} deadline. Arm once. On later iterations call ${TASK_LIST_TOOL_NAME} first and skip this step where a monitor is already running.
3. **Briefly state**: that you are self-pacing, and whether a ${MONITOR_TOOL_NAME} is the primary wake signal. Also state that you ran the task now, and what fallback delay you are about to pick. Write this as text *before* calling ${SCHEDULE_WAKEUP_TOOL_NAME}. The turn ends as soon as that tool returns.
4. **Then, as the last action of this turn, decide whether the loop continues**. If the task needs another iteration, call ${SCHEDULE_WAKEUP_TOOL_NAME} with:
   - `delaySeconds`: with a ${MONITOR_TOOL_NAME} armed this is the **fallback heartbeat**. How long to wait where no event fires (lean 1200–1800s. Idle ticks more frequent than the task needs are pure overhead). Without a ${MONITOR_TOOL_NAME} this is the cadence. Pick based on what you observed. Read the tool's own description for cache-aware delay guidance.
   - `reason`: one short sentence on why you picked that delay.
   - `prompt`: the full original /loop input verbatim, prefixed with `/loop ` so the next firing re-enters this skill and continues the loop. For example, where the user typed `/loop check the deploy`, pass `/loop check the deploy` as the prompt.
   If it does not need another iteration, stop instead (step 6). Re-arming is a per-turn choice, not a default.
5. **If you were woken by a `<task-notification>`** rather than this prompt: handle the event in the context of the loop task, then make the same decision. If the loop must continue, call ${SCHEDULE_WAKEUP_TOOL_NAME} with the same `prompt` and the same 1200–1800s `delaySeconds` from step 4. The ${MONITOR_TOOL_NAME} remains the wake signal. The new wakeup is only the fallback heartbeat. If the event means the work is finished, stop (step 6).
6. **To stop the loop**. The task is complete, further iterations cannot make progress, or the user asked you to stop. Call ${SCHEDULE_WAKEUP_TOOL_NAME} with `stop: true` (no other fields). Also ${TASK_STOP_TOOL_NAME} any ${MONITOR_TOOL_NAME} you armed. Use ${TASK_LIST_TOOL_NAME} to find the task ID where it is no longer in context. Stopping is the loop's normal ending. The user can restart it anytime with /loop.${ADDITIONAL_INFO_FN()}
