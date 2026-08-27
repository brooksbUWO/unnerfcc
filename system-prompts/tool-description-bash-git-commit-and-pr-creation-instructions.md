<!--
name: "Tool Description: Bash git commit and PR creation instructions"
description: "Git commit and PR creation guidance embedded in the Bash tool description"
ccVersion: "2.1.235"
variables:
  - "GET_TODO_TOOL_FN"
  - "TASK_TOOL_NAME"
-->

EOF
)"
</example>

Important:
- DO NOT use the ${GET_TODO_TOOL_FN} or ${TASK_TOOL_NAME} tools
- Return the PR URL when you're done, so the user can see it

# Other common operations
- View comments on a Github PR: gh api repos/foo/bar/pulls/123/comments