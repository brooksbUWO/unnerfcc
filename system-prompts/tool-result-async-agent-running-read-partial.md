<!--
name: 'Tool Result: Async Agent Running (read partial output)'
description: >-
  Tool_result note when a spawned async agent is still running and has no
  readable output file: do not spawn a duplicate; message it for a progress
  report instead.
ccVersion: 2.1.280
variables:
  - SEND_MESSAGE_TOOL_NAME
-->
Do NOT spawn a duplicate. You will be notified when it completes. Send it a message with ${SEND_MESSAGE_TOOL_NAME} if you need a progress report before then.
