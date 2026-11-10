<!--
name: 'Tool Result: Monitor expired with no events'
description: >-
  Notifies the model that a background monitor expired with no events delivered
  and advises re-arming or widening the filter.
ccVersion: 2.1.321
variables:
  - TIMEOUT
  - REARM_ADVICE
-->
[Monitor expired after ${TIMEOUT} with no events delivered. ${REARM_ADVICE} — and widen the filter if silence was unexpected.]
