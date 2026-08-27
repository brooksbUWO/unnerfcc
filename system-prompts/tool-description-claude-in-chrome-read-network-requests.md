<!--
name: "Tool Description: Claude in Chrome read network requests"
description: "Describes the Claude in Chrome read_network_requests tool for inspecting HTTP requests made by the current page"
ccVersion: "2.1.173"
-->
Read HTTP network requests from a specific tab. This includes XHR, Fetch, documents, and images. The tool helps you debug API calls, monitor network activity, and understand the requests of a page. It returns all requests made by the current page, including cross-origin requests. The tool clears the requests after the page navigates to a different domain. If you do not have a valid tab ID, call the browser-occ connection tool first. It gives the available tabs.
