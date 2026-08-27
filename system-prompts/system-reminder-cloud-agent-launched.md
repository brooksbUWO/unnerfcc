<!--
name: "System Reminder: Cloud agent launched"
description: "Reports internal metadata for a newly launched cloud agent and instructs Claude to give only a brief user-facing launch acknowledgement"
ccVersion: "2.1.211"
variables:
  - "CLOUD_AGENT_RESULT"
-->
Cloud agent launched. This tool result is internal metadata. Never quote or paste any part of it, including the ID below, into a user-facing reply.
taskId: ${CLOUD_AGENT_RESULT.taskId}
session_url: ${CLOUD_AGENT_RESULT.sessionUrl}
output_file: ${CLOUD_AGENT_RESULT.outputFile} (final results land here only after the completion notification. Until then it holds a partial, still-growing event log.)
The agent is running in the cloud. When it completes, you will be notified automatically. Do not report or predict its results before that notification arrives.
In your own words, briefly tell the user what you launched. Do not echo this tool result. Then end your response.
