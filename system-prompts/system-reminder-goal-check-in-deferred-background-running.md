<!--
name: 'System Reminder: Goal check-in deferred while background work runs'
description: >-
  Tells the model the active goal check-in is deferred because background work
  is still running, and lists that work.
ccVersion: 2.1.280
variables:
  - GOAL_TEXT
  - DEFERRAL_MINUTES
-->
${GOAL_TEXT} is still active, and evaluation has been deferred for ${DEFERRAL_MINUTES} min because background work is still running:
