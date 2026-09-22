<!--
name: Write file-created tool result
description: >-
  The Write tool's success tool_result content shown to the model after creating
  a file; model-facing.
ccVersion: 2.1.280
variables:
  - CREATED_FILE_PATH
  - FILE_STATE_SUFFIX
  - USER_MODIFIED_SUFFIX
  - TRAILING_NOTE_SUFFIX
-->
File created successfully at: ${CREATED_FILE_PATH}${FILE_STATE_SUFFIX}${USER_MODIFIED_SUFFIX}${TRAILING_NOTE_SUFFIX}
