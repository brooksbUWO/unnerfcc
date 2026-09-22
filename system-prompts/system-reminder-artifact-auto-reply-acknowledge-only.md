<!--
name: 'System Reminder: Auto-reply can only acknowledge'
description: >-
  Tail of the auto-reply-posted notification telling the model the automatic
  reply only answered and changed nothing, so it must read the thread and make
  any requested artifact change itself.
ccVersion: 2.1.280
variables:
  - ARTIFACT_URL
-->
 on artifact ${ARTIFACT_URL} — a reply only: it may answer a question, but nothing in the artifact was changed. If the thread asks for a change to the artifact, read the thread and make the change yourself if appropriate.
