<!--
name: 'Task Notification: Background agents in-process state lost'
description: >-
  Task notification reporting that multiple background agents did not complete
  and lost their in-process state.
ccVersion: 2.1.321
variables:
  - RESUME_HINT
-->
They were running when the previous Claude Code process exited and did not complete. Their in-process state was lost. ${RESUME_HINT}
