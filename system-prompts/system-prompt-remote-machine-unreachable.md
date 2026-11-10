<!--
name: 'System Prompt: Remote machine unreachable'
description: >-
  Notes that the named machine is not reachable, lists the usual causes, and
  states what brings it back.
ccVersion: 2.1.321
variables:
  - MACHINE_NAME
-->
- ${MACHINE_NAME}: not reachable right now: its Claude is not connected to this session (since when is not known), which most often means Claude is not running on ${MACHINE_NAME}, Remote Control is off there, or the computer is asleep or offline; what brings it back is Claude open on ${MACHINE_NAME} with Remote Control on and the computer awake and online.
