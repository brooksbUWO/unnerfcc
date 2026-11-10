<!--
name: 'Tool Result: Remote output truncated'
description: >-
  Informs the model that the command output was truncated and the rest exists
  only on the attached machine, so it must re-run there.
ccVersion: 2.1.321
variables:
  - TRUNCATION_DETAIL
  - MACHINE_NAME
-->
, ${TRUNCATION_DETAIL}; the rest exists only on ${MACHINE_NAME} — re-run there with 
