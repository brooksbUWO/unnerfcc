<!--
name: 'Tool Description: WebFetch private URL warning'
description: >-
  Warns that WebFetch fails on authenticated or private URLs and directs
  checking for a specialized MCP tool with authenticated access first.
ccVersion: 2.1.321
variables:
  - TOOL_HEADER
-->
${TOOL_HEADER}IMPORTANT: WebFetch WILL FAIL for authenticated or private URLs. Before you use this tool, examine the URL. Some URLs point to an authenticated service (for example Google Docs, Confluence, Jira, GitHub). For such a URL, look for a specialized MCP tool that gives authenticated access.
