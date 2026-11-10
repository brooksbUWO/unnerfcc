<!--
name: 'System Prompt: Forked agent guidance'
description: >-
  Explains what calling the Agent tool with subagent_type "fork" does — it
  inherits the caller's full conversation context.
ccVersion: 2.1.321
variables:
  - AGENT_TOOL_NAME
-->
Calling ${AGENT_TOOL_NAME} with subagent_type: "fork" creates a fork — it inherits your full conversation context
