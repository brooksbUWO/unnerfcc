<!--
name: 'Tool Description: ReadMcpResourceDirTool prompt'
description: >-
  Tool prompt for listing direct children of an MCP directory resource and
  explaining the required server and uri parameters
ccVersion: 2.1.219
variables:
  - DIRECTORY_MIME_TYPE
-->

List the direct children of a directory resource on an MCP server (`resources/directory/read`).

Parameters:
- server (required): The name of the MCP server to read from
- uri (required): The URI of the directory resource

The listing is not recursive. Each entry carries its own `uri`. Subdirectories appear with mimeType "${DIRECTORY_MIME_TYPE}". To descend, call this tool again on the `uri` of a subdirectory.

Use this tool only against a server that declares support for directory listing. Other servers return an error.
