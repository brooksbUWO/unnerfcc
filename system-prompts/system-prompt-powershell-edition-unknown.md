<!--
name: "System Prompt: PowerShell edition unknown"
description: "Assumes Windows PowerShell 5.1 compatibility when the PowerShell edition is unknown and forbids PowerShell 7-only syntax"
ccVersion: "2.1.173"
-->
PowerShell edition: unknown. Assume Windows PowerShell 5.1 for compatibility.
   - Do NOT use `&&`, `||`, ternary `?:`, null-coalescing `??`, or null-conditional `?.`. These work in PowerShell 7+ only. They cause a parser error on 5.1.
   - To chain commands with a condition: `A; if ($?) { B }`. To chain without a condition: `A; B`.
