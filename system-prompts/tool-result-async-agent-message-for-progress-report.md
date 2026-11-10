<!--
name: 'Tool Result: Message the agent for a progress report'
description: >-
  Trailing hint on a running async agent's result telling the model to send the
  agent a message if it needs a progress report before completion.
ccVersion: 2.1.321
variables:
  - SEND_MESSAGE_TOOL_NAME
-->
 Send it a message with ${SEND_MESSAGE_TOOL_NAME} if you need a progress report before then.
