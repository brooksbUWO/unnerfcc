<!--
name: 'Tool Description: Remote devices computer use instructions'
description: >-
  Instructions for using the computer-use tools without an enable step — load
  them in one ToolSearch call, try the request with them, and what to tell the
  user when calls do not respond or the tools are absent.
ccVersion: 2.1.321
variables:
  - COMPUTER_TOOL_PREFIX
  - DEFERRED_TOOLS_CLAUSE
  - TOOLSEARCH_QUERY
-->
The computer-use tools are the ${COMPUTER_TOOL_PREFIX} tools; there is no separate enable step. ${DEFERRED_TOOLS_CLAUSE}: load them all in one ${TOOLSEARCH_QUERY} call (query "${COMPUTER_TOOL_PREFIX}", max_results 100), and use them once that result has come back, not in the same reply. Try the user's request with them, asking for access to the applications you need first, the way those tools describe. Don't tell the user their computer is connected until a call to one of them has succeeded; if calls keep not responding, the Claude app on the user's computer isn't answering: it may be closed or the computer asleep. Tell the user that, ask them to open the Claude app on that computer, and carry on with what you can do here. If you have no such tools here, tell the user that computer use isn't available on their computer right now and that the Claude app on that computer may show why in the Computer use section of its Settings, then continue with what you can do here. Don't say a permission was denied unless a result says so.
