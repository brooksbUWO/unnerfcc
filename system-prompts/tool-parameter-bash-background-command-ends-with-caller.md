<!--
name: 'Tool Parameter: Background command ends with its caller'
description: >-
  Model-facing schema note for the flag that marks a backgrounded command as
  terminated at its caller's final response, so no completion notification can
  follow.
ccVersion: 2.1.321
-->
True when this backgrounded command is terminated at its caller's final response, so no completion notification can follow (a synchronous subagent's command, or a headless session that takes no further input and is not waiting for background commands); absent when the command survives
