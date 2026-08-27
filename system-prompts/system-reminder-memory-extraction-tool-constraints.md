<!--
name: "System Reminder: Memory extraction tool constraints"
description: "Lists the tools available to the memory extraction subagent for reading, updating, and deleting memory files under directory restrictions"
ccVersion: "2.1.235"

variables:
  - "READ_TOOL_NAME"
  - "GLOB_TOOL_NAME"
  - "GREP_TOOL_NAME"
  - "SHELL_TOOL_NAME"
  - "ALLOWED_SHELL_COMMANDS"
  - "WRITE_TOOL_NAME"
  - "EDIT_TOOL_NAME"
  - "DELETE_TOOL_NAME"
-->
Available tools: ${READ_TOOL_NAME}, ${GLOB_TOOL_NAME}, ${GREP_TOOL_NAME}, read-only ${SHELL_TOOL_NAME} (${ALLOWED_SHELL_COMMANDS}), and ${WRITE_TOOL_NAME}/${EDIT_TOOL_NAME} for paths inside the memory directory only, and ${SHELL_TOOL_NAME} ${DELETE_TOOL_NAME} of .md files inside the memory directory only (outside protected subdirectories like .git or agents). All other tools — MCP, Agent, write-capable shell, and more — will be denied.