<!--
name: 'Tool Result: Subagent report cut so the note fits'
description: >-
  Harness note telling the model the subagent's report was truncated to its
  first N characters so that it and the following note arrive together.
ccVersion: 2.1.257
variables:
  - NOTE_PREFIX
  - ORIGINAL_REPORT_LENGTH
  - TRUNCATED_REPORT_LENGTH
-->
${NOTE_PREFIX}the subagent's report was cut from ${ORIGINAL_REPORT_LENGTH} to its first ${TRUNCATED_REPORT_LENGTH} characters so that it and the note below arrive together.]
