<!--
name: 'System Reminder: Tool disconnected continue without it'
description: >-
  Informs the model that a listed tool has no provider in this session right now
  and to continue without it.
ccVersion: 2.1.321
variables:
  - TOOL_NAME
  - STILL_LISTED_CLAUSE
  - ADDITIONAL_TOOL_STATE_NOTE
-->
. ${TOOL_NAME} ${STILL_LISTED_CLAUSE}, but nothing in this session provides it right now (its source was removed or disconnected, or this version no longer has it), so it cannot run. Continue without it.${ADDITIONAL_TOOL_STATE_NOTE}
