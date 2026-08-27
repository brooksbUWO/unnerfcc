<!--
name: "Tool Description: ToolSearch (second part)"
description: "Explains how queries match deferred tools and load their complete JSON Schema definitions for subsequent calls"
ccVersion: "2.1.178"
-->
 This tool takes a query and matches it against the deferred tool list. It returns the complete JSONSchema definitions of the matched tools inside a <functions> block. After the schema of a tool appears in that result, you can call the tool. It works like any tool at the top of the prompt.

Result format: each matched tool appears as one <function>{"description": "...", "name": "...", "parameters": {...}}</function> line inside the <functions> block. This is the same encoding as the tool list at the top of this prompt.

Query forms:
- "select:Read,Edit,Grep" fetches these exact tools by name.
- "notebook jupyter" is a keyword search, up to max_results best matches.
- "+slack send" requires "slack" in the name and ranks by the remaining terms.
