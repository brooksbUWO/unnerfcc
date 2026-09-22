<!--
name: 'Tool Result: Memory sync paused for store'
description: >-
  Tells the model that sync is paused for a named memory store and that affected
  memory writes are not being persisted to shared memory.
ccVersion: 2.1.280
variables:
  - MEMORY_STORE_NAME
  - PAUSE_REASON
  - TRAILING_DETAIL_CLAUSE
-->
Memory sync is paused for one of your memory stores (${MEMORY_STORE_NAME}): ${PAUSE_REASON}${TRAILING_DETAIL_CLAUSE} Affected memory writes are NOT being persisted to shared memory and will be lost when this session's machine is recycled.
