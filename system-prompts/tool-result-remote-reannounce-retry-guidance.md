<!--
name: 'Tool Result: Remote re-announce retry guidance'
description: >-
  Guidance not to retry the command until the machine re-announces, to continue
  with what does not need it, and to tell the user what could not be confirmed.
ccVersion: 2.1.321
variables:
  - MACHINE_NAME
-->
 Do not retry it on ${MACHINE_NAME} until ${MACHINE_NAME} re-announces, and do not call it again in this turn; continue with what you can do without it, and tell the user you could not confirm whether it 
