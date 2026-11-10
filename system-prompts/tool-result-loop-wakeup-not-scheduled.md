<!--
name: Loop wakeup-not-scheduled tool_result
description: >-
  Tells the model no wake-up was scheduled because the loop hit its maximum
  duration and has ended, so it must not be re-issued.
ccVersion: 2.1.321
variables:
  - ADDITIONAL_LOOP_END_NOTE
-->
Wakeup not scheduled. The loop reached its maximum duration — the loop has ended; do not re-issue. ${ADDITIONAL_LOOP_END_NOTE}
