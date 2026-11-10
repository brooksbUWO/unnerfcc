<!--
name: 'Tool Description: Read (long lines need a character range)'
description: >-
  Notes that a file's lines are too long for line-based offset/limit chunking
  and suggests slicing by character range with a shell tool.
ccVersion: 2.1.321
variables:
  - READ_TOOL_NAME
-->
- Note: this file's lines are too long for ${READ_TOOL_NAME}'s offset/limit chunking. If a shell tool is available, slice by character range (e.g. python read()[A:B], dd, or cut -c) instead.
