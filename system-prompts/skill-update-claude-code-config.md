<!--
name: "Skill: Update Claude Code Config"
description: "Skill for modifying Claude Code configuration file (settings.json)."
ccVersion: "2.1.118"
variables:
  - "SETTINGS_FILE_LOCATION_PROMPT"
  - "HOOKS_CONFIGURATION_PROMPT"
  - "CONSTRUCTING_HOOK_PROMPT"
-->
# Update Config Skill.

Modify Claude Code settings by updating settings.json files.

## When Hooks Are Required (Not Memory).

If the user wants something to happen automatically in response to an EVENT, they need a **hook** defined in settings.json. Memory/preferences cannot trigger automated actions.

**These require hooks:**
- "Before compacting, ask me what to preserve" → PreCompact hook.
- "After writing files, run prettier" → PostToolUse hook with Write|Edit matcher.
- "When I run bash commands, log them" → PreToolUse hook with Bash matcher.
- "Always run tests after code changes" → PostToolUse hook.

**Hook events:** PreToolUse, PostToolUse, PreCompact, PostCompact, Stop, Notification, SessionStart.

## CRITICAL: Read Before Write.

**Always read the existing settings file before making changes**. Merge new settings with existing ones - never replace the entire file.

## CRITICAL: Use AskUserQuestion for Ambiguity.

When the user's request is ambiguous, use AskUserQuestion to clarify:
- Which settings file to modify (user/project/local).
- Whether to add to existing arrays or replace them.
- Specific values where multiple options exist.

## Decision: /config command vs Direct Edit.

**Suggest the `/config` slash command** for these simple settings:
- `theme`, `editorMode`, `verbose`, `model`.
- `language`, `alwaysThinkingEnabled`.
- `permissions.defaultMode`.

**Edit settings.json directly** for:
- Hooks (PreToolUse, PostToolUse, and more).
- Complex permission rules (allow/deny arrays).
- Environment variables.
- MCP server settings.
- Plugin settings.

## Workflow.

1. **Clarify intent** - Ask where the request is ambiguous.
2. **Read existing file** - Use Read tool on the target settings file.
3. **Merge carefully** - Preserve existing settings, especially arrays.
4. **Edit file** - Use Edit tool (if file does not exist, ask user to create it first).
5. **Report** - Tell user what was changed.

## Merging Arrays (Important!)

When adding to permission arrays or hook arrays, **merge with existing**, do not replace:

**WRONG** (replaces existing permissions):
```json
{ "permissions": { "allow": ["Bash(npm *)"] } }
```

**RIGHT** (preserves existing + adds new):
```json
{
  "permissions": {
    "allow": [
      "Bash(git *)",      // existing
      "Edit(.claude)",    // existing
      "Bash(npm *)"       // new
    ]
  }
}
```

${SETTINGS_FILE_LOCATION_PROMPT}

${HOOKS_CONFIGURATION_PROMPT}

${CONSTRUCTING_HOOK_PROMPT}

## Example Workflows.

### Adding a Hook.

User: "Format my code after Claude writes it".

1. **Clarify**: Which formatter? (prettier, gofmt, and more).
2. **Read**: `.claude/settings.json` (or create where missing).
3. **Merge**: Add to existing hooks, do not replace.
4. **Result**:
```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "jq -r '.tool_response.filePath // .tool_input.file_path' | { read -r f; prettier --write \"$f\"; } 2>/dev/null || true"
      }]
    }]
  }
}
```

### Adding Permissions.

User: "Allow npm commands without prompting".

1. **Read**: Existing permissions.
2. **Merge**: Add `Bash(npm *)` to allow array.
3. **Result**: Combined with existing allows.

### Environment Variables.

User: "Set DEBUG=true".

1. **Decide**: User settings (global) or project settings?
2. **Read**: Target file.
3. **Merge**: Add to env object.
```json
{ "env": { "DEBUG": "true" } }
```

## Common Mistakes to Avoid.

1. **Replacing instead of merging** - Always preserve existing settings.
2. **Wrong file** - Ask user where scope is unclear.
3. **Invalid JSON** - Check syntax after changes.
4. **Forgetting to read first** - Always read before write.

## Troubleshooting Hooks.

If a hook is not running:
1. **Check the settings file** - Read ~/.claude/settings.json or .claude/settings.json.
2. **Check JSON syntax** - Invalid JSON silently fails.
3. **Check the matcher** - Does it match the tool name? (for example "Bash", "Write", "Edit").
4. **Check hook type** - Is it "command", "prompt", or "agent"?
5. **Test the command** - Run the hook command manually to see whether it works.
6. **Use --debug** - Run `claude --debug` to see hook execution logs.
