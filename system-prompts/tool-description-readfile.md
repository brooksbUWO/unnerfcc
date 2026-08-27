<!--
name: "Tool Description: ReadFile"
description: "Tool description for reading files"
ccVersion: "2.1.235"

variables:
  - "DEFAULT_READ_LINE_LIMIT"
  - "OFFSET_LIMIT_NOTE"
  - "LINE_TRUNCATION_NOTE"
  - "EXTRA_USAGE_NOTES"
-->
Reads a file from the local filesystem. You can access any file directly with this tool.
Assume that this tool can read all files on the machine. If the user gives a path to a file, assume that the path is valid. A read of a file that does not exist is okay. The tool returns an error.

Usage:
- The file_path parameter must be an absolute path, not a relative path
- By default, it reads up to ${DEFAULT_READ_LINE_LIMIT} lines from the start of the file${OFFSET_LIMIT_NOTE}
${LINE_TRUNCATION_NOTE}
${EXTRA_USAGE_NOTES}
- This tool reads images (for example PNG or JPG). It presents the contents of an image file visually, because Claude Code is a multimodal LLM.
