<!--
name: 'Tool Description: SuggestConnectors'
description: >-
  Describes the SuggestConnectors tool for resolving SearchMcpRegistry
  directoryUuid values into full connector payloads and install-state guidance
ccVersion: 2.1.199
-->
Get the full connector payloads for a set of directoryUuid values from SearchMcpRegistry. Call this tool only with directoryUuid values from a SearchMcpRegistry result. Do not guess UUIDs. Do not pass connector names.

This tool returns the name, the description, the url, the iconUrl, and sample tool names of each connector. It also returns whether the connector is installed for the claude.ai org of the user. The installState field shows org-level auth only. It does not show whether the tools are loaded this session. To know whether a connector is usable here, examine the enabledInChat field from ListConnectors first. If a result is relevant and is not installed, tell the user to connect it through claude.ai. This tool does not connect anything itself.
