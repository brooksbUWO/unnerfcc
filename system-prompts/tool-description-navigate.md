<!--
name: "Tool Description: Navigate"
description: "Describes the browser navigate tool for opening URLs and moving forward or backward in tab history"
ccVersion: "2.1.211"
-->
Navigate to a URL, or go forward or back in browser history. You can omit tabId for URL navigation with a STANDALONE navigate call (not inside browser_batch). Then `tabs_context_mcp{createIfEmpty:true}` is called for you. The first tab in the session's group is navigated. Its result is appended to this call's output, so you get the tab list and ids for later calls. Inside browser_batch, navigate needs an explicit tabId. Other tools that act on a page also need an explicit tabId. Pass an explicit tabId for a specific tab. If the session's group has multiple tabs whose state you must preserve, pass an explicit tabId. tabId is required for `url:"back"` and `url:"forward"`.
