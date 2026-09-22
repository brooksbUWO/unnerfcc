<!--
name: 'Tool Result: Artifact live subscription did not arm notice'
description: >-
  Reports that the live subscription did not arm with the reason, that this
  session is not watching and does not track new versions, and not to claim to
  be watching meanwhile.
ccVersion: 2.1.280
variables:
  - FAILURE_REASON
  - RETRY_ADVICE
-->
 did not arm — ${FAILURE_REASON}. This session is NOT watching it and does not keep track of new versions of it; ${RETRY_ADVICE}, and do not claim to be watching it meanwhile.
