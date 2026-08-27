<!--
name: "Tool Description: WebFetch private URL warning"
description: "Warns that WebFetch fails for authenticated or private URLs and includes the standard WebFetch usage notes"
ccVersion: "2.1.235"
variables:
  - "IS_ARTIFACT_TOOL_ENABLED"
  - "WEBFETCH_TOOL_DESCRIPTION_BLOCK"
-->
IMPORTANT: WebFetch WILL FAIL for authenticated or private URLs. Before you use this tool, examine the URL. Some URLs point to an authenticated service (for example Google Docs, Confluence, Jira, GitHub). For such a URL, look for a specialized MCP tool that gives authenticated access.
${
  IS_ARTIFACT_TOOL_ENABLED
    ? `- Exception: claude.ai/code/artifact/{uuid} URLs (including preview.claude.ai) ARE fetchable — WebFetch uses your claude.ai login. Use WebFetch for these, not curl or a headless browser (those return the SPA shell or a Cloudflare 403, not the content).
`
    : ""
}${WEBFETCH_TOOL_DESCRIPTION_BLOCK()}
