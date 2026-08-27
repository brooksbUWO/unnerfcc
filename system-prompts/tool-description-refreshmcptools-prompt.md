<!--
name: "Tool Description: RefreshMcpTools prompt"
description: "Tool prompt for refreshing one or all connected MCP servers tool lists and interpreting per-server results"
ccVersion: "2.1.211"
-->
Re-query the tool lists of connected MCP servers and update the available tools.

This tool returns one entry per server. Each entry has the server name, the refresh status, and the current tool count. Each entry also lists the tool names added or removed since the last tool list. A server that is not connected now is reported as not_connected. This tool never dials or re-dials connections. It only re-reads the tool list over the current connection.

Parameters:
- server (optional): The name of a specific MCP server to refresh. If not provided, all connected servers are refreshed.
