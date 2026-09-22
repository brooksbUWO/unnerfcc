<!--
name: 'Tool Result: Remote machine omit param fallback lead-in'
description: >-
  Lead-in saying the named machine does not serve this tool right now and to
  omit the machine parameter to run it elsewhere.
ccVersion: 2.1.280
variables:
  - MACHINE_NAME
  - TOOL_NAME
  - PARAM_NAME
-->
${MACHINE_NAME} does not serve ${TOOL_NAME} right now (its Claude Code may be an older version); omit "${PARAM_NAME}" to run it 
