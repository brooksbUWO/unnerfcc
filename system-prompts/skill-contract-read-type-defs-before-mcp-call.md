<!--
name: 'Skill: Read contract type defs before MCP calls'
description: >-
  Closes the artifact call-contract note — the read directive it interpolates
  names the extracted files that are authoritative for this contract version
  over any remembered API shape.
ccVersion: 2.1.280
variables:
  - READ_CONTRACT_FILES_DIRECTIVE
  - ADDITIONAL_CONTRACT_NOTES
  - TRAILING_CONTRACT_NOTE
-->
. ${READ_CONTRACT_FILES_DIRECTIVE} authoritative for this contract version over any remembered API shape. ${ADDITIONAL_CONTRACT_NOTES} ${TRAILING_CONTRACT_NOTE}
