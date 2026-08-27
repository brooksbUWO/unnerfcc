<!--
name: "Tool Description: BrowserBatch"
description: "Tool description for BrowserBatch, which executes multiple browser tool calls sequentially in one round trip"
ccVersion: "2.1.120"
-->
Execute a sequence of browser tool calls in ONE round trip. Each item is {name, input}. The input is exactly what you pass to that tool standalone. Actions execute SEQUENTIALLY (not in parallel) and stop on the first error. When you can predict two or more steps ahead, use this tool to execute work fast. For example: navigate, click a field, type, press Return, screenshot. Each tool runs its own permission check per item. If an action navigates to a domain without permission, the next item's check fails and the batch stops. Screenshots and other images are returned between the outputs. Coordinates you write in THIS batch refer to the screenshot taken BEFORE this call. browser_batch cannot be nested.
