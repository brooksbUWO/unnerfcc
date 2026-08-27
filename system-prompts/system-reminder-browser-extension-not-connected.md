<!--
name: "System Reminder: Browser extension not connected"
description: "Tells the user how to resolve a disconnected Claude browser extension and where to report bugs"
ccVersion: "2.1.173"
variables:
  - "CHROME_EXTENSION_URL"
  - "BROWSER_EXTENSION_BUG_REPORT_URL"
-->
Browser extension is not connected. Make sure that the Claude browser extension is installed and running (${CHROME_EXTENSION_URL}). Make sure that you are logged into claude.ai with the same account as Claude Code. If this is your first Chrome connection, restart Chrome so the installation takes effect. If issues continue, report a bug: ${BROWSER_EXTENSION_BUG_REPORT_URL}
