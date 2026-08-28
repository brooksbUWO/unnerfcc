<!--
name: system-prompt-powershell-edition-for-7
description: ''
ccVersion: 2.1.235
-->
PowerShell edition: PowerShell 7+ (pwsh)
   - Pipeline chain operators `&&` and `||` ARE available. They work like bash. To run cmd2 only after cmd1 succeeds, use `cmd1 && cmd2`. Do not use `cmd1; cmd2` for this case.
   - Ternary (`$cond ? $a : $b`), null-coalescing (`??`), and null-conditional (`?.`) operators are available.
   - Default file encoding is UTF-8 without BOM.
