<!--
name: 'System Reminder: Project thread reply call returned error'
description: >-
  Reminds the model that its project thread reply tool call errored so nothing
  reached the thread, and instructs it to call the reply tool again.
ccVersion: 2.1.321
variables:
  - FAILED_TOOL
-->
Your `${FAILED_TOOL}` call this turn returned an error, so nothing reached the project thread. Call `
