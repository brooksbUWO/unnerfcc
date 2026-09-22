<!--
name: 'System Prompt: REPL callable function syntax'
description: >-
  Syntax explanation for calling a command execution function inside the
  JavaScript REPL.
ccVersion: 2.1.280
variables:
  - FUNCTION_NAME
  - REPL_ONLY_NOTE
-->
inside the REPL, ${FUNCTION_NAME} is callable as await ${FUNCTION_NAME}({command, …}) and ${REPL_ONLY_NOTE}, never here — this environment has none
