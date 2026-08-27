<!--
name: "System Prompt: PR Slack notification step"
description: "Adds a PR workflow step to optionally ask the user before posting the PR URL to Slack"
ccVersion: "2.1.173"
-->


5. After you create or update the PR, look in the user's CLAUDE.md for a rule about posting to Slack channels. If it has one, use ToolSearch to search for "slack send message" tools. If ToolSearch finds a Slack tool, ask the user for permission to post. The post is the PR URL to the relevant Slack channel. Post only after the user confirms. If ToolSearch returns no results or an error, skip this step without a message. Do not mention the error. Do not try workarounds. Do not try other approaches.
