<!--
name: "Tool Description: WebFetch"
description: "Tool description for web fetch functionality"
ccVersion: "2.1.233"
variables:
  - "WEBFETCH_CACHE_TTL_FN"
-->

- Fetches content from a specified URL and processes it with an AI model.
- Takes a URL and a prompt as input.
- Fetches the URL content and converts HTML to markdown.
- Processes the content with the prompt and a small, fast model.
- Returns the response of the model about the content.
- Use this tool to retrieve and analyze web content.

Usage notes:
  - IMPORTANT: If an MCP web fetch tool is available, prefer it over this tool. It can have fewer restrictions.
  - The URL must be a fully-formed valid URL.
  - HTTP URLs are upgraded to HTTPS automatically.
  - The prompt describes what information you want from the page.
  - This tool is read-only. It does not modify any files.
  - Large content can come back summarized.
  - This tool includes a self-cleaning cache for faster responses on the same URL. Entries expire after ${WEBFETCH_CACHE_TTL_FN()}.
  - When a URL redirects to a different host, the tool gives you the redirect URL in a special format. Then make a new WebFetch request with the redirect URL to fetch the content.
  - For GitHub URLs, prefer the gh CLI through Bash (for example, gh pr view, gh issue view, gh api).
