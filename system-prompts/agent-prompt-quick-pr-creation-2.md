<!--
name: 'Agent Prompt: Quick PR creation'
description: >-
  PR steps for the quick skill — push the branch to the configured remote, then
  edit the existing PR for the current branch or create one with an inline
  multi-line body, keeping the title short.
ccVersion: 2.1.321
variables:
  - PR_EDIT_SUFFIX
  - PR_CREATE_SUFFIX
  - PR_BODY_GUIDANCE
-->

3. Push the branch to the repo's remote (usually `origin`; use the remote this repo is actually configured with)
4. If a PR already exists for this branch (check the gh pr view output above), update the PR title and body using `gh pr edit --title "..." --body "..."` with NO PR number/URL selector (gh resolves the current branch's PR when no selector is given) to reflect the current diff${PR_EDIT_SUFFIX}. Otherwise, create a pull request using `gh pr create` with the multi-line body syntax shown below${PR_CREATE_SUFFIX}; the body goes inline, never `--body-file`/`-F` (refused while this skill runs).
   - IMPORTANT: Keep PR titles short (under 70 characters). Use the body for details.
   - ${PR_BODY_GUIDANCE}
