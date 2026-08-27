<!--
name: "Tool Description: WebFetch (concise)"
description: "Concise tool description for WebFetch covering URL fetching, private URL limitations, redirects, and caching"
ccVersion: "2.1.235"
variables:
  - "IS_ARTIFACT_TOOL_ENABLED"
  - "WEBFETCH_CACHE_TTL_FN"
-->
Fetches a URL, converts the page to markdown, and answers `prompt` against it with a small fast model.

- This tool fails on authenticated or private URLs. For those, use an authenticated MCP tool or `gh` instead.${IS_ARTIFACT_TOOL_ENABLED ? " Exception: claude.ai/code/artifact/{uuid} URLs ARE fetchable via your claude.ai login — use WebFetch, not curl (curl gets the SPA shell or a Cloudflare 403)." : ""}
- HTTP is upgraded to HTTPS. This tool returns a cross-host redirect to you and does not follow it. Call the tool again with the redirect URL.
- Responses are cached for ${WEBFETCH_CACHE_TTL_FN()} per URL.
