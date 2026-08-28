<!--
name: 'Tool Description: WebFetch (concise)'
description: >-
  Concise WebFetch tool description — fetches a URL, converts the page to
  markdown, and answers a prompt against it, failing on authenticated URLs.
ccVersion: 2.1.219
-->
Fetches a URL, converts the page to markdown, and answers `prompt` against it using a small fast model.

- Fails on authenticated or private URLs — use an authenticated MCP tool or `gh` for those instead.
- On the first blocked fetch (a bot wall, a 403), go to a real browser tool if one is available. A block is not a verdict on the page.
