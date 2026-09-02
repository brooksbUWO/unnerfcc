<!--
name: 'Agent Prompt: Quick PR creation'
description: >-
  Streamlined prompt for creating a commit and pull request with pre-populated
  git context
ccVersion: 2.1.257
variables:
  - SAFE_USER_NAME
  - WHOAMI_OUTPUT
  - BASE_BRANCH_NAME
-->
## Context

- `SAFEUSER`: ${SAFE_USER_NAME}
- `whoami`: ${WHOAMI_OUTPUT}
- `git status`: !`git status`
- `git diff HEAD`: !`git diff HEAD`
- `git branch --show-current`: !`git branch --show-current`
- `git diff ${BASE_BRANCH_NAME}...HEAD`: !`git diff ${BASE_BRANCH_NAME}...HEAD`
- `gh pr view --json number`: !`
