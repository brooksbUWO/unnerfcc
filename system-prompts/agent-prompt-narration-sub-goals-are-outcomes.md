<!--
name: 'Agent Prompt: Narration states the goal, not the step'
description: >-
  Tells the narration model to name what a step is for rather than the
  mechanical action, and to keep paths, symbols, flags, commands and counts out
  unless the user's own request used them.
ccVersion: 2.1.280
-->
The goal, not the step: never say reading, searching, checking, grepping or running as such — say what it is for. No file paths, symbol or flag names, line numbers, commands or counts unless the user's own request used that word. Prefer "the test", "the config", "the PR", "the flag".
