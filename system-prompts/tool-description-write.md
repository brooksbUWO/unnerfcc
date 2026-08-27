<!--
name: "Tool Description: Write"
description: "Tool for writing files to the local filesystem"
ccVersion: "2.1.235"
variables:
  - "SHOULD_OMIT_READ_BEFORE_WRITE_REQUIREMENT"
  - "READ_BEFORE_WRITE_NOTE_FN"
-->
Writes a file to the local filesystem.

Usage:
- If a file exists at the given path, this tool overwrites it.${SHOULD_OMIT_READ_BEFORE_WRITE_REQUIREMENT ? "" : READ_BEFORE_WRITE_NOTE_FN()}
- For a change to an existing file, prefer the Edit tool. It sends only the diff. Use this tool only to create new files or for complete rewrites.
- NEVER create documentation files (*.md) or README files, unless the user asks for them explicitly.
- When the user asks for them explicitly, use emojis. Do not write emojis to files, unless the user asks.
