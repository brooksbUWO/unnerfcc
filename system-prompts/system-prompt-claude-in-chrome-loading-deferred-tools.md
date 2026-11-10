<!--
name: 'System Prompt: Claude in Chrome loading deferred tools'
description: >-
  Instructs the model on batch loading deferred claude-in-chrome tools via a
  single ToolSearch call.
ccVersion: 2.1.321
variables:
  - ADDITIONAL_TOOL_LOADING_NOTE
-->
## Loading deferred tools

If the mcp__claude-in-chrome__* tools are deferred (must be loaded via ToolSearch before use), load every tool you expect to need in ONE ToolSearch call — the select query accepts a comma-separated list — never one call per tool. Start with the core set:

ToolSearch with query "select:mcp__open-claude-in-chrome__tabs_context_mcp,mcp__open-claude-in-chrome__navigate,mcp__open-claude-in-chrome__computer,mcp__open-claude-in-chrome__read_page,mcp__open-claude-in-chrome__tabs_create_mcp,mcp__open-claude-in-chrome__tabs_close_mcp"

${ADDITIONAL_TOOL_LOADING_NOTE}
