<!--
name: 'System Reminder: Memory Index Partial Load Warning'
description: >-
  Warns that the memory index was only partially loaded because of its size and
  that index entries belong on one short line with detail moved into topic
  files.
ccVersion: 2.1.280
variables:
  - MEMORY_INDEX_PATH
  - MEMORY_INDEX_SIZE
  - LOADED_PORTION_DESCRIPTION
-->
${MEMORY_INDEX_PATH} is ${MEMORY_INDEX_SIZE}. Only part of it was loaded: ${LOADED_PORTION_DESCRIPTION}. Keep index entries to one line under ~200 chars; move detail into topic files.
