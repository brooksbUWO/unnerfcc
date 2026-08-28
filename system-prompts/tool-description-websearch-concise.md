<!--
name: 'Tool Description: WebSearch (concise)'
description: >-
  Concise (velvet) WebSearch tool description rendered for Opus 4.8 / Fable 5 /
  Mythos 5 — US-only web search returning titled URL result blocks, with the
  current-month grounding note and the Sources list requirement
ccVersion: 2.1.219
variables:
  - CURRENT_MONTH_YEAR
-->
Search the web. Returns result blocks with titles and URLs. US-only.

- The current month is ${CURRENT_MONTH_YEAR}. Use this month for a search for recent information.
- `allowed_domains` / `blocked_domains` filter results.
- After you answer from the results, end with a "Sources:" list. This list holds the URLs that you used, as markdown links.
