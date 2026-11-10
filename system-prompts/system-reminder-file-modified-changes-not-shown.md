<!--
name: 'System Reminder: File modified, changes not shown'
description: >-
  Variant of the external-file-change notice that withholds the diff and points
  the model at the named tool to read the file's current content.
ccVersion: 2.1.321
variables:
  - FILE_CHANGE_NOTICE
  - READ_TOOL_NAME
-->
${FILE_CHANGE_NOTICE} The changes are not shown here; use ${READ_TOOL_NAME} if you need the current content.
