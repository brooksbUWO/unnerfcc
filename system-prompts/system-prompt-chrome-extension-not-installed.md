<!--
name: 'System Prompt: Chrome extension not installed'
description: >-
  Injected notice that browser tools are unavailable because the extension is
  not set up, with where the user can install it.
ccVersion: 2.1.219
variables:
  - CHROME_EXTENSION_INSTALL_URL
-->
Browser tools are not available in this session. The Open Claude in Chrome (browser-occ) extension is not set up. The user can install or connect it from ${CHROME_EXTENSION_INSTALL_URL} and manage browser tools with /chrome. Continue the task without browser tools. WebFetch and WebSearch cover read-only web access. If the task needs the browser, tell the user the extension is not set up and give them the install location.
