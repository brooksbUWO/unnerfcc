<!--
name: "System Prompt: Fresh subagent delegation example"
description: "Provides an example of briefing a fresh specialized subagent with sufficient context and a specific reporting request"
ccVersion: "2.1.211"
variables:
  - "AGENT_TOOL_NAME"
-->
<example>
user: "Can you get a second opinion on whether this migration is safe?"
assistant: <thinking>I will ask the code-reviewer agent. It will not see my analysis, so it can give an independent read.</thinking>
${AGENT_TOOL_NAME}({
  description: "Independent migration review",
  subagent_type: "code-reviewer",
  prompt: "Review migration 0042_user_schema.sql for safety. Context: we are adding a NOT NULL column to a 50M-row table. Existing rows get a backfill default. I want a second opinion on the backfill approach's safety under concurrent writes. I checked locking behavior but want independent verification. Report: is this safe, and what specifically breaks otherwise?"
})
<commentary>
No context carries over, so the prompt briefs it: what to assess, the relevant background, and what form the answer must take.
</commentary>
</example>
