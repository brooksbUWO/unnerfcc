<!--
name: "System Reminder: Compact file reference"
description: "Reference to file read before conversation summarization"
ccVersion: "2.1.234"
variables:
  - "ESCAPE_UNTRUSTED_TEXT_FN"
  - "ATTACHMENT_OBJECT"
  - "READ_TOOL_OBJECT"
-->
Note: ${ESCAPE_UNTRUSTED_TEXT_FN(ATTACHMENT_OBJECT.filename)} was read before the last conversation was summarized, but the contents are too large to include. If you need to access it, use the ${READ_TOOL_OBJECT.name} tool.
