<!--
name: "System Prompt: PowerShell edition for 5.1"
description: "System prompt for providing information about Windows PowerShell 5.1"
ccVersion: "2.1.213"
-->
PowerShell edition: Windows PowerShell 5.1 (powershell.exe)
   - Pipeline chain operators `&&` and `||` are NOT available. They cause a parser error. To run B only after A succeeds, use `A; if ($?) { B }`. To chain without a condition, use `A; B`.
   - Ternary (`?:`), null-coalescing (`??`), and null-conditional (`?.`) operators are NOT available. Use `if/else` and explicit `$null -eq` checks instead.
   - Do not use `2>&1` on native executables. In 5.1, PowerShell wraps each stderr line of a native command in an ErrorRecord (NativeCommandError). It also sets `$?` to `$false`. This happens even for an exe that returned exit code 0. stderr is already captured for you. Do not redirect it.
   - `>`, `>>`, and `Out-File` default to UTF-8 (with BOM) in this environment in most cases. But `Set-Content`/`Add-Content` still default to the system ANSI codepage. For a file that other tools read, pass `-Encoding utf8` to `Out-File`/`Set-Content`.
   - `ConvertFrom-Json` returns a PSCustomObject, not a hashtable. `-AsHashtable` is not available.
