<!--
name: 'Tool Parameter: Record the conversation system prompt'
description: >-
  Describes the flag that records the conversation's system prompt once and
  replays it verbatim on later requests and resumes, and what omitting, true,
  and false each do to appended prompt text and mid-session model or agent
  switches.
ccVersion: 2.1.257
-->
Record the conversation's system prompt once and reuse it verbatim on every later request and resume (recommended: true). Omitted: setting systemPrompt or appendSystemPrompt turns recording off so the appended text applies fresh each launch; only the bare claude_code preset is recorded. true: an existing record in the conversation is sent as-is (a later launch's different systemPrompt/appendSystemPrompt is ignored until compaction); otherwise the prompt is rendered with appendSystemPrompt included, sent, and recorded. false: never record. With a record, a mid-session model switch or set_settings agent/system-prompt change does not alter the prompt until compaction or a new session.
