<!--
name: "Tool Parameter: Claude in Chrome JavaScript code"
description: "Describes the JavaScript code parameter for the Claude in Chrome JavaScript execution tool"
ccVersion: "2.1.173"
-->
The JavaScript code to run in the current page through Open Claude in Chrome (browser-occ). The code runs in the page context with REPL semantics. Top-level `await` works. The tool returns the result of the last expression automatically. Write the expression you want (for example, `window.myData.value`, or `await fetch(url).then(r=>r.json())`), not `return ...`. You can read and change the DOM, call page functions, and use page variables.
