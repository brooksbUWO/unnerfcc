<!--
name: 'Tool Result: Human approval required on machine'
description: >-
  Tool result explaining that the session's automatic check is not enough
  because only a person's approval counts for this tool on the named machine, so
  nothing ran.
ccVersion: 2.1.321
variables:
  - TOOL_NAME
  - MACHINE_NAME
-->
This session's automatic check approved this ${TOOL_NAME} call, but only a person's approval counts for ${TOOL_NAME} on ${MACHINE_NAME}, so nothing ran. Retry once if it is still needed. If it is refused again, stop and tell the user that ${TOOL_NAME} on ${MACHINE_NAME} needs their own approval.
