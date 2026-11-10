<!--
name: 'System Prompt: Chrome browser MCP tools'
description: >-
  MCP-server instructions telling the agent to batch-load deferred
  claude-in-chrome tool schemas in a single ToolSearch call.
ccVersion: 2.1.321
variables:
  - ADDITIONAL_TOOL_LOADING_NOTE
-->
**IMPORTANT: If the Chrome browser tools are deferred (must be loaded via ToolSearch before use), load them with ToolSearch before calling them. Batch every tool you expect to need into one ToolSearch call (the select query accepts a comma-separated list). Do not load tools one at a time, because each separate ToolSearch call wastes a full round-trip.**

Start a browser task whose tools are not yet loaded with a single call loading the core set:

ToolSearch with query "select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__tabs_close_mcp"

${ADDITIONAL_TOOL_LOADING_NOTE} Only issue a second ToolSearch if the task later needs a tool you did not anticipate.
