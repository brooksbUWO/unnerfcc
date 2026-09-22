<!--
name: 'Tool Result: Artifact live version reached earlier'
description: >-
  Refuses a publish because the artifact's live version already reached the
  model in this same turn, so the publish could not have been built on it.
ccVersion: 2.1.280
variables:
  - LIVE_VERSION_DETAIL
-->
This artifact's live version reached you earlier in this same turn${LIVE_VERSION_DETAIL}, so this publish could not have been built on it: nothing was published. Publish again in your next turn, built on that content — do not resend this content unchanged.
