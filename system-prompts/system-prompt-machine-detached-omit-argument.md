<!--
name: 'System Prompt: Machine detached omit argument'
description: >-
  Notice that no machine is attached any more, directing the model to omit the
  machine argument, run commands here, and say so when the task needs that
  machine's files, tools or logins.
ccVersion: 2.1.321
variables:
  - DETACH_NOTICE
  - MACHINE_ARGUMENT
-->
${DETACH_NOTICE}; omit "${MACHINE_ARGUMENT}" and run commands here. If the task needs that machine's files, tools or logins, say so instead of doing it here.
