<!--
name: 'Tool Description: Claude in Chrome read page'
description: >-
  Describes the Claude in Chrome read_page tool for retrieving an accessibility
  tree of page elements
ccVersion: 2.1.217
-->
Get an accessibility tree of the elements on the page. By default the tool returns all elements, including non-visible ones. The output is limited to 50000 characters by default. If the output is more than this limit, the tool truncates it at a line boundary. A note gives the full size. To get more, pass a larger max_chars value. You can also use depth or ref_id to focus on part of the page. You can filter for interactive elements only. If you do not have a valid tab ID, call the browser-occ connection tool first. It gives the available tabs.
