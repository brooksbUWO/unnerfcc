<!--
name: 'Tool Description: Bash (PR creation close-out)'
description: >-
  Closing notes of the pull-request workflow — which tools not to use, returning
  the PR URL, and the common gh operations.
ccVersion: 2.1.321
variables:
  - FORBIDDEN_TOOL_1
  - FORBIDDEN_TOOL_2
-->

</example>

Important:
- DO NOT use the ${FORBIDDEN_TOOL_1} or ${FORBIDDEN_TOOL_2} tools
- Return the PR URL when you're done, so the user can see it

# Other common operations
- View comments on a Github PR: gh api repos/foo/bar/pulls/123/comments
