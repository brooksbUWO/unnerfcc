<!--
name: 'System Reminder: Auto-reply paused (hourly cap)'
description: >-
  Tells the model that artifact auto-reply is paused by the hourly cap, so it
  should read the waiting comments and reply with the Artifact tool.
ccVersion: 2.1.321
variables:
  - PENDING_COMMENTS_NOTICE
  - ARTIFACT_TOOL_NAME
-->
${PENDING_COMMENTS_NOTICE} — auto-reply held back (hourly cap); use ${ARTIFACT_TOOL_NAME} to read and reply.
