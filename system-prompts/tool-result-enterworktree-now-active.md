<!--
name: 'Tool Result: Session now working in the worktree'
description: >-
  Confirms the session has moved into the new worktree and explains that
  ExitWorktree leaves mid-session while exiting the session prompts for cleanup.
ccVersion: 2.1.321
variables:
  - WORKTREE_CREATED_MESSAGE
  - ADDITIONAL_WORKTREE_NOTE
  - SECOND_ADDITIONAL_WORKTREE_NOTE
  - WORKTREE_EXIT_GUIDANCE
-->
${WORKTREE_CREATED_MESSAGE}.${ADDITIONAL_WORKTREE_NOTE}${SECOND_ADDITIONAL_WORKTREE_NOTE} The session is now working in the worktree. ${WORKTREE_EXIT_GUIDANCE}
