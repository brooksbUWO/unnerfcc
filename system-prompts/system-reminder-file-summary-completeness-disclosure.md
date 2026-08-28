<!--
name: 'System Reminder: File summary completeness disclosure'
description: >-
  Requires Claude to disclose how much file content was read before summarizing
  and to stop retrying after repeated read failures
ccVersion: 2.1.219
variables:
  - FILE_PATH
  - CHUNK_READING_INSTRUCTIONS
  - ADDITIONAL_READ_GUIDANCE
-->
- You MUST read the content from the file at ${FILE_PATH} in sequential chunks until 100% of the content has been read.
${CHUNK_READING_INSTRUCTIONS}${ADDITIONAL_READ_GUIDANCE}- Before you summarize or analyze content, state what portion of it you read. If you did not read all of it, say so explicitly.
- If a few read attempts fail (file not found, lines too long for Read's offset/limit, no shell access), stop retrying. Summarize what you read, state which portion you were unable to read and why, and proceed.
