<!--
name: >-
  System Prompt: Avoiding Unnecessary Sleep Commands (part of PowerShell tool
  description)
description: >-
  Guidelines for avoiding unnecessary sleep commands in PowerShell, starting
  with not sleeping between commands that can run immediately.
ccVersion: 2.1.321
-->
  - Avoid unnecessary `Start-Sleep` commands:
    - Do not sleep between commands that can run immediately — just run them.
