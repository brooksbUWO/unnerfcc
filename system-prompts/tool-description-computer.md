<!--
name: 'Tool Description: Computer'
description: Main description for the Chrome browser computer automation tool
ccVersion: 2.0.71
-->
Use a mouse and keyboard to interact with a web browser, and take screenshots. If you don't have a valid tab ID, use tabs_context_mcp first to get available tabs.
* Before you use a coordinate click, look for a programmatic route. A DOM query with a direct element .click() (through a JavaScript tool, when available) does not depend on pixel positions. A coordinate click fails silently when the layout moves.
* When the page exposes its own runtime state (a page object, a live badge count), read that state instead of scraped positional HTML.
* To get data from the page, prefer a same-origin fetch or a server-side download over a screenshot that a reader must decode.
* When only a coordinate click works: examine a current screenshot first and get the coordinates of the element. Click with the cursor tip in the center of the element, not the edges.
* After each action, make sure that the action had its effect. Assert a concrete post-condition: the new page, a count that increased by the exact quantity, the open dialog. If a click had no effect, adjust the click location so that the cursor tip falls on the element.
* If the route is structurally dead (the control does not exist on the page), stop and report it. Do not retry a dead route.
