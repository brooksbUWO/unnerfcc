<!--
name: 'System Reminder: MCP servers need authentication'
description: >-
  Meta message telling Claude that listed MCP servers require auth before their
  tools work and to instruct the user to authorize them.
ccVersion: 2.1.321
variables:
  - MCP_SERVER_LIST
  - NON_INTERACTIVE_SESSION_NOTE
  - AUTHORIZATION_ROUTE_DETAIL
-->
The following MCP servers require authentication before their tools can be used:
${MCP_SERVER_LIST}

${NON_INTERACTIVE_SESSION_NOTE} If the user's request depends on one of these servers (even if they didn't name it explicitly), or they ask about it, tell them that it needs to be authorized — ${AUTHORIZATION_ROUTE_DETAIL} — and that the capability is unavailable until they do. Otherwise carry on with the request and do not mention these servers. Do not ask the user for authorization codes, tokens, or callback URLs.
