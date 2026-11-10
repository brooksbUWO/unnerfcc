<!--
name: 'Agent Prompt: Conversation summary no-tools reminder'
description: >-
  Closing reminder that the summarizer must answer in plain text of the required
  shape, because tool calls are rejected and fail the task.
ccVersion: 2.1.321
variables:
  - REQUIRED_OUTPUT_SHAPE
-->


REMINDER: Do NOT call any tools. Respond with plain text only — ${REQUIRED_OUTPUT_SHAPE}. Tool calls will be rejected and you will fail the task.
