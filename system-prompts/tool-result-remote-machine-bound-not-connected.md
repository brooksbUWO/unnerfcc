<!--
name: 'Tool Result: Remote machine bound not connected'
description: >-
  Reports that the user's linked computer has not connected, so the call did not
  run, and asks the user to check that Claude is running there.
ccVersion: 2.1.321
variables:
  - REASON
-->
The user's computer is linked to this session, but Claude on it has not connected — ${REASON}; the call did not run. Ask the user to check that Claude is running on that computer.
