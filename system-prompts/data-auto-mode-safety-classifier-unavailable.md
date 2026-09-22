<!--
name: 'Data: Auto mode safety classifier unavailable'
description: >-
  tool_result text telling the model the auto-mode safety classifier is
  unavailable and to wait a moment and try the action again.
ccVersion: 2.1.280
variables:
  - CANNOT_DETERMINE_SAFETY_CLAUSE
  - BLOCKED_ACTION_DESCRIPTION
  - RETRY_FALLBACK_GUIDANCE
-->
${CANNOT_DETERMINE_SAFETY_CLAUSE}${BLOCKED_ACTION_DESCRIPTION} right now. Wait a moment and then try this action again. ${RETRY_FALLBACK_GUIDANCE} 
