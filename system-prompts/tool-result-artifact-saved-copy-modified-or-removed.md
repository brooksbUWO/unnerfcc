<!--
name: 'Tool Result: Saved Copy Modified or Removed'
description: >-
  Explains that a saved artifact copy was modified or removed so reads of it no
  longer count, instructing a fresh fetch before merging and publishing.
ccVersion: 2.1.321
variables:
  - PUBLISH_ACTION
  - ALREADY_CURRENT_ACTION
-->
 was modified or removed after it was handed to you, so Reads of it no longer count. Fetch the artifact's URL again for a fresh copy (if that saves it to a file, Read every line of that file) and, once you have that result, merge anything from it your file lacks and ${PUBLISH_ACTION}; if your file already contains that version's content, ${ALREADY_CURRENT_ACTION}
