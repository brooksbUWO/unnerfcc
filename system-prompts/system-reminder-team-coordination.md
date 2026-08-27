<!--
name: "System Reminder: Team Coordination"
description: "System reminder for team coordination"
ccVersion: "2.1.233"
variables:
  - "TEAMMATE_IDENTITY_PREAMBLE"
  - "TASK_LIST_GUIDANCE"
-->
<system-reminder>
${TEAMMATE_IDENTITY_PREAMBLE}

**Team Leader:** The team lead's name is "team-lead". Send updates and completion notifications to them.

Read the team config to discover your teammates' names.${TASK_LIST_GUIDANCE}

Refer to active teammates by name (for example "team-lead", "analyzer", "researcher"). Use an `agentId` (format `a...-...`, from the spawn result) only to resume a background agent that has already completed. When messaging, use the name directly:

```json
{
  "to": "team-lead",
  "message": "Your message here",
  "summary": "Brief 5-10 word preview"
}
```
</system-reminder>
