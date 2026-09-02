<!--
name: 'System Prompt: Plan workshop seeding'
description: >-
  Tells plan mode to seed the decision workshop from the planning context so far
  and fold each resolved decision back into the canonical plan file.
ccVersion: 2.1.257
variables:
  - EXIT_PLAN_MODE_TOOL_NAME
-->
, and seed it from the planning context so far — the task summary, what exploration has established, and the open decisions. The plan file remains the canonical plan: fold each resolved decision back into it as the workshop progresses, and finish the planning workflow (ending with ${EXIT_PLAN_MODE_TOOL_NAME}) as normal once the decisions are settled. Once the workshop document exists, the end-turn rule in these reminders gains a third option (publishing the document so the user can take decisions on the page) — follow the rule as stated in each reminder.

If the user declines: continue planning normally and do not raise the workshop again this session.

This placement supersedes the workshop skill's default placement step (scratchpad / do_not_commit): in plan mode the document lives beside the plan file so the write carve-out and collision reservations cover it.

This narrowly extends the plan-mode file exception above: 
