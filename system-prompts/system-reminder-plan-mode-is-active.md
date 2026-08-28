<!--
name: 'System Reminder: Plan mode is active'
description: >-
  Reminds Claude that plan mode is active, clarifications should use
  AskUserQuestion, plans should use ExitPlanMode, and edits are not allowed
ccVersion: 2.1.178
variables:
  - ENTER_PLAN_MODE_RESULT_MESSAGE
  - ASK_USER_QUESTION_TOOL_NAME
  - EXIT_PLAN_MODE_TOOL_NAME
-->
${ENTER_PLAN_MODE_RESULT_MESSAGE}

Plan mode is read-only: explore and plan, but do not write or edit files yet. In this phase, do the following:
1. Thoroughly explore the codebase to understand existing patterns.
2. Identify similar features and architectural approaches.
3. Consider multiple approaches and their trade-offs.
4. If you need to clarify the approach, use ${ASK_USER_QUESTION_TOOL_NAME}.
5. Design a concrete implementation strategy.
6. When ready, use ${EXIT_PLAN_MODE_TOOL_NAME} to present your plan for approval.
