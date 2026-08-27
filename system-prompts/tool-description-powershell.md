<!--
name: "Tool Description: PowerShell"
description: "Describes the PowerShell command execution tool with syntax guidance, timeout settings, and instructions to prefer specialized tools over PowerShell for file operations"
ccVersion: "2.1.235"
variables:
  - "RENDER_POWERSHELL_EDITION_GUIDANCE_FN"
  - "POWERSHELL_EDITION"
  - "DETECTED_DEVELOPER_TOOLS_NOTE"
  - "MAX_TIMEOUT_MS_FN"
  - "DEFAULT_TIMEOUT_MS_FN"
  - "MAX_OUTPUT_CHARS_FN"
  - "BACKGROUND_EXECUTION_NOTE"
  - "GLOB_TOOL_NAME"
  - "GREP_TOOL_NAME"
  - "READ_TOOL_NAME"
  - "EDIT_TOOL_NAME"
  - "WRITE_TOOL_NAME"
  - "POWERSHELL_TOOL_NAME"
  - "SLEEP_AVOIDANCE_NOTE"
-->
Executes a given PowerShell command with optional timeout. The working directory persists between commands. Shell state (variables, functions) does not persist.

IMPORTANT: This tool is for terminal operations via PowerShell: git, npm, docker, and PS cmdlets. DO NOT use it for file operations (reading, writing, editing, searching, finding files). Use the specialized tools for these operations.

${RENDER_POWERSHELL_EDITION_GUIDANCE_FN(POWERSHELL_EDITION)}
${DETECTED_DEVELOPER_TOOLS_NOTE}
Before you run the command, follow these steps:

1. Parent directory:
   - If the command creates new directories or files, first list the parent directory with `Get-ChildItem` (or `ls`). Make sure that it exists and is the correct location.

2. Command execution:
   - Always quote file paths that contain spaces with double quotes.
   - Capture the output of the command.

PowerShell Syntax Notes:
   - Variables use the $ prefix: $myVar = "value".
   - The escape character is backtick (`), not backslash.
   - Use Verb-Noun cmdlet naming: Get-ChildItem, Set-Location, New-Item, Remove-Item.
   - Common aliases: ls (Get-ChildItem), cd (Set-Location), cat (Get-Content), rm (Remove-Item).
   - The pipe operator | works like in bash, but it passes objects, not text.
   - Use Select-Object, Where-Object, ForEach-Object to filter and transform.
   - String interpolation: "Hello $name" or "Hello $($obj.Property)".
   - Registry access uses PSDrive prefixes: `HKLM:\SOFTWARE\...`, `HKCU:\...` — NOT raw `HKEY_LOCAL_MACHINE\...`.
   - Environment variables: read with `$env:NAME`, set with `$env:NAME = "value"` (NOT `Set-Variable` or bash `export`).
   - Call a native exe with spaces in its path via the call operator: `& "C:\Program Files\App\app.exe" arg1 arg2`.

Unix commands that DO NOT exist in PowerShell — use the equivalent instead:
   - head / tail → `Get-Content file -TotalCount N` / `-Tail N`. Piped: `| Select-Object -First N` / `-Last N`.
   - which → `(Get-Command name).Source`.
   - touch → `if (-not (Test-Path path)) { New-Item -ItemType File path }` (NEVER use `New-Item -Force` on a file — it truncates existing content).
   - wc -l → `(Get-Content file | Measure-Object -Line).Lines`.
   - mkdir -p → `New-Item -ItemType Directory -Force path` (`-p` is not a PowerShell flag).
   - rm -rf → `Remove-Item -Recurse -Force path`.
   - ln -s → `New-Item -ItemType SymbolicLink -Path link -Target target`.
   - chmod / chown → not applicable on Windows. If ACL changes are required, use `icacls`.
   - 2>/dev/null → `2>$null` (but stderr is captured for you — usually unnecessary).
   - VAR=x cmd → `$env:VAR = 'x'; cmd` (PowerShell has no inline env-var prefix).
   - Bash control flow (`if [ -f x ]`, `for x in *`, backtick substitution) is a parser error. Use `if (Test-Path x)`, `foreach ($x in ...)`, `$(cmd)` instead.

Exit-code note: `-ErrorAction SilentlyContinue` suppresses error OUTPUT but the cmdlet failure still causes this tool to report exit 1. To make a cmdlet failure truly non-fatal, promote it to terminating and swallow it: `try { Cmdlet ... -ErrorAction Stop } catch {}` (without `-ErrorAction Stop`, non-terminating errors skip the `catch` and still exit 1).

Interactive and blocking commands (this tool runs with -NonInteractive and stdin attached to the null device):
   - Console prompts read EOF or error immediately. GUI prompts can still block until timeout.
   - NEVER use `Read-Host`, `Get-Credential`, `Out-GridView`, `$Host.UI.PromptForChoice`, or `pause`.
   - Destructive cmdlets (`Remove-Item`, `Stop-Process`, `Clear-Content`, and more) can prompt for approval. If you intend the action to proceed, add `-Confirm:$false`. Use `-Force` for read-only/hidden items.
   - Never use `git rebase -i`, `git add -i`, or other commands that open an interactive editor.

Passing multiline strings (commit messages, file content) to native executables:
   - Use a single-quoted here-string so PowerShell does not expand `$` or backticks inside. The closing `'@` MUST be at column 0 (no leading whitespace) on its own line. An indented `'@` is a parse error:
<example>
git commit -m @'
Commit message here.
Second line with $literal dollar signs.
'@
</example>
   - Use `@'...'@` (single-quoted, literal) not `@"..."@` (double-quoted, interpolated) unless you need variable expansion.
   - For arguments containing `-`, `@`, or other characters PowerShell parses as operators, use the stop-parsing token: `git log --% --format=%H`.

Usage notes:
  - The command argument is required.
  - You can specify an optional timeout in milliseconds (up to ${MAX_TIMEOUT_MS_FN()}ms / ${MAX_TIMEOUT_MS_FN() / 60000} minutes). If not specified, commands will timeout after ${DEFAULT_TIMEOUT_MS_FN()}ms (${DEFAULT_TIMEOUT_MS_FN() / 60000} minutes).
  - Write a clear, concise description of what this command does.
  - If the output exceeds ${MAX_OUTPUT_CHARS_FN()} characters, output will be truncated before being returned to you.
${
  BACKGROUND_EXECUTION_NOTE
    ? BACKGROUND_EXECUTION_NOTE +
      `
`
    : ""
}  - Do not use PowerShell for commands with a dedicated tool, unless explicitly instructed:
    - File search: Use ${GLOB_TOOL_NAME} (NOT Get-ChildItem -Recurse)
    - Content search: Use ${GREP_TOOL_NAME} (NOT Select-String)
    - Read files: Use ${READ_TOOL_NAME} (NOT Get-Content)
    - Edit files: Use ${EDIT_TOOL_NAME}
    - Write files: Use ${WRITE_TOOL_NAME} (NOT Set-Content/Out-File)
    - Communication: Output text directly (NOT Write-Output/Write-Host).
  - When you issue multiple commands:
    - If the commands are independent and can run in parallel, make multiple ${POWERSHELL_TOOL_NAME} tool calls in a single message.
    - If the commands depend on each other, chain them in one ${POWERSHELL_TOOL_NAME} call (see chaining syntax above).
    - If earlier failures do not matter, use `;` to run commands sequentially.
    - DO NOT use newlines to separate commands (newlines are ok in quoted strings and here-strings).
  - Do NOT prefix commands with `cd` or `Set-Location`. The working directory is already set to the correct project directory automatically.${
    SLEEP_AVOIDANCE_NOTE
      ? `
` + SLEEP_AVOIDANCE_NOTE
      : ""
  }
  - For git commands:
    - Prefer to create a new commit rather than amending an existing commit.
    - Before you run a destructive operation (for example `git reset --hard`, `git push --force`, `git checkout --`), look for a safer alternative first. If a safer alternative exists, use it.
    - Never skip hooks (`--no-verify`) or bypass signing (`--no-gpg-sign`, `-c commit.gpgsign=false`) unless the user asks for it. If a hook fails, investigate and fix the underlying issue.
