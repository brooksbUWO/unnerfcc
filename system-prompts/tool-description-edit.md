<!--
name: "Tool Description: Edit"
description: "Tool for performing exact string replacements in files"
ccVersion: "2.1.235"
variables:
  - "SHOULD_OMIT_READ_BEFORE_EDIT_REQUIREMENT"
  - "MUST_READ_FIRST_FN"
  - "LINE_NUMBER_PREFIX_FORMAT"
  - "EXTRA_EDIT_GUIDANCE"
-->
Performs exact string replacements in files.

Usage:${SHOULD_OMIT_READ_BEFORE_EDIT_REQUIREMENT ? "" : MUST_READ_FIRST_FN()}
- For text from Read tool output, keep the exact indentation (tabs or spaces) after the line number prefix. The line number prefix format is: ${LINE_NUMBER_PREFIX_FORMAT}. Everything after that prefix is the actual file content to match. Never include any part of the line number prefix in the old_string or new_string.
- Prefer a change to an existing file over a new file. Create a new file only for a task that needs one.
- When the user asks for them explicitly, use emojis. Do not add emojis to files, unless the user asks.${EXTRA_EDIT_GUIDANCE}
- Use `replace_all` to replace and rename strings across the file. This parameter helps you rename a variable, for example.
