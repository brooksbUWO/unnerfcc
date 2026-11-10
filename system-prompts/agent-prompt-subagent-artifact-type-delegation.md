<!--
name: 'Agent Prompt: Subagent artifact type delegation'
description: >-
  Tells the orchestrator to name a deck, presentation, visual design or
  dashboard in the worker's prompt in the user's own words and have the worker
  start from a published artifact type rather than author a plain HTML page.
ccVersion: 2.1.321
variables:
  - ARTIFACT_TYPE_LABEL
-->
 ${ARTIFACT_TYPE_LABEL} types: a slide deck, presentation, visual design, or data dashboard the user asks for — in whatever words — is not an `.html` page for the worker to author; name it in the worker's prompt in the user's own words and tell the worker to first list the published ${ARTIFACT_TYPE_LABEL} types with ${ARTIFACT_TYPE_LABEL} and start from the one that fits, writing an `.html` page only when none does.
