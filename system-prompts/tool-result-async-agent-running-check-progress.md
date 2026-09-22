<!--
name: 'Tool Result: Async Agent Running (check progress)'
description: >-
  Tool_result note when a spawned async agent is still running: do not spawn a
  duplicate; read its partial output or send it a message.
ccVersion: 2.1.280
variables:
  - PARTIAL_OUTPUT_FILE_PATH
  - SEND_MESSAGE_TOOL_NAME
-->
Do NOT spawn a duplicate. You will be notified when it completes. You can read partial output at ${PARTIAL_OUTPUT_FILE_PATH} or send it a message with ${SEND_MESSAGE_TOOL_NAME}.
