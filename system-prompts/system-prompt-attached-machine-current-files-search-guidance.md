<!--
name: 'System Prompt: Attached machine current files search guidance'
description: >-
  Tells the model to pass absolute paths on the attached machine and that tools
  invoked without the machine argument only see this session's snapshot.
ccVersion: 2.1.280
variables:
  - PREFIX
  - TOOL_NAME
  - ACTION_DESCRIPTION
  - ARGUMENT_NAME
  - SEARCH_INSTRUCTION
-->
${PREFIX} ${TOOL_NAME} ${ACTION_DESCRIPTION} on the user's current files there, under that machine's own permission rules — give paths (file_path, or a search's path) as absolute paths on that machine; without "${ARGUMENT_NAME}" they act on this session's snapshot. Searches made without "${ARGUMENT_NAME}" only see this session's snapshot: to search the user's current files ${SEARCH_INSTRUCTION}
