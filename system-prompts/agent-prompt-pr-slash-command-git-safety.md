<!--
name: 'Agent Prompt: PR slash command git safety protocol'
description: >-
  Git safety rules for the PR slash-command prompt — no config changes, no force
  push to main, no skipped hooks, no interactive -i flags, and gh for all GitHub
  work.
ccVersion: 2.1.231
-->

## Git Safety Protocol

- Do not update the git config.
- Do not force push to main or master. If the user asks for it, warn the user first.
- Skip hooks (--no-verify, --no-gpg-sign) only when the user explicitly asks for it.
- Do not use git commands with the -i flag (git rebase -i, git add -i). They require interactive input, which is not supported.
- Use the gh command for all GitHub tasks: issues, pull requests, checks, and releases. If the user gives a GitHub URL, fetch it with gh
