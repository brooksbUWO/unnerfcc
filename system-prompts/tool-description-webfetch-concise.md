<!--
name: 'Tool Description: WebFetch (concise)'
description: >-
  Concise WebFetch description — fetches a URL, converts it to markdown, answers
  the prompt against it with a small fast model, and fails on authenticated or
  private URLs.
ccVersion: 2.1.321
variables:
  - TOOL_HEADER
-->
${TOOL_HEADER}Fetches a URL, converts the page to markdown, and answers `prompt` against it using a small fast model.

- Fails on authenticated or private URLs — use an authenticated MCP tool or `gh` for those instead.
- On the first blocked fetch (a bot wall, a 403), go to a real browser tool if one is available. A block is not a verdict on the page.
