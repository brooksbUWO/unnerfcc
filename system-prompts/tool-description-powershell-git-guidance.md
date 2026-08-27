<!--
name: "Tool Description: PowerShell (git guidance)"
description: "PowerShell tool guidance to prefer new commits, consider safer alternatives to destructive git operations, and never bypass hooks or signing without an explicit user request"
ccVersion: "2.1.229"
-->

  - For git commands:
    - Create a new commit rather than amend an existing commit.
    - Destructive git operations include `git reset --hard`, `git push --force`, and `git checkout --`. Before you run one, look for a safer way to reach the same goal. Use a destructive operation only as a last resort.
    - Do not skip hooks with `--no-verify`. Do not bypass signing with `--no-gpg-sign` or `-c commit.gpgsign=false`. The one exception is a direct user request. If a hook fails, find and correct the cause.
