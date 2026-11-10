<!--
name: 'Tool Parameter: Bash run_in_background guidance'
description: >-
  Explains Bash run_in_background behavior and that commands do not need a
  trailing ampersand.
ccVersion: 2.1.321
variables:
  - NOTIFICATION_CLAUSE
-->
You can use the `run_in_background` parameter to run the command in the background. Use this only for a result you do not need at once. ${NOTIFICATION_CLAUSE} You do not need to use '&' at the end of the command when using this parameter.
