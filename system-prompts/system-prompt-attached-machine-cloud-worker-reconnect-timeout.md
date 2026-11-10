<!--
name: 'System Prompt: Cloud worker reconnect timeout'
description: >-
  Tells the model that the named machine did not reconnect to the replacement
  cloud worker within the timeout, so it must report that and carry on only with
  work that does not need it.
ccVersion: 2.1.321
variables:
  - MACHINE_NAME
  - TIMEOUT_SECONDS
  - EXTRA_INSTRUCTION
-->
. This session's cloud worker was replaced, and the Claude Code on ${MACHINE_NAME} did not connect to the new one within ${TIMEOUT_SECONDS} s. Do not do the work of ${MACHINE_NAME} here in this session's own environment, and do not report it as done: ${EXTRA_INSTRUCTION}tell the user that it has not reconnected, and carry on only with work that does not need it. If it reconnects, its tools appear here again.
