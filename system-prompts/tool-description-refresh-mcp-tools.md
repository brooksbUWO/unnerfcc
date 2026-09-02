<!--
name: 'Tool Description: Refresh MCP tools'
description: >-
  Describes the tool that re-queries connected MCP servers for their tool lists
  and when to use it after a device or app connects.
ccVersion: 2.1.257
-->
Re-queries the tool list of connected MCP servers and updates the set of available tools. It reports which tools were added or removed.

An MCP server normally pushes a notification for a change in its tool list. But that notification can get lost. Two causes are connection hiccups and a device that announced while the notification stream was down. When the available tools can be out of date, use this tool to re-sync. Good triggers:
- The user says that a device or app is now open or connected. Examples are "my desktop IS open" and "I just started the app". This follows a failed tool call with device-not-connected, or the expected tools are missing.
- A tool that you expect from an MCP server is absent from your available tools.
- The tools of a server look stale after its connection recovered.
