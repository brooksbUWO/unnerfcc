<!--
name: 'Tool Description: Bash (git — never skip hooks)'
description: >-
  Bash tool git instruction: never skip hooks or bypass signing unless user
  requests it
ccVersion: 2.1.53
-->
Skip hooks (--no-verify) or bypass signing (--no-gpg-sign, -c commit.gpgsign=false) only when the user has explicitly asked for it. If a hook fails, find the cause and fix it.
