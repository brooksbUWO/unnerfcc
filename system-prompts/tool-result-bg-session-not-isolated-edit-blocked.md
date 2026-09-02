<!--
name: 'Tool Result: Background session not isolated (edit blocked)'
description: >-
  Tells the model this background session has not isolated its changes yet and
  to call the isolation tool first so edits land in a worktree, then retry the
  edit against the worktree path.
ccVersion: 2.1.257
variables:
  - ENTER_WORKTREE_TOOL_NAME
-->
This background session hasn't isolated its changes yet. Call ${ENTER_WORKTREE_TOOL_NAME} first so edits land in a worktree instead of the shared checkout, then retry this edit using the worktree path
