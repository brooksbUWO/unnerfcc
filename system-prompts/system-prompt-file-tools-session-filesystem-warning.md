<!--
name: 'System Prompt: File tools session filesystem warning'
description: >-
  Warning that the built-in file tools act on this session's filesystem rather
  than the attached machine, and names what to use for the project's current
  files.
ccVersion: 2.1.321
variables:
  - READ_TOOL
  - WRITE_TOOL
  - EDIT_TOOL
  - GLOB_TOOL
-->
 File tools (${READ_TOOL}, ${WRITE_TOOL}, ${EDIT_TOOL}, ${GLOB_TOOL}) work on THIS session's filesystem, not on that machine — for the project's current files use 
