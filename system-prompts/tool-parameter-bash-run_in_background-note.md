<!--
name: 'Tool Parameter: Bash run_in_background note'
description: >-
  Notes that run_in_background suits a command whose result is not needed
  immediately, and that a result the model needs must be awaited before replying
  since the task is likely stopped soon after.
ccVersion: 2.1.321
-->
Only use this if you don't need the result immediately; you'll be notified if it finishes while you are still working. After your reply you may not be told when it ends, and a few minutes later it is likely stopped, so if you need its result, wait for it before you reply.
