<!--
name: 'System Reminder: Conversation summary part omitted'
description: >-
  Notes that part of the earlier conversation was too large to include in the
  summary and tells the model to say so plainly if the task depends on it rather
  than guessing.
ccVersion: 2.1.321
variables:
  - OMITTED_RANGE_CLAUSE
  - TRAILING_CLAUSE
-->


Note: part of the earlier conversation was too large to include and is NOT covered by this summary${OMITTED_RANGE_CLAUSE}. If the task turns out to depend on something from that part, say so plainly rather than guessing at it.${TRAILING_CLAUSE}
