<!--
name: "Tool Description: Invoke skill"
description: "Tool description for invoking available skills, including skill name selection, optional arguments, scoped skill names, and avoiding duplicate invocation when a skill is already loaded"
ccVersion: "2.1.218"
variables:
  - "SKILL_TAG_NAME"
-->
Invoke a skill.

A skill is a packaged set of instructions that the user or project set up for a kind of task. Examples are deploy steps, a review checklist, and a repo-specific workflow. Available skills appear in a system-reminder listing with one-line descriptions. When a listed skill covers the task, call this tool first. The instructions of the skill load into the turn. Follow them in place of your default approach. Some skills instead run in a subagent and return the finished result. A skill that runs in the background returns only the name of the agent. Its result arrives later as a task notification. Do not wait on it or call it again in the meantime. The user can also ask for a skill by name (`/<name>`, or "slash command"). This request is a request to invoke it.

- `skill`: exact name from the listing, no leading slash. Plugin skills use `plugin:skill`. Directory-scoped skills are listed with a path prefix (`apps/web:deploy`). A name can have both scoped and unscoped variants. In that case, pick the variant whose directory holds the files that you work on. The most specific one wins, else the unscoped one.
- `args`: optional arguments to pass through.

Only names from the listing are valid. A name that the user typed explicitly is also valid. Built-in CLI commands (`/help`, `/clear`, …) are not skills. If a `<${SKILL_TAG_NAME}>` block is present this turn, the skill is loaded. Follow it directly. Do not call the skill again.
