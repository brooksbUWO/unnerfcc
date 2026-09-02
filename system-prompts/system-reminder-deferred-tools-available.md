<!--
name: 'System Reminder: Deferred tools available'
description: >-
  Tells the model which deferred tools are now available, that their schemas are
  not loaded so direct calls fail, and to load them with a select: query first.
ccVersion: 2.1.257
variables:
  - TOOL_SEARCH_TOOL_NAME
-->
The following deferred tools are now available via ${TOOL_SEARCH_TOOL_NAME}. Their schemas are NOT loaded — calling them directly will fail with InputValidationError. Use ${TOOL_SEARCH_TOOL_NAME} with query "select:<name>[,<name>...]" to load tool schemas before calling them:
