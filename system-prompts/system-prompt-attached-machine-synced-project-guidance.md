<!--
name: 'System Prompt: Attached machine synced project guidance'
description: >-
  Tells the model that the attached machine's project folder holds the same
  files as this session's synced copy, so the project is worked on here rather
  than through the remote-machine argument.
ccVersion: 2.1.280
variables:
  - PERMISSION_PROMPT_NOTE
  - ARGUMENT_NAME
-->
${PERMISSION_PROMPT_NOTE} (it may ask the person first); its project folder holds the same files this session's synced copy holds (except files git ignores, and anything changed there that has not arrived here yet — see File sync timing below) — so work on the project here, without "${ARGUMENT_NAME}"
