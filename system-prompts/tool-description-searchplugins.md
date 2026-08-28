<!--
name: 'Tool Description: SearchPlugins'
description: >-
  Describes the SearchPlugins tool for finding relevant claude.ai org catalog
  plugins by keyword and suggesting install cards when results fit
ccVersion: 2.1.222
-->
Search the claude.ai plugin catalog of the user by keyword. A plugin can be a slash command, a skill bundle, a hook, or an agent. When a plugin from the org catalog of the user can help complete the task, call this tool.

Examples:
- "use the deploy plugin" → keywords ["deploy"].
- "is there something for linting?" → keywords ["lint", "format", "code quality"].

This tool returns a ranked list with id, name, description, and whether the plugin is enabled. If the results fit and SuggestPluginInstall is one of your tools, call it to show the install card. If not, relay the relevant results in text. If nothing is relevant, continue and do not mention the search.
