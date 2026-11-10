<!--
name: 'Tool Result: Desktop browser tools connection status guidance'
description: >-
  Explains that the Claude desktop app's built-in browser needs no enabling, how
  to recognize its tools, and what to tell the user when no browser tool is
  present.
ccVersion: 2.1.321
variables:
  - TOOL_USE_GUIDANCE
  - FALLBACK_GUIDANCE
-->
The Claude desktop app's built-in browser needs no enabling: its tools are the ones whose names contain Claude_Browser. ${TOOL_USE_GUIDANCE}. ${FALLBACK_GUIDANCE} If you have no browser tool of any kind, tell the user that the browser in their Claude desktop app is not available in this chat right now and continue with what you can do here.
