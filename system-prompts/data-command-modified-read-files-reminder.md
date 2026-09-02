<!--
name: 'Data: Command modified read files reminder'
description: >-
  Warns the model that a command modified files it had previously read, and to
  re-read them before editing.
ccVersion: 2.1.257
variables:
  - MODIFIED_FILE_PATHS
  - ADDITIONAL_FILES_SUFFIX
  - FILE_READ_TOOL_NAME
-->
 you've previously read: ${MODIFIED_FILE_PATHS}${ADDITIONAL_FILES_SUFFIX}. Call ${FILE_READ_TOOL_NAME} before editing.]
