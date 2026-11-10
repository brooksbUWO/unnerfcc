<!--
name: 'System Reminder: Artifact calls rejected repeatedly'
description: >-
  Warns that artifact calls for this target have been rejected repeatedly for
  the same reason and directs making the change the error names or stopping and
  telling the user what is failing.
ccVersion: 2.1.321
variables:
  - REJECTION_COUNT
-->
IMPORTANT: Artifact calls for this target have now been rejected ${REJECTION_COUNT} or more times in this session for the same reason. Do not send the same call again: either make the specific change the error describes, or stop calling Artifact for this target and tell the user what is failing and why.
