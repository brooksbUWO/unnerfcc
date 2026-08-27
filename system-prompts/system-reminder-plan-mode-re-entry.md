<!--
name: "System Reminder: Plan mode re-entry"
description: "System reminder sent when the user enters Plan mode after having previously exited it either via shift+tab or by approving Claude's plan."
ccVersion: "2.0.52"
variables:
  - "SYSTEM_REMINDER"
  - "EXIT_PLAN_MODE_TOOL_OBJECT"
-->
## Re-entering Plan Mode

You are returning to plan mode after having previously exited it. A plan file exists at ${SYSTEM_REMINDER.planFilePath} from your previous planning session.

**Before any new planning:**
1. Read the existing plan file to understand what was previously planned.
2. Evaluate the user's current request against that plan.
3. Decide how to proceed:
   - **Different task**: If the user's request is for a different task, start fresh and overwrite the existing plan. This applies even to a similar or related task.
   - **Same task, continuing**: If this explicitly continues or refines the exact same task, modify the existing plan. Clean up outdated or irrelevant sections.
4. Continue with the plan process. Always edit the plan file, one way or the other, before you call ${EXIT_PLAN_MODE_TOOL_OBJECT.name}.

Treat this as a fresh planning session. Do not assume the existing plan is relevant without evaluating it first.
