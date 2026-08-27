<!--
name: "Skill: Update config description"
description: "Update-config skill description (settings.json hooks, perms, env)"
ccVersion: "2.1.173"
-->
Use this skill to configure the Claude Code harness via `settings.json`. Automated behaviors ("from now on when X", "each time X", "whenever X", "before/after X") require hooks in `settings.json`. The harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions ("allow X", "add permission", "move permission to"), env vars ("set X=Y"). Also hook troubleshooting, or any changes to `settings.json`/`settings.local.json` files. Examples: "allow npm commands", "add bq permission to global settings", "move permission to user settings". Also "set DEBUG=true", "when claude stops show X". For simple items like theme/model, suggest the `/config` command.
