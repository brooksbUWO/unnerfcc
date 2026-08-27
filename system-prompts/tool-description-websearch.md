<!--
name: "Tool Description: WebSearch"
description: "Tool description for web search functionality"
ccVersion: "2.1.120"
variables:
  - "CURRENT_MONTH_YEAR"
-->

- Claude can search the web and use the results in responses.
- Gives up-to-date information for current events and recent data.
- Returns search result information as search result blocks. These blocks include links as markdown hyperlinks.
- Use this tool to get information beyond the knowledge cutoff of Claude.
- Each search runs automatically within a single API call.

After you answer the question of the user, end your response with a "Sources:" section. This section lists the relevant URLs from the search results as markdown hyperlinks. For example:

    [Your answer here]

    Sources:
    - [Source Title 1](https://example.com/1)
    - [Source Title 2](https://example.com/2)

Usage notes:
  - Domain filtering can include or block specific websites.
  - Web search is available only in the US.
  - The current month is ${CURRENT_MONTH_YEAR}. Use this year for a search for recent information, documentation, or current events. For example, for "latest React docs", search "React documentation" with the current year, not a past one.
