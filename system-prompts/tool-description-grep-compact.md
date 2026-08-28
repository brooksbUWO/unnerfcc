<!--
name: Grep tool description (compact)
description: ''
ccVersion: 2.1.235
variables:
  - GREP_TOOL_NAME
-->
Content search built on ripgrep. Use this tool instead of `grep`/`rg` through ${GREP_TOOL_NAME}. The results integrate with the permission UI and file links.

- Full regex syntax (for example "log.*Error", "function\s+\w+"). This is ripgrep, not grep. Escape literal braces (`interface\{\}`).
- Filter with `glob` (for example "**/*.tsx") or `type` (for example "js", "py", "rust").
- `output_mode`: "content" (matching lines), "files_with_matches" (paths only, default), or "count".
- `multiline: true` for patterns that span lines.
