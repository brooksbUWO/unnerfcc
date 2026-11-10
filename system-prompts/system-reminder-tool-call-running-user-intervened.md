<!--
name: 'System Reminder: Tool call still running, user intervened'
description: >-
  Tells the model a still-loading tool call was not interrupted and its result
  arrives later under the same tool_use_id, so it should answer the user's new
  message without repeating, waiting for or claiming to cancel the call.
ccVersion: 2.1.321
variables:
  - TOOL_NAME
  - RESULT_BLOCK_TAG
-->
[Still running. The user sent a message while this call loads, and that message follows so you can answer it now. This ${TOOL_NAME} call was not interrupted. Its result will be delivered to you on its own, in a later <${RESULT_BLOCK_TAG}> carrying this tool_use_id. Do not repeat the call, and do not wait, sleep or poll for it. You cannot stop it either, so never say you cancelled or dropped it.
