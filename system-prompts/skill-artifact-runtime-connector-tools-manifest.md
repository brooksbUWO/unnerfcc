<!--
name: 'Skill: Artifact runtime connector tool names'
description: >-
  Tells the artifact runtime skill that a connector manifest's `tools` array
  takes upstream tool names and that every servers[] entry needs a non-empty
  tools list, which never means "all tools".
ccVersion: 2.1.257
variables:
  - CONNECTOR_SCOPE_NOTE
  - MANIFEST_SHAPE_NOTE
  - SERVER_ENTRY_NOTE
  - TOOL_NAME_SEGMENT_NOTE
  - LIST_TOOLS_SOURCE
  - HERMETIC_SESSION_NOTE
-->
${CONNECTOR_SCOPE_NOTE}${MANIFEST_SHAPE_NOTE}${SERVER_ENTRY_NOTE}${TOOL_NAME_SEGMENT_NOTE} The manifest's `tools` array takes the connector's upstream tool names (as returned by ${LIST_TOOLS_SOURCE}), which can differ from the normalized `<toolName>` segment when an upstream name contains `.` or spaces. Every `servers[]` entry needs a non-empty `tools` array naming the tools the page calls — an empty or omitted `tools` list is refused and never means "all tools"; to publish without connector access, leave `mcp` out of `capabilities` (pass `capabilities: {}` to clear a stored declaration) rather than declaring an empty `servers` list.${HERMETIC_SESSION_NOTE}
