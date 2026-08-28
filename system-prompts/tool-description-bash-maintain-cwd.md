<!--
name: 'Tool Description: Bash (maintain cwd)'
description: 'Bash tool instruction: use absolute paths and avoid cd'
ccVersion: 2.1.113
-->
Keep your current working directory through the session. Use absolute paths and do not use `cd`. If the user asks for `cd`, you can use it. Never put `cd <current-directory>` before a `git` command. The `git` command already works on the current tree. The compound command triggers a permission prompt.
