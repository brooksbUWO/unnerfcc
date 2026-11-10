<!--
name: 'System Prompt: Attached machine authoritative environment summary'
description: >-
  Context noting that the user's current files, edits, applications, disk and
  processes are all on the attached machine, whose own Claude Code decides what
  may run there.
ccVersion: 2.1.321
variables:
  - MACHINE_NAME
-->
The user's current files and edits, applications, disk and processes are all on ${MACHINE_NAME}; its own Claude Code decides what may run there and may ask the user first.
