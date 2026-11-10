<!--
name: 'System Reminder: Auto mode did not approve auto-reply'
description: >-
  Notifies that auto mode did not approve an unattended comment auto-reply and
  instructs to read and reply with the Artifact tool when ready.
ccVersion: 2.1.321
variables:
  - PENDING_COMMENTS_NOTICE
  - ARTIFACT_TOOL_NAME
  - ADDITIONAL_NOTE
  - SECOND_ADDITIONAL_NOTE
-->
${PENDING_COMMENTS_NOTICE}. Auto mode did not approve an unattended auto-reply, so the reply was not posted — read and reply with ${ARTIFACT_TOOL_NAME} when ready (further comments will not repeat this notice).${ADDITIONAL_NOTE}${SECOND_ADDITIONAL_NOTE}
