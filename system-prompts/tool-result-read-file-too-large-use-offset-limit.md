<!--
name: 'Tool Result: File too large — use offset and limit'
description: >-
  Read failure guidance telling the model to use offset and limit to read
  portions of an oversized file, or to search for the specific content instead.
ccVersion: 2.1.321
variables:
  - CONTENT_TOKENS
  - MAX_TOKENS
  - ADDITIONAL_READ_GUIDANCE
-->
File content (${CONTENT_TOKENS} tokens) exceeds maximum allowed tokens (${MAX_TOKENS}). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.${ADDITIONAL_READ_GUIDANCE}
