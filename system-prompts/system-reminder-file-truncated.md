<!--
name: 'System Reminder: File truncated'
description: >-
  Tells the model the file was truncated to its first N lines, not to mention
  the truncation, and which tool to use to read more.
ccVersion: 2.1.257
variables:
  - TRUNCATED_LINE_COUNT
  - FILE_READ_TOOL_NAME
-->
 was too large and has been truncated to the first ${TRUNCATED_LINE_COUNT} lines. If the truncation can affect your answer, tell the user. Use ${FILE_READ_TOOL_NAME} to read more of the file if you need.
