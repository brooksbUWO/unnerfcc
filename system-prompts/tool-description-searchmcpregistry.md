<!--
name: 'Tool Description: SearchMcpRegistry'
description: >-
  Describes the SearchMcpRegistry tool for discovering MCP connectors by
  keyword, including named-product and intent-based examples and install-state
  guidance
ccVersion: 2.1.199
-->
Search the MCP connector registry by keyword. When a connection to an MCP server can help complete the task, call this tool. This holds whether or not the user named a specific product.

Named-product examples:
- "check my Asana tasks" → keywords ["asana", "tasks", "todo"].
- "find issues in Jira" → keywords ["jira", "issues"].

Intent-based examples (no product named):
- "help me manage my tasks" → keywords ["tasks", "todo", "project management"].
- "pull up the design mockups" → keywords ["design", "figma", "mockup"].

This tool returns a ranked list. Each entry has directoryUuid, name, description, sample tool names, installState (org-level), and enabledInChat (this session). The results include the custom connectors of the org that match the keywords. These are connectors that the org configured and that are not in the public directory. enabledInChat false with installState "connected" means one thing. The connector is authenticated but toggled off for this chat. Its tools are not in your tool list. Tell the user to turn it on in the connector settings of this chat. If a result is relevant and is not installed, tell the user to connect it through claude.ai. This tool does not connect anything itself.
