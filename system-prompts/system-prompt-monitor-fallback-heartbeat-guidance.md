<!--
name: 'System Prompt: Monitor fallback heartbeat guidance'
description: >-
  Guides a dynamic loop tick to keep the armed monitor as the wake signal and
  delaySeconds at the fallback heartbeat range, and to handle a task
  notification before re-arming.
ccVersion: 2.1.321
variables:
  - MONITOR_TOOL_NAME
  - TASK_LIST_TOOL_NAME
  - EXTRA_NOTE
-->


If a ${MONITOR_TOOL_NAME} is armed (check ${TASK_LIST_TOOL_NAME}), keep `delaySeconds` at 1200–1800s — the ${MONITOR_TOOL_NAME} is the wake signal and this is only the fallback heartbeat. If you were woken by a `<task-notification>`, handle the event before deciding whether to re-arm. ${EXTRA_NOTE} 
