<!--
name: Memory Sync Paused After Failures
description: >-
  Tells the model that sync paused for a memory store after repeated failures,
  that recent writes are local only, and that sync retries automatically.
ccVersion: 2.1.280
variables:
  - PAUSE_REASON
  - TRAILING_DETAIL_CLAUSE
-->
Memory sync is paused for one of your memory stores after repeated failures (${PAUSE_REASON}). ${TRAILING_DETAIL_CLAUSE}Recent memory writes are saved locally but are NOT being persisted to shared memory. Sync retries automatically every few minutes.
