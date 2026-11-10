<!--
name: 'System Reminder: Large JSON is not line-chunkable'
description: >-
  Tells the model that the read tool's line-based offset and limit cannot chunk
  this file, so it must extract slices another way.
ccVersion: 2.1.321
variables:
  - STRUCTURE_PROBE_GUIDANCE
  - READ_TOOL_NAME
-->
${STRUCTURE_PROBE_GUIDANCE} — ${READ_TOOL_NAME}'s line-based offset/limit will not chunk this file.
