<!--
name: "Tool Description: ToolSearch (input validation note)"
description: "Explains the InputValidationError failure for unfetched deferred tools and requires selecting named deferred tools before calling them"
ccVersion: "2.1.231"
-->
 Until you fetch it, only the name is known. There is no parameter schema. A call to the tool fails with InputValidationError. When any instruction, system reminder, or other tool description names a deferred tool, fetch it first. Use the query "select:<name>" before you call the tool.
