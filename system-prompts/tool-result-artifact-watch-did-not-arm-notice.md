<!--
name: 'Tool Result: Artifact live subscription did not arm notice'
description: >-
  Reports that the live subscription did not arm with the reason, that this
  session is not watching and does not keep track of new versions, and not to
  claim to be watching meanwhile.
ccVersion: 2.1.321
variables:
  - FAILURE_REASON
-->
 did not arm — ${FAILURE_REASON}. This session is NOT watching it and does not keep track of new versions of it; 
