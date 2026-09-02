<!--
name: 'Tool Result: Parent background session not isolated'
description: >-
  Tells the model the subagent's parent background session has not isolated its
  changes, so writes to the shared checkout are blocked and the agent must be
  re-spawned with worktree isolation.
ccVersion: 2.1.257
-->
This subagent's parent bg session hasn't isolated yet, so writes to the shared checkout are blocked. Re-spawn this agent with `isolation: "worktree"`
