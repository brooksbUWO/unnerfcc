<!--
name: 'Tool Description: Claude in Chrome tabs context'
description: >-
  Describes the Claude in Chrome tabs_context_mcp tool for retrieving the
  current MCP tab group context
ccVersion: 2.1.178
-->
Get context about the current Open Claude in Chrome (browser-occ) tab group. The tool returns all tab IDs in the group. The group must exist first. Call this tool at least once before other browser automation tools, so you know what tabs exist. Every later tool call needs the correct tab ID. Each new conversation must create its own new tab. Reuse an existing tab for one reason only: a user request.
