<!--
name: "Tool Description: Claude in Chrome bridge timeout error"
description: "Error message shown when a Claude in Chrome tool does not respond before timing out"
ccVersion: "2.1.173"
variables:
  - "CHROME_TOOL_NAME"
-->
The "${CHROME_TOOL_NAME}" tool did not respond in time. The Open Claude in Chrome (browser-occ) host is connected, but the page can be slow. The page can be loading or unresponsive, or it can wait on a permission prompt. Try a lighter operation, for example "get_page_text" instead of a screenshot. You can also ask the user to check the page and any pending prompts.
