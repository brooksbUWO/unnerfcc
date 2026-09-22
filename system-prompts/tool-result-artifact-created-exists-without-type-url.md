<!--
name: 'Tool Result: Artifact exists, publish without type_url'
description: >-
  Instruction noting the Artifact exists and further publishes must omit
  type_url.
ccVersion: 2.1.280
variables:
  - PUBLISH_ACTION_HINT
  - FILES_SECTION
-->
. The Artifact exists — ${PUBLISH_ACTION_HINT}, WITHOUT `type_url` (passing it again would create another Artifact).${FILES_SECTION}
