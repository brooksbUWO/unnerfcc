<!--
name: 'Tool Result: Remote machine protocol version mismatch'
description: >-
  Reports that the attached machine shares no usable protocol version so the
  call did not run, with the update recommendation.
ccVersion: 2.1.321
variables:
  - MACHINE_NAME
  - MISMATCH_DETAIL
  - UPDATE_RECOMMENDATION
  - RUN_IMPOSSIBLE_NOTE
-->
${MACHINE_NAME} is attached but ${MISMATCH_DETAIL}; the call did not run; ${UPDATE_RECOMMENDATION}. ${RUN_IMPOSSIBLE_NOTE}
