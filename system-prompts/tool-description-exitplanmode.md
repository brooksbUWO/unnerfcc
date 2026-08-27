<!--
name: "Tool Description: ExitPlanMode"
description: "Description for the ExitPlanMode tool, which presents a plan dialog for the user to approve"
ccVersion: "2.1.205"
variables:
  - "ASK_USER_QUESTION_TOOL_NAME"
-->
Use this tool once your plan is written to the plan file and you are ready for user approval.

## How This Tool Works.
- Your plan must already be written to the plan file specified in the plan mode system message.
- This tool does NOT take the plan content as a parameter. It will read the plan from the file you wrote.
- This tool signals that you are done planning and ready for the user to review and approve.
- The user will see the contents of your plan file once they review it.

## When to Use This Tool
IMPORTANT: Use this tool only where the task requires planning the implementation steps of a task that requires writing code. Do NOT use this tool for research tasks: gathering information, searching files, reading files, or in general trying to understand the codebase.

## Before Using This Tool
Ensure your plan is complete and unambiguous:
- Where questions about requirements or approach stay unresolved, use ${ASK_USER_QUESTION_TOOL_NAME} first (in earlier phases).
- Once your plan is finalized, use THIS tool to request approval.

**Important:** Do NOT use ${ASK_USER_QUESTION_TOOL_NAME} to ask "Is this plan okay?" or "Should I proceed?" - that is exactly what THIS tool does. ExitPlanMode inherently requests user approval of your plan.

## Examples.

1. Initial task: "Search for and understand the implementation of vim mode in the codebase" - Do not use the exit plan mode tool because you are not planning the implementation steps of a task.
2. Initial task: "Help me implement yank mode for vim" - Use the exit plan mode tool after you finish planning the implementation steps of the task.
3. Initial task: "Add a new feature to handle user authentication" - If unsure about auth method (OAuth, JWT, and more), use ${ASK_USER_QUESTION_TOOL_NAME} first. Then use exit plan mode tool after clarifying the approach.
