<!--
name: "Agent Prompt: PR follow-up cron"
description: "Cron prompt for checking a pull request created in the session and fixing failures, comments, or conflicts"
ccVersion: "2.1.173"
variables:
  - "PR_INSTRUCTIONS_PREFIX"
  - "PR_GENERATED_WITH_CLAUDE_CODE"
  - "PR_NUMBER"
  - "GITHUB_REPOSITORY"
  - "CRON_DELETE_TOOL_NAME"
  - "PR_COMMON_OPERATIONS_NOTE"
-->
${PR_INSTRUCTIONS_PREFIX}${PR_GENERATED_WITH_CLAUDE_CODE} (created in this session). Get the PR state with `gh pr view ${PR_NUMBER} -R ${GITHUB_REPOSITORY} --json state,mergeable,mergeStateStatus,statusCheckRollup`. Get new review comments with `gh api --paginate repos/${GITHUB_REPOSITORY}/pulls/${PR_NUMBER}/comments`. If the state is MERGED or CLOSED, delete this cron with ${CRON_DELETE_TOOL_NAME} and report the outcome. If CI is failing, or comments are unaddressed, or there are merge conflicts, fix them and push. If none of these apply, there is nothing to do. In that case, complete the turn without commentary.${PR_COMMON_OPERATIONS_NOTE}
