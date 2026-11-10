<!--
name: 'Tool Description: SuggestConnectors'
description: >-
  Describes the SuggestConnectors tool for resolving SearchMcpRegistry
  directoryUuid values or installed server_id values into full connector
  payloads, with install-state and session-availability guidance.
ccVersion: 2.1.321
-->
Get the full connector payloads for a set of directoryUuid values from SearchMcpRegistry. Call this tool only with directoryUuid values from a SearchMcpRegistry result, or installed connectors' server_id values listed in your system prompt. Do not guess UUIDs. Do not pass connector names.

Returns name, description, url, iconUrl, sample tool names, and whether the connector is already installed for the user's claude.ai org. installState reflects org-level auth, not whether tools are loaded this session — check ListConnectors' enabledInChat before claiming a connector is usable here. If a result looks relevant and is not installed, tell the user they could connect it via claude.ai; this tool does not itself connect anything.
