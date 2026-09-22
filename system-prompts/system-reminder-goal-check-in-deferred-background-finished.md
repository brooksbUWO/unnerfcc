<!--
name: 'System Reminder: Goal check-in resumed, background work finished'
description: >-
  Tells the model the active goal check-in was deferred while background work
  ran, that the work is no longer running, and to continue toward the goal.
ccVersion: 2.1.280
variables:
  - GOAL_TEXT
  - DEFERRAL_MINUTES
-->
${GOAL_TEXT} is still active. Its evaluation was deferred for ${DEFERRAL_MINUTES} min while background work ran, and that work is no longer running (it finished or was stopped without reporting back). Continue toward the goal.
