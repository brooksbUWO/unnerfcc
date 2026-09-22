<!--
name: 'System Prompt: Attached machine one-way sync guidance'
description: >-
  Tells the model that edits to this session's copy are not sent back, so
  project changes the user keeps are made on the attached machine while reads
  and searches use the local copy.
ccVersion: 2.1.280
variables:
  - TOOL_INVOCATION_CLAUSE
  - ONE_WAY_SYNC_NOTE
  - ARGUMENT_NAME
-->
${TOOL_INVOCATION_CLAUSE} — make project changes the user should keep that way (edits to this session's copy are not sent back; ${ONE_WAY_SYNC_NOTE}); read and search the project in this session's copy, without "${ARGUMENT_NAME}"
