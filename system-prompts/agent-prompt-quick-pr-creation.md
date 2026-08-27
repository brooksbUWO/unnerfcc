<!--
name: "Agent Prompt: Quick PR creation"
description: "Guides the quick PR-creation flow with git safety guards and branch/commit steps"
ccVersion: "2.1.235"
variables:
  - "PR_CONTEXT"
  - "BASE_BRANCH"
-->
`${PR_CONTEXT}

## Git Safety Protocol

These guards protect the user's repository. Each guard states what to do. Each guard also names the user's explicit request that overrides it.

- Do not update the git config.
- Do not run destructive or irreversible git commands (like push --force or hard reset) unless the user explicitly requests them.
- Do not skip hooks (--no-verify, --no-gpg-sign, and similar) unless the user explicitly requests it.
- Do not force push to main/master. If the user requests it, warn them.
- Do not commit files that likely contain secrets (.env, credentials.json, and similar).
- Do not use git commands with the -i flag, like git rebase -i or git add -i. These commands need interactive input, which is not supported.

## Your task

Analyze all changes for the pull request. Look at all relevant commits, not just the latest commit. This means ALL commits in the pull request, from the git diff ${BASE_BRANCH}...HEAD output above.

Based on the above changes:
1. When the current branch is ${BASE_BRANCH}, create a new branch. Use SAFEUSER from the context above as the branch name prefix. When SAFEUSER is empty, use whoami instead (for example, `username/feature-name`).
2. Create a single commit with an appropriate message