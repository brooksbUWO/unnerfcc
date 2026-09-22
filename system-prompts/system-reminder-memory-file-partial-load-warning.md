<!--
name: 'System Reminder: Memory file partially loaded'
description: >-
  Warns that a memory file was only partially loaded because of its size and
  that each memory file should stay focused on one topic.
ccVersion: 2.1.280
variables:
  - MEMORY_FILE_SIZE
  - LOADED_PORTION_DESCRIPTION
-->
this memory file is ${MEMORY_FILE_SIZE}. Only part of it was loaded: ${LOADED_PORTION_DESCRIPTION}. Keep each memory file focused on one topic.
