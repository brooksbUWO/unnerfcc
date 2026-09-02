<!--
name: 'Tool Description: Bash sandbox default intro'
description: >-
  Tells the model that bash tool commands run sandboxed by default and that the
  sandbox governs which directories and network hosts a command may reach or
  modify without an explicit override.
ccVersion: 2.1.257
variables:
  - BASH_TOOL_NAME
-->
By default, ${BASH_TOOL_NAME} tool commands run in a sandbox. This sandbox controls which directories and network hosts commands may access or modify without an explicit override.
