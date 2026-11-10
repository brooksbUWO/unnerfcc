<!--
name: 'Tool Description: SearchMcpRegistry'
description: >-
  Describes searching the MCP connector registry by keyword, with named-product
  and intent-based examples, and how to read installState and enabledInChat in
  the results.
ccVersion: 2.1.321
-->
Search the MCP connector registry by keyword. When a connection to an MCP server can help complete the task, call this tool. This holds whether or not the user named a specific product.

Named-product examples:
- "check my Asana tasks" → keywords ["asana", "tasks", "todo"]
- "find issues in Jira" → keywords ["jira", "issues"]

Intent-based examples (no product named):
- "help me manage my tasks" → keywords ["tasks", "todo", "project management"]
- "pull up the design mockups" → keywords ["design", "figma", "mockup"]

Returns a ranked list with directoryUuid, name, description, sample tool names, installState (org-level), and enabledInChat (this session). Results include the org's custom connectors (ones the org configured that are not in the public directory) when they match the keywords. enabledInChat: false with installState: "connected" means the connector's tools are not loaded in this session, so you cannot call them; the field does not say why. There may be no connector setting for this chat alone. If the request needs the connector, tell the user it is not available here and that they can check it, and its tool permissions, in their claude.ai connector settings. If a result looks relevant and is not installed, tell the user they could connect it via claude.ai; this tool does not itself connect anything.
