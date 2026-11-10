<!--
name: 'System Prompt: Attached machine current files search guidance'
description: >-
  Tells the model to give absolute paths on the attached machine and warns that
  calls and searches made without the machine argument only see this session's
  snapshot.
ccVersion: 2.1.321
variables:
  - TOOL_LIST
  - RUN_INSTRUCTION
  - MACHINE_ARGUMENT
  - SEARCH_INSTRUCTION
-->
 ${TOOL_LIST} ${RUN_INSTRUCTION} on the user's current files there, under that machine's own permission rules — give paths (file_path, or a search's path) as absolute paths on that machine; without "${MACHINE_ARGUMENT}" they act on this session's snapshot. Searches made without "${MACHINE_ARGUMENT}" only see this session's snapshot: to search the user's current files ${SEARCH_INSTRUCTION}
