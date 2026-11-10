<!--
name: 'Tool Result: Background completion record not found'
description: >-
  Notes that no completion record was found for background work from the
  previous session, naming the stop reason and the resume hint.
ccVersion: 2.1.321
variables:
  - STOP_REASON
  - RESUME_HINT
-->
No completion record was found for it in the previous session. It may have been ${STOP_REASON}, or it may have been running when the previous Claude Code process exited.${RESUME_HINT}
