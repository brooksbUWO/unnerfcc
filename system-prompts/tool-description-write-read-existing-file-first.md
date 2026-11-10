<!--
name: 'Tool Description: Write (read an existing file first)'
description: >-
  Write tool guidance — use it for a new file or a full replacement of one
  already read, overwriting an unread file fails, and partial changes belong to
  the edit tool.
ccVersion: 2.1.321
variables:
  - READ_TOOL_NAME
  - EDIT_TOOL_NAME
-->
Writes a file to the local filesystem. If a file exists, this tool overwrites it.

Use this tool to create a new file. Also use it to fully replace a file that you already read with ${READ_TOOL_NAME}. Overwriting an existing file you have not read with ${READ_TOOL_NAME} fails. For partial changes, use ${EDIT_TOOL_NAME} instead.
