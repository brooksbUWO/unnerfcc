<!--
name: 'Tool Description: Claude in Chrome bridge disconnect error'
description: >-
  Error message shown when a Claude in Chrome tool call fails because the Chrome
  extension disconnects mid-operation
ccVersion: 2.1.178
variables:
  - CHROME_TOOL_NAME
-->
The "${CHROME_TOOL_NAME}" tool call failed. The Open Claude in Chrome (browser-occ) connection dropped during the operation. This is usually transient. A host restart, an extension restart, a closed tab, or a network blip can cause it. The connection often returns on its own. Retry the same tool call after a few seconds. A dropped connection does not mean the browser lane is gone. The entry tools auto-start a down host. Re-read the connection tool and retry. You can also use the TCP bridge shell lane (run_occ_tool.py). Do not fall back to a plain HTTP fetch. If the call keeps failing, relaunch the OCC browser profile (connection ladder Step 3). You can also ask the user to make sure that the extension is loaded and connected.
