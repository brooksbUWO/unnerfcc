<!--
name: "System Reminder: Async agent launched metadata"
description: "Reports internal metadata for a newly launched asynchronous agent and warns Claude not to expose its ID or predict its results"
ccVersion: "2.1.211"
variables:
  - "ASYNC_AGENT_RESULT"
-->
Async agent launched successfully. This tool result is internal metadata. Never quote or paste any part of it, including the agentId below, into a user-facing reply.
agentId: ${ASYNC_AGENT_RESULT.agentId} (internal ID - do not mention to user. Use SendMessage with to: '${ASYNC_AGENT_RESULT.agentId}', summary: '<5-10 word recap>' to continue this agent.)
The agent is working in the background. When it completes, you will be notified automatically. You know nothing about its results until that notification arrives. Do not report, assume, or predict them. In the meantime, continue other work or respond to the user.
