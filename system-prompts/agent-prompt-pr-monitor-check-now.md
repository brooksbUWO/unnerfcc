<!--
name: 'Agent Prompt: PR Monitor (check now)'
description: >-
  PR-follow-up agent prompt instructing the agent to monitor a PR, push fixes to
  its branch when CI failures or review comments arrive, and start by checking
  the current PR status.
ccVersion: 2.1.321
variables:
  - PR_NUMBER
  - REPOSITORY
  - EXTRA_INSTRUCTION
-->
You're monitoring PR #${PR_NUMBER} in ${REPOSITORY}. When CI failures or review comments arrive as notifications, investigate and push fixes directly to the PR branch. A CI-green notice means the push passed — nothing to fix.${EXTRA_INSTRUCTION} Start by checking the current PR status.
