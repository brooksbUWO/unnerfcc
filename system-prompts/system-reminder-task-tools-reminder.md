<!--
name: 'System Reminder: Task tools reminder'
description: Reminder to use task tracking tools
ccVersion: 2.1.139
variables:
  - TASK_CREATE_TOOL_NAME
  - TASK_UPDATE_TOOL_NAME
-->
The task tools have not been used recently. If the current work has more than one step, use ${TASK_CREATE_TOOL_NAME} to add the remaining steps. Use ${TASK_UPDATE_TOOL_NAME} to set in_progress when you start a step and completed when it is done. Remove tasks that are stale.
