<!--
name: "Tool Description: Agent when to launch subagents"
description: "Explains subagent_type selection including fork vs fresh agents"
ccVersion: "2.1.235"
variables:
  - "AGENT_TOOL_NAME"
-->
When using the ${AGENT_TOOL_NAME} tool, specify a subagent_type to select an agent: `"fork"` forks yourself (the fork inherits your full conversation context and always runs on your model — a `model` override is ignored); 