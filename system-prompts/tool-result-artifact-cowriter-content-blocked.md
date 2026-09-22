<!--
name: 'Tool Result: Artifact co-writer content blocked'
description: >-
  Error result when an action touches an artifact modified by a co-writer
  without prior user permission.
ccVersion: 2.1.280
variables:
  - BLOCKED_CONTENT_KIND
-->
a co-writer has published to this artifact, so its ${BLOCKED_CONTENT_KIND} are someone else's content — nothing was returned; retry the same action so it is checked again (the user is asked once where a prompt can reach them)
