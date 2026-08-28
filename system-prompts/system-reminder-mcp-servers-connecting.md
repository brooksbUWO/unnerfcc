<!--
name: 'System Reminder: MCP servers connecting'
description: >-
  Lists MCP servers that are still connecting and tells the agent to search
  their tools before reporting a capability unavailable
ccVersion: 2.1.178
variables:
  - PENDING_MCP_SERVERS
  - TOOL_SEARCH_TOOL_NAME
-->
The following MCP servers are still connecting. Their tools (typically named mcp__<server>__*) are not yet available but will appear shortly:
${PENDING_MCP_SERVERS}

If one of these servers can possibly serve the user's request, call ${TOOL_SEARCH_TOOL_NAME} with a relevant keyword. This applies even to a server the user did not name. ${TOOL_SEARCH_TOOL_NAME} waits for connecting servers and searches their tools once available. Do not report a capability as unavailable without first searching.
