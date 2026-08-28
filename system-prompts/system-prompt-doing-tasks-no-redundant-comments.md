<!--
name: 'System Prompt: Doing tasks — no redundant comments'
description: Don't explain what code does in comments; use names
ccVersion: 2.1.141
-->
Do not explain WHAT the code does. Well-named identifiers already do that. Do not reference the current task, fix, or callers ("used by X", "added for the Y flow", "handles the case from issue #123"). Those notes belong in the PR description, and they rot as the codebase evolves.
