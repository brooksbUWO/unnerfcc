<!--
name: "Tool Description: Grep"
description: "Tool description for content search using ripgrep"
ccVersion: "2.1.235"
variables:
  - "GREP_TOOL_NAME"
  - "BASH_TOOL_NAME"
  - "SUBAGENT_STEERING_MODE_FN"
  - "AGENT_TOOL_NAME"
-->
A search tool built on ripgrep.

  Usage:
  - For search tasks, prefer ${GREP_TOOL_NAME} over `grep` or `rg` as a ${BASH_TOOL_NAME} command. The ${GREP_TOOL_NAME} tool is optimized for correct permissions and access.
  - Supports full regex syntax (for example, "log.*Error", "function\s+\w+").
  - Filter files with glob parameter (for example, "*.js", "**/*.tsx") or type parameter (for example, "js", "py", "rust").
  - Output modes: "content" shows matching lines. "files_with_matches" shows only file paths (default). "count" shows match counts.
${
  SUBAGENT_STEERING_MODE_FN() === "default"
    ? `  - Use ${AGENT_TOOL_NAME} tool (if available) for open-ended searches requiring multiple rounds
`
    : ""
}  - Pattern syntax: this tool uses ripgrep, not grep. Escape literal braces (use `interface\{\}` to find `interface{}` in Go code).
  - Multiline matching: by default, patterns match within single lines only. For cross-line patterns like `struct \{[\s\S]*?field`, use `multiline: true`.
