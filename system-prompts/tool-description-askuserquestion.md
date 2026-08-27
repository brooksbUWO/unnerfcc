<!--
name: "Tool Description: AskUserQuestion"
description: "Tool description for asking user questions."
ccVersion: "2.1.154"
variables:
  - "ENTER_PLAN_MODE_TOOL_NAME"
  - "EXIT_PLAN_MODE_TOOL_NAME"
-->
Use this tool only for a decision that is truly for the user to make. This is a decision that you cannot resolve from the request, the code, or sensible defaults.

Usage notes:
- The user can always select "Other" to give custom text input.
- Use multiSelect: true to let the user select more than one answer for a question.
- To recommend a specific option, make it the first option in the list. Add "(Recommended)" at the end of the label.

Plan mode note: To switch into plan mode, use ${ENTER_PLAN_MODE_TOOL_NAME}, not this tool. In plan mode, use this tool to clarify requirements or to choose between approaches. Do this before you finalize your plan. Do NOT use this tool to ask "Is my plan ready?" or "Do I proceed?". Do NOT reference "the plan" in questions. The user cannot see the plan until you call ${EXIT_PLAN_MODE_TOOL_NAME} for approval.
