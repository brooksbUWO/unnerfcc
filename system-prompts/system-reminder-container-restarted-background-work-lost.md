<!--
name: 'System Reminder: Container restarted background work lost'
description: >-
  System reminder informing that background work was lost to a container
  restart, and that it should be re-created only if something still waits on it.
ccVersion: 2.1.321
variables:
  - BACKGROUND_WORK_LIST
  - RECREATE_ACTION
-->
The container running this session was restarted before background work reported back: ${BACKGROUND_WORK_LIST}. ${RECREATE_ACTION} if still needed (a long-running server or watcher that nothing is waiting on does not need restarting now), or tell the user what was lost.
