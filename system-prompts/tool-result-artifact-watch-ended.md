<!--
name: 'Tool Result: Artifact watch ended'
description: >-
  Reports that an artifact watch ended with its reason, that this session no
  longer keeps track of new versions of that artifact, and what to do next.
ccVersion: 2.1.280
variables:
  - WATCH_END_REASON
  - WATCH_FOLLOW_UP_NOTE
-->
 ended — ${WATCH_END_REASON}. This session no longer keeps track of new versions of it; ${WATCH_FOLLOW_UP_NOTE}.
