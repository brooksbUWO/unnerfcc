<!--
name: 'Task Notification: Artifact auto-reply is notify-only'
description: >-
  task-notification injected when the session's permission mode allows only
  notification instead of an automatic reply to waiting artifact comments,
  telling the model to read the thread and reply with the Artifact tool itself
  since later comments will not repeat the notice.
ccVersion: 2.1.321
variables:
  - PENDING_COMMENTS_NOTICE_PREFIX
  - ARTIFACT_TOOL_NAME
  - ADDITIONAL_NOTE
  - SECOND_ADDITIONAL_NOTE
-->
${PENDING_COMMENTS_NOTICE_PREFIX}. Auto-reply is notify-only in this permission mode — read and reply with ${ARTIFACT_TOOL_NAME} when ready (further comments will not repeat this notice).${ADDITIONAL_NOTE}${SECOND_ADDITIONAL_NOTE}
