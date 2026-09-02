<!--
name: 'Tool Result: Live artifact version now counts as viewed'
description: >-
  Returns the artifact's live published version after a refused publish and
  requires merging edits onto it, without resending the previous content
  unchanged, before publishing again.
ccVersion: 2.1.257
variables:
  - PUBLISH_REFUSED_NOTICE
  - LIVE_CONTENT_BLOCK
  - LIVE_CONTENT_END_MARKER
-->
${PUBLISH_REFUSED_NOTICE} That version is below and now counts as viewed: merge your edits onto it so no published content is lost, then publish again — do not resend your previous content unchanged.${LIVE_CONTENT_BLOCK}${LIVE_CONTENT_END_MARKER}
