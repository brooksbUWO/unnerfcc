<!--
name: 'Tool Description: ListMcpResourcesTool prompt'
description: >-
  Tool prompt for listing MCP resources and explaining the optional server
  parameter
ccVersion: 2.1.178
-->

List available resources from configured MCP servers.
Each returned resource includes all standard MCP resource fields. Each resource also includes a 'server' field. This field names the source server of the resource.

Parameters:
- server (optional): The name of a specific MCP server to get resources from. If you do not provide it, the tool returns resources from all servers.
