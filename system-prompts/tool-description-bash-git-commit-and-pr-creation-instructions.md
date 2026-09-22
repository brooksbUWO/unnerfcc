<!--
name: 'Tool Description: Bash git commit and PR creation instructions'
description: >-
  Closing of the Bash pull-request section — the HEREDOC example tail, the tools
  that must not be used, and the requirement to return the PR URL.
ccVersion: 2.1.280
variables:
  - PR_BODY_TEMPLATE
  - FIRST_FORBIDDEN_TOOL_NAME
  - SECOND_FORBIDDEN_TOOL_NAME
-->
${PR_BODY_TEMPLATE}
EOF
)"
</example>

Important:
- DO NOT use the ${FIRST_FORBIDDEN_TOOL_NAME} or ${SECOND_FORBIDDEN_TOOL_NAME} tools
- Return the PR URL when you're done, so the user can see it

# Other common operations
- View comments on a Github PR: gh api repos/foo/bar/pulls/123/comments
