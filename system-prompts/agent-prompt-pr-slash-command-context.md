<!--
name: 'Agent Prompt: PR slash command context block'
description: >-
  Context block for the /pr command â€” injects git status, the current branch,
  the commits since the base branch, and the full diff against it.
ccVersion: 2.1.257
variables:
  - COMMAND_PREAMBLE
  - BASE_BRANCH
-->
## Context

- Current git status: !`git status`
- Current branch: !`git branch --show-current`
- Commits since origin/${COMMAND_PREAMBLE}: !`git log --oneline origin/${COMMAND_PREAMBLE}..HEAD`
- Full diff vs origin/${COMMAND_PREAMBLE}: !`git diff origin/${COMMAND_PREAMBLE}...HEAD`${BASE_BRANCH}
