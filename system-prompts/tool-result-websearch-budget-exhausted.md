<!--
name: 'Tool Result: Web search budget exhausted'
description: >-
  Tells the model this session has spent its WebSearch budget, to continue from
  information already gathered, and not to route around the limit through
  shells, browsers, computer use, or third-party readers and proxies.
ccVersion: 2.1.321
variables:
  - BUDGET_SCOPE_NOUN
  - SEARCH_USAGE_COUNTS
  - CONTINUE_WITHOUT_SEARCH_GUIDANCE
  - SHELL_TOOL_NAME
  - ADDITIONAL_BUDGET_NOTE
-->
Web search was not performed: this ${BUDGET_SCOPE_NOUN}'s web search budget is used up (${SEARCH_USAGE_COUNTS}). ${CONTINUE_WITHOUT_SEARCH_GUIDANCE}; do not work around the limit by querying search engines with curl or wget from ${SHELL_TOOL_NAME}, by querying them in a browser or through a computer-use tool, or by searching or fetching through a third-party reader, proxy or archive service.${ADDITIONAL_BUDGET_NOTE}
