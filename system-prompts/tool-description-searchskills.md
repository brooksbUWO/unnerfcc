<!--
name: 'Tool Description: SearchSkills'
description: >-
  Describes the SearchSkills tool for finding relevant claude.ai skills by
  keyword and suggesting add cards when results fit
ccVersion: 2.1.222
-->
Search the claude.ai skills of the user by keyword. A skill is a reference document or instruction set that the user uploaded or enabled. When a skill can help complete the task, call this tool.

Examples:
- "follow the team's PR guidelines" → keywords ["pr", "review", "guidelines"].
- "export this as a slide deck" → keywords ["pptx", "slides", "presentation"].

This tool returns a ranked list with id, name, description, and whether the skill is enabled. If the results fit and SuggestSkills is one of your tools, call it to show the add card. If not, relay the relevant results in text. If nothing is relevant, continue and do not mention the search.
