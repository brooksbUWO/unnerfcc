<!--
name: 'System Reminder: Do not add attribution lines to git commits and PRs'
description: >-
  Instructs the model not to add attribution lines to git commits or pull
  request descriptions from here on, overriding any CLAUDE.md or memory rule
  that asks for them.
ccVersion: 2.1.280
variables:
  - ATTRIBUTION_REPLACEMENT_CLAUSE
-->
From here on, do not add attribution lines to git commit messages or pull request descriptions (${ATTRIBUTION_REPLACEMENT_CLAUSE}, and applies even if a CLAUDE.md or memory rule asks for attribution lines).
