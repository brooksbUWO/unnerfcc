<!--
name: 'Tool Result: Quickstart core type instructions'
description: >-
  Instructs the model to start from the listed first-party type and publish with
  its type_url, or to route the document to the connector and its skill when no
  type matches.
ccVersion: 2.1.321
variables:
  - PUBLISH_PARAMS
  - CONNECTOR_NOTE
  - FORMAT_SKILL_NOTE
  - NEXT_STEP
-->
` (a row opens with the type's first-party tier in brackets, when it has one, then its title in quotes), start from that type: publish with its `type_url`, ${PUBLISH_PARAMS}; if none does, the document goes to the connector, and to its skill when one appears in your skill list. ${CONNECTOR_NOTE}${FORMAT_SKILL_NOTE} ${NEXT_STEP}
