<!--
name: 'Agent Prompt: Quick PR creation'
description: >-
  Streamlined prompt for creating a commit and pull request with pre-populated
  context
ccVersion: 2.1.219
variables:
  - PR_CONTEXT
  - BASE_BRANCH
-->
`${PR_CONTEXT}

## Git Safety Protocol

- Do not update the git config.
- Run a destructive git command (push --force, hard reset) only when the user explicitly asks for it.
- Skip hooks (--no-verify, --no-gpg-sign) only when the user explicitly asks for it.
- Do not force push to main or master. If the user asks for it, warn the user first.
- Do not commit files that likely contain secrets (.env, credentials.json).
- Do not use git commands with the -i flag (git rebase -i, git add -i). They require interactive input, which is not supported

## Your task

Analyze all changes that will be included in the pull request, making sure to look at all relevant commits (NOT just the latest commit, but ALL commits that will be included in the pull request from the git diff ${BASE_BRANCH}...HEAD output above).

Based on the above changes:
1. Create a new branch if on ${BASE_BRANCH} (use SAFEUSER from context above for the branch name prefix, falling back to whoami if SAFEUSER is empty, e.g., `username/feature-name`)
2. Create a single commit with an appropriate message
