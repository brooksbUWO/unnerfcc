<!--
name: "System Reminder: Memory extraction recent context only"
description: "Restricts the memory extraction subagent to saving facts from only the recent conversation window"
ccVersion: "2.1.173"
variables:
  - "RECENT_MESSAGE_COUNT"
  - "TRAILING_CONSTRAINTS"
-->
Update your persistent memories only from the last ~${RECENT_MESSAGE_COUNT} messages. Do not spend turns verifying that content further: no grepping source files, no reading code to verify a pattern, no git commands.${TRAILING_CONSTRAINTS}
