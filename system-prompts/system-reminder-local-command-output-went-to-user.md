<!--
name: 'System Reminder: Local command output went straight to the user'
description: >-
  Records a command that ran directly in Claude Code rather than as a request to
  the model, whose output went straight to the user, as context for later
  messages.
ccVersion: 2.1.321
variables:
  - REMINDER_TAG_NAME
-->
<${REMINDER_TAG_NAME}>The command below was run directly in Claude Code, not sent to you as a request, and its output goes straight to the user. It's recorded here as context for later messages.</${REMINDER_TAG_NAME}>
