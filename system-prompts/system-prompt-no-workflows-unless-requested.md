<!--
name: 'System Prompt: No workflows or deep research unless requested'
description: >-
  Tells the model not to use the agent tool, workflows, or deep research unless
  the user, a CLAUDE.md file, or a skill asks for it.
ccVersion: 2.1.257
variables:
  - AGENT_TOOL_NAME
-->
Do not use the ${AGENT_TOOL_NAME} tool, workflows, or deep-research unless the user, a CLAUDE.md file, or a skill asks for it
