<!--
name: 'Tool Result: Live artifact version now counts as viewed'
description: >-
  Returns the artifact's live published version after a refused publish and
  states that merging edits onto it follows.
ccVersion: 2.1.321
variables:
  - PUBLISH_REFUSED_NOTICE
  - MERGE_INSTRUCTION
-->
${PUBLISH_REFUSED_NOTICE} That version now counts as viewed; its content and how to merge onto it follow.
${MERGE_INSTRUCTION} so no published content is lost
