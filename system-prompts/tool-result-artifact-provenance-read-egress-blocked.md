<!--
name: 'Tool Result: Provenance read blocked by the network allowlist'
description: >-
  Republish refusal telling the model this environment's network allowlist
  blocks reading the published page, so the decision-provenance check every
  republish performs cannot run here.
ccVersion: 2.1.257
variables:
  - EGRESS_ERROR_DETAIL
-->
could not read the published page to verify decision provenance (${EGRESS_ERROR_DETAIL}). This environment's network allowlist blocks the read, so republish cannot proceed from here — every republish verifies decision provenance against the published page.
