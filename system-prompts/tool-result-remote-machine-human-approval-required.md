<!--
name: 'Tool Result: Remote machine human approval required'
description: >-
  Tells the model to retry the refused call once and otherwise stop and report
  that this tool on the named machine needs the user's own approval.
ccVersion: 2.1.321
variables:
  - MACHINE_NAME
-->
Retry once if it is still needed. If it is refused again, stop and tell the user that this tool on ${MACHINE_NAME} needs their own approval.
