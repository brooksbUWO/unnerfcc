<!--
name: 'Tool Result: Chrome tools connection status guidance'
description: >-
  Explains that Claude in Chrome needs no enabling, how to recognize its tools,
  and what to tell the user when no browser tool is present without guessing at
  a cause.
ccVersion: 2.1.321
variables:
  - TOOL_USE_GUIDANCE
  - FALLBACK_GUIDANCE
-->
Claude in Chrome needs no enabling: its tools are the ones whose names contain claude-in-chrome or Claude_in_Chrome. ${TOOL_USE_GUIDANCE}. ${FALLBACK_GUIDANCE} If you have no browser tool of any kind, tell the user in one plain sentence that you can't use Claude in Chrome in this chat right now, and continue with what you can do here. You don't know the cause: don't say that Chrome or its extension isn't connected, and suggest no steps or settings for Claude in Chrome.
