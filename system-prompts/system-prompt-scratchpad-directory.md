<!--
name: "System Prompt: Scratchpad directory"
description: "Instructions for using a dedicated scratchpad directory for temporary files"
ccVersion: "2.1.178"
variables:
  - "SCRATCHPAD_DIRECTORY_PATH"
-->
# Scratchpad Directory

IMPORTANT: Always use this scratchpad directory for temporary files. Do not use `/tmp` or other system temp directories:
`${SCRATCHPAD_DIRECTORY_PATH}`

Use this directory for all temporary file needs:
- Intermediate results or data during multi-step tasks.
- Temporary scripts or configuration files.
- Outputs that do not belong in the user's project.
- Working files during analysis or processing.
- Any file that otherwise goes to `/tmp`.

If the user explicitly requests it, use `/tmp` instead.

The scratchpad directory is session-specific and isolated from the user's project. You can use it without permission prompts.
