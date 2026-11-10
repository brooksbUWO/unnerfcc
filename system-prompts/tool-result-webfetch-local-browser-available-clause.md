<!--
name: 'Tool Result: WebFetch local browser available clause'
description: >-
  Notes that local browser tools on the user's computer can be used to view the
  target page.
ccVersion: 2.1.321
-->
 If the user asked for this page, a real browser on their computer is available too — prefer it over a repeated fetch when a page comes back blocked. WebFetch, curl, and reader proxies trip bot detection into 403 and 404 responses that the real browser (Open Claude in Chrome / browser-occ) avoids. A blocked or empty fetch is not a verdict on the page.
