<!--
name: 'Tool Description: Resume watching artifact with reason'
description: >-
  Action description for resuming a watch that was stopped earlier in this
  session, naming the reason the watch stopped.
ccVersion: 2.1.280
variables:
  - STOP_REASON
  - STATUS_PREFIX
  - STATUS_SUFFIX
  - EXTRA_NOTE
-->
resume watching an artifact whose watch was stopped earlier in this session (${STOP_REASON}) → ${STATUS_PREFIX}${STATUS_SUFFIX}${EXTRA_NOTE}
