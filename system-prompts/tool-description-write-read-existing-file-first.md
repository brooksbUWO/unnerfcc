<!--
name: "Tool Description: Write (read existing file first)"
description: "Tool description for Write in environments where existing files must be read before overwrite"
ccVersion: "2.1.223"
variables:
  - "READ_TOOL_NAME"
  - "OVERWRITE_READ_REQUIREMENT_NOTE"
  - "EDIT_TOOL_NAME"
-->
Writes a file to the local filesystem. If a file exists, this tool overwrites it.

Use this tool to create a new file. Also use it to fully replace a file that you already read with ${READ_TOOL_NAME}.${OVERWRITE_READ_REQUIREMENT_NOTE} For partial changes, use ${EDIT_TOOL_NAME} instead.
