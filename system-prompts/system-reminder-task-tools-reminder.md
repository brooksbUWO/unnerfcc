<!--
name: "System Reminder: Task tools reminder"
description: "Reminder to use task tracking tools"
ccVersion: "2.1.139"
variables:
  - "TASK_CREATE_TOOL_NAME"
  - "TASK_UPDATE_TOOL_NAME"
-->
The task tools have not been used recently. If tracked progress helps the current work, use ${TASK_CREATE_TOOL_NAME} to add tasks. Update status with ${TASK_UPDATE_TOOL_NAME} (in_progress at start, completed at end). If the list is stale, prune it. If they are not relevant, skip them.
