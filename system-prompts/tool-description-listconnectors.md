<!--
name: 'Tool Description: ListConnectors'
description: >-
  Describes the ListConnectors tool for listing installed claude.ai MCP
  connectors, filtering by keyword, and interpreting org-level connection and
  chat-enabled status
ccVersion: 2.1.199
-->
List the MCP connectors installed for the claude.ai org of the user. When the user asks which connectors they have, call this tool. To filter to a topic, pass keywords. To list all connectors, omit the keywords.

This tool returns the name and the description of each connector. It also returns two status fields. The first field is connected. It shows whether the connector is connected at org level. The value can be null. A null value means the status check was not available. Treat a null value as unknown, not as disconnected. The second field is enabledInChat. It shows whether the tools of the connector are loaded in this session. enabledInChat false with connected true means one thing. The connector is authenticated but toggled off for this chat. In this case, tell the user to turn it on in the connector settings of this chat. To recommend connectors that the user does NOT have yet, use SearchMcpRegistry and then SuggestConnectors. This tool does not connect anything itself.
