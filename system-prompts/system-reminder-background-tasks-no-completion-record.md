<!--
name: 'System Reminder: Background tasks with no completion record'
description: >-
  Reports previous-session background agents that have no completion record, the
  recovery guidance, and that scan-marker ids in the notification are not real
  tasks.
ccVersion: 2.1.280
variables:
  - TASK_ID_LIST
  - NOTIFICATION_TAG_NAME
  - INNER_NOTIFICATION_TAG_NAME
  - RECOVERY_GUIDANCE
  - SCAN_MARKER_PREFIX
  - CLOSING_TAG_NAME
-->
. ${TASK_ID_LIST}</${NOTIFICATION_TAG_NAME}>
<${INNER_NOTIFICATION_TAG_NAME}>No completion record was found for them in the previous session. ${RECOVERY_GUIDANCE} Task ids in this notification beginning with "${SCAN_MARKER_PREFIX}" are internal scan markers, not tasks.</${INNER_NOTIFICATION_TAG_NAME}>
</${CLOSING_TAG_NAME}>
