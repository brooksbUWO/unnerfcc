<!--
name: 'Agent Prompt: Chrome Browser whenToUse'
description: >-
  whenToUse text for the Chrome browser-automation agent: invoke before using
  any mcp__claude-in-chrome__* tools for browser-based actions.
ccVersion: 2.1.178
-->
When the user wants to interact with web pages, automate browser tasks, capture screenshots, read console logs, or do any browser-based action. If the browser-occ skill is listed in this session, invoke Skill(browser-occ) instead of this skill. Invoke this skill only when browser-occ is not listed, before you use any mcp__open-claude-in-chrome__* tool.
