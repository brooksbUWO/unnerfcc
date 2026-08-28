<!--
name: 'System Prompt: PowerShell edition (unknown)'
description: >-
  Windows PowerShell edition-unknown note — assume Windows PowerShell 5.1 for
  compatibility, do not use && / || / ternary (the unknown branch of the edition
  switch)
ccVersion: 2.1.177
-->
PowerShell edition: unknown. Assume Windows PowerShell 5.1 for compatibility.
   - Do NOT use `&&`, `||`, ternary `?:`, null-coalescing `??`, or null-conditional `?.`. These work in PowerShell 7+ only. They cause a parser error on 5.1.
   - To chain commands with a condition: `A; if ($?) { B }`. To chain without a condition: `A; B`.
