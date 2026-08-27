<!--
name: "System Reminder: Read truncation retry guidance"
description: "Instructs Claude to reduce chunk size after file-read truncation warnings and notes the Bash output character limit"
ccVersion: "2.1.173"
variables:
  - "MAX_OUTPUT_CHARS"
-->
- If a file read reports truncation ("[N lines truncated]"), reduce the chunk size and re-read. Continue until you read 100% of the content without truncation. Finish the full read before you proceed. This applies while the reads keep succeeding. If instead the reads are hard-failing, the completeness-disclosure guidance takes precedence. Hard failures include: file not found, lines too long for the offset/limit, no shell access. Then stop retrying, disclose the portion you were unable to read, and proceed. Bash output is limited to ${MAX_OUTPUT_CHARS.toLocaleString()} chars.
