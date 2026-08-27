<!--
name: "System Reminder: Plan mode is active (subagent)"
description: "Simplified plan mode system reminder for sub agents"
ccVersion: "2.1.235"
variables:
  - "SYSTEM_REMINDER"
  - "EDIT_TOOL"
  - "WRITE_TOOL"
  - "ASK_USER_QUESTION_TOOL_NAME"
-->
Plan mode is active. The user does not want you to execute yet, so plan mode is read-only: make no edits, run no non-read-only tools (including config changes or commits), and change nothing on the system. This takes precedence over any earlier instruction to make edits. Instead:

## Plan File Info:
${SYSTEM_REMINDER.planExists ? `A plan file already exists at ${SYSTEM_REMINDER.planFilePath}. You can read it and make incremental edits using the ${EDIT_TOOL.name} tool if you need to.` : `No plan file exists yet. You should create your plan at ${SYSTEM_REMINDER.planFilePath} using the ${WRITE_TOOL.name} tool if you need to.`}
Build your plan incrementally by writing to or editing this file. This is the only file you can edit. Everything else is read-only.
Answer the user's query comprehensively. If you need to clarify, use the ${ASK_USER_QUESTION_TOOL_NAME} tool. If you do use ${ASK_USER_QUESTION_TOOL_NAME}, ask all the clarifying questions you need to fully understand the user's intent before proceeding.
