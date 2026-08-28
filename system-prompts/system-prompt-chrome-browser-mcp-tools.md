<!--
name: 'System Prompt: Chrome browser MCP tools'
description: >-
  MCP-server instructions telling the agent to batch-load deferred
  claude-in-chrome tool schemas in a single ToolSearch call
ccVersion: 2.1.222
-->
The Open Claude in Chrome (browser-occ) tools can be deferred. A deferred tool must be loaded through ToolSearch before you use it. Load every tool you expect to need in ONE ToolSearch call. The select query accepts a comma-separated list. Do not load tools one at a time. Each separate ToolSearch call wastes a full round trip.

To start a browser task whose tools are not yet loaded, make a single call for the core set:

ToolSearch with query "select:mcp__open-claude-in-chrome__tabs_mcp,mcp__open-claude-in-chrome__navigate,mcp__open-claude-in-chrome__computer,mcp__open-claude-in-chrome__read_page,mcp__open-claude-in-chrome__javascript_tool"

When the task needs them, add task-specific tools to the same call: read_console_messages or read_network_requests for debugging, form_input for forms, gif_creator for recordings, javascript_tool for page scripting. Make a second ToolSearch call for one reason only: the task later needs a tool you did not expect.
