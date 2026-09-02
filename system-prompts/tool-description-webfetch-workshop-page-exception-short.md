<!--
name: 'Tool Description: WebFetch workshop page exception (short)'
description: >-
  Shorter variant routing workshop pages to the Artifact tool's read_page_data
  action with the workshop-decisions schema, which the workshop skill requires
  instead of a content read.
ccVersion: 2.1.257
variables:
  - ARTIFACT_TOOL_NAME
-->
for a workshop page use the ${ARTIFACT_TOOL_NAME} tool's read_page_data action with schema "workshop-decisions" — the workshop skill forbids a content read there; otherwise 
