<!--
name: 'Tool Result: Remote machine bridge unreachable details'
description: >-
  Informs the model that the named computer is not answering, most often because
  Claude there is not connected to this session, so the call did not run.
ccVersion: 2.1.321
variables:
  - MACHINE_NAME
-->
${MACHINE_NAME} is not answering right now, most often because its Claude is not connected to this session (Claude is not running on ${MACHINE_NAME}, the computer is asleep or offline, or it is reconnecting after another session used it); the call did not run.
