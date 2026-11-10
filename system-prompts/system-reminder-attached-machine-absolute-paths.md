<!--
name: 'System Reminder: Attached machine absolute paths'
description: >-
  Instructs passing absolute paths on the attached machine and warns that the
  same relative path names two different files, one in each copy.
ccVersion: 2.1.321
variables:
  - TOOL_LIST
  - RUN_INSTRUCTION
  - PATH_EXAMPLE_NOTE
  - MACHINE_ARGUMENT
-->
 ${TOOL_LIST} ${RUN_INSTRUCTION} on the user's copy there, under that machine's own permission rules — give paths (file_path, or a search's path) as absolute paths on that machine${PATH_EXAMPLE_NOTE}; without "${MACHINE_ARGUMENT}" they act on this session's checkout. The same relative path names two different files, one in each copy, and they may differ: an edit to one does not change the other
