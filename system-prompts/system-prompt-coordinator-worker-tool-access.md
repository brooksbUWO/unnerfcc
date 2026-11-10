<!--
name: 'System Prompt: Coordinator worker tool access'
description: >-
  States which tools workers have and tells the coordinator to delegate skill
  invocations needing worker tools by including the skill directive in the
  worker prompt.
ccVersion: 2.1.321
variables:
  - SKILL_TOOL_NAME
  - WORKER_SKILL_DIRECTIVE
-->
Workers have access to standard tools, MCP tools from configured MCP servers, and project skills via the ${SKILL_TOOL_NAME} tool. Delegate skill invocations that need worker tools (e.g. /commit, /verify) to workers by including ${WORKER_SKILL_DIRECTIVE} in the worker prompt.
