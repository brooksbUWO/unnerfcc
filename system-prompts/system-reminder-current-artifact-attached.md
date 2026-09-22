<!--
name: 'System Reminder: Current artifact attached'
description: >-
  Tells the model the user attached an artifact as the session's current
  artifact of interest and that it must re-read it before editing or
  republishing.
ccVersion: 2.1.280
variables:
  - PREFIX_NOTE
  - EXTRA_NOTE
  - ARTIFACT_ID
-->
${PREFIX_NOTE}${EXTRA_NOTE}The user attached the artifact ${ARTIFACT_ID} to this session as the current artifact of interest. re-read it before editing or republishing (
