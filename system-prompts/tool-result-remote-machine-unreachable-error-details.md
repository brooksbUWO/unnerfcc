<!--
name: 'Tool Result: Remote machine unreachable error details'
description: >-
  Reports that the named computer could not be reached from this session, with
  the error details, and that the call did not run.
ccVersion: 2.1.321
variables:
  - MACHINE_NAME
  - ERROR_DETAILS
  - ERROR_DETAIL_SUFFIX
-->
${MACHINE_NAME} could not be reached from this session (${ERROR_DETAILS}${ERROR_DETAIL_SUFFIX}); the call did not run.
