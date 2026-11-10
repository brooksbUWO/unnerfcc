<!--
name: 'Tool Result: Tool disabled in current session'
description: >-
  Informs the model that a listed tool is currently switched off in this session
  and to proceed without it.
ccVersion: 2.1.321
variables:
  - TOOL_NAME
  - STILL_LISTED_CLAUSE
  - ADDITIONAL_TOOL_STATE_NOTE
-->
. ${TOOL_NAME} ${STILL_LISTED_CLAUSE} but is switched off in this session right now, so it cannot run. Continue without it.${ADDITIONAL_TOOL_STATE_NOTE}
