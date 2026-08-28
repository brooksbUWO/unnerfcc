<!--
name: ToolSearch input-validation note
description: ''
ccVersion: 2.1.235
-->
 Until you fetch it, only the name is known. There is no parameter schema. A call to the tool fails with InputValidationError. When any instruction, system reminder, or other tool description names a deferred tool, fetch it first. Use the query "select:<name>" before you call the tool.
