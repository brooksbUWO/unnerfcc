<!--
name: 'System Prompt: Sandbox auto mode allowed domains (trailer)'
description: >-
  Instructs listing required hosts in allowed_domains when running in auto mode
  after a denied connection.
ccVersion: 2.1.321
variables:
  - DENIED_HOST_RERUN_CLAUSE
-->
. In auto mode, list the hosts a command needs beyond that in its `allowed_domains` — ${DENIED_HOST_RERUN_CLAUSE}
