<!--
name: 'System Reminder: Working directory changed'
description: >-
  Tells the model the session's working directory has changed, that tool calls
  and relative paths now resolve from it, and which project settings, MCP
  servers and skills now apply.
ccVersion: 2.1.321
variables:
  - NEW_DIRECTORY
  - CHANGE_REASON
  - EXTRA_NOTE
-->
The session's working directory has changed to ${NEW_DIRECTORY} (${CHANGE_REASON}). ${EXTRA_NOTE}All tool calls and relative paths now resolve from ${NEW_DIRECTORY}. Project settings (permission rules, hooks), project MCP servers, and project skills now come from ${NEW_DIRECTORY}; its CLAUDE.md, if any, follows below. Environment variables set by the previous directory's settings stay in effect for this process — they cannot be unset — and the new directory's settings env is applied on top of them.
