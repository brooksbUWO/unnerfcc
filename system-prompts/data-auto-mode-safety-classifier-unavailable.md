<!--
name: 'Data: Auto mode safety classifier unavailable'
description: >-
  tool_result text telling the model the auto-mode safety classifier is
  unavailable and to wait a moment and try the action again.
ccVersion: 2.1.321
variables:
  - CANNOT_DETERMINE_SAFETY_CLAUSE
  - BLOCKED_ACTION_DESCRIPTION
  - SECOND_BLOCKED_ACTION_DETAIL
  - THIRD_BLOCKED_ACTION_DETAIL
  - RETRY_FALLBACK_GUIDANCE
-->
${CANNOT_DETERMINE_SAFETY_CLAUSE} is temporarily unavailable${BLOCKED_ACTION_DESCRIPTION}${SECOND_BLOCKED_ACTION_DETAIL}${THIRD_BLOCKED_ACTION_DETAIL} right now. Wait a moment and then try this action again. ${RETRY_FALLBACK_GUIDANCE} 
