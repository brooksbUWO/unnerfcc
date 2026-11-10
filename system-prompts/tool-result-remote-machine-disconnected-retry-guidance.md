<!--
name: 'Tool Result: Remote machine disconnected retry guidance'
description: >-
  Guidance against retrying non-idempotent commands or calling the machine again
  until it reconnects.
ccVersion: 2.1.321
variables:
  - FAILURE_PREFIX
  - MACHINE_NAME
-->
${FAILURE_PREFIX} Do not retry non-idempotent commands on ${MACHINE_NAME} until ${MACHINE_NAME} reconnects, and do not call it again 
