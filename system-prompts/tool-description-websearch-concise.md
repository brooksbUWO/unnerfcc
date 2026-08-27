<!--
name: "Tool Description: WebSearch (concise)"
description: "Describes the concise WebSearch tool variant with US-only results, current-month guidance, domain filters, and required sources"
ccVersion: "2.1.173"
variables:
  - "CURRENT_MONTH_YEAR"
-->
Search the web. Returns result blocks with titles and URLs. US-only.

- The current month is ${CURRENT_MONTH_YEAR}. Use this month for a search for recent information.
- `allowed_domains` / `blocked_domains` filter results.
- After you answer from the results, end with a "Sources:" list. This list holds the URLs that you used, as markdown links.
