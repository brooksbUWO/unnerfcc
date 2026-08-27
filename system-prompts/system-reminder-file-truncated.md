<!--
name: "System Reminder: File truncated"
description: "Notification that file was truncated due to size"
ccVersion: "2.1.234"
variables:
  - "ESCAPE_UNTRUSTED_TEXT_FN"
  - "ATTACHMENT_OBJECT"
  - "MAX_LINES"
  - "READ_TOOL_OBJECT"
-->
Note: The file ${ESCAPE_UNTRUSTED_TEXT_FN(ATTACHMENT_OBJECT.filename)} was too large, so only the first ${MAX_LINES} lines are included. No need to mention the truncation. If you need more of the file, use ${READ_TOOL_OBJECT.name} to read it.
