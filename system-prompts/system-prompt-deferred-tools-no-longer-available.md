<!--
name: 'System Prompt: Deferred tools no longer available'
description: >-
  Informs the model that specific deferred tools are no longer available in this
  session, followed by the do-not-search clause.
ccVersion: 2.1.280
variables:
  - DEFERRED_TOOL_NOUN
  - DO_NOT_SEARCH_CLAUSE
-->
The following ${DEFERRED_TOOL_NOUN}s are no longer available in this session. ${DO_NOT_SEARCH_CLAUSE}:
