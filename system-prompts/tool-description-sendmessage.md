<!--
name: "Tool Description: SendMessage"
description: "Describes the SendMessage tool for communicating with other agents and handling legacy team protocol responses"
ccVersion: "2.1.235"
variables:
  - "CROSS_SESSION_RECIPIENT_TABLE_ROWS"
  - "CROSS_SESSION_GUIDANCE_BLOCK"
  - "SHOULD_INCLUDE_LEGACY_PROTOCOL_RESPONSES"
-->

# SendMessage.

Send a message to another agent.

```json
{"to": "researcher", "summary": "assign task 1", "message": "start on task #1"}
```

| `to` | |
|---|---|
| `"researcher"` | Teammate by name |
| `"main"` | The main conversation (background subagents only) |${CROSS_SESSION_RECIPIENT_TABLE_ROWS}${""}

Your plain text output is NOT visible to other agents. To communicate, you MUST call this tool. Messages from teammates are delivered automatically. You do not check an inbox. Refer to agents by name. Names keep working after an agent completes (a send resumes it from its transcript). Use the raw `agentId` (format `a...-...`) from its spawn result only where the agent has no name. Or use it where a newer agent took the name (latest wins). When relaying, do not quote the original. It is already rendered to the user.${CROSS_SESSION_GUIDANCE_BLOCK}${SHOULD_INCLUDE_LEGACY_PROTOCOL_RESPONSES ? '\n\n## Protocol responses (legacy)\n\nIf you receive a JSON message with `type: "shutdown_request"` or `type: "plan_approval_request"`, respond with the matching `_response` type. Echo the `request_id`, set `approve` true/false:\n\n```json\n{"to": "team-lead", "message": {"type": "shutdown_response", "request_id": "...", "approve": true}}\n{"to": "researcher", "message": {"type": "plan_approval_response", "request_id": "...", "approve": false, "feedback": "add error handling"}}\n```\n\nApproving shutdown terminates your process. Rejecting plan sends the teammate back to revise. Do not originate `shutdown_request` unless asked. Do not send structured JSON status messages. Report progress through your task tools where you have them, otherwise in plain prose.' : ""}
