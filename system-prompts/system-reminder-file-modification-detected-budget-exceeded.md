<!--
name: 'System Reminder: File modification detected (budget exceeded)'
description: >-
  Tells the model the changed file's diff was omitted because other changed
  files this turn filled the snippet budget, and to read the file if it needs
  the current content.
ccVersion: 2.1.257
variables:
  - FILE_MODIFICATION_NOTICE
  - FILE_READ_TOOL_NAME
-->
${FILE_MODIFICATION_NOTICE} The diff is omitted here because other changed files this turn already filled the snippet budget; use ${FILE_READ_TOOL_NAME} if you need the current content.
