<!--
name: Edit all-occurrences replaced result
description: >-
  Edit tool_result content sent to the model confirming the file was updated and
  all occurrences were successfully replaced; model-facing.
ccVersion: 2.1.280
variables:
  - UPDATED_FILE_PATH
  - FILE_STATE_SUFFIX
  - USER_MODIFIED_SUFFIX
  - TRAILING_NOTE_SUFFIX
-->
The file ${UPDATED_FILE_PATH} has been updated${FILE_STATE_SUFFIX}. All occurrences were successfully replaced.${USER_MODIFIED_SUFFIX}${TRAILING_NOTE_SUFFIX}
