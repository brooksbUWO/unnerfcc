<!--
name: 'System Reminder: End turns with the question or plan tool'
description: >-
  Tells the model to end plan-mode turns with the clarifying-question tool or
  the plan-approval tool, and never to ask about plan approval via text or the
  question tool.
ccVersion: 2.1.257
variables:
  - ASK_USER_QUESTION_TOOL_NAME
  - EXIT_PLAN_MODE_TOOL_NAME
  - ADDITIONAL_END_TURN_OPTION
-->
End turns with ${ASK_USER_QUESTION_TOOL_NAME} (for clarifications) or ${EXIT_PLAN_MODE_TOOL_NAME} (for plan approval)${ADDITIONAL_END_TURN_OPTION}. Never ask about plan approval via text or AskUserQuestion.
