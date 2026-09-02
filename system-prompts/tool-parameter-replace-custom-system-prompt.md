<!--
name: 'Tool Parameter: Replace the custom system prompt'
description: >-
  Internal field that replaces the custom system prompt from the next turn on —
  applied only when the model request is accepted, required non-empty with no
  revert-to-built-in form, outranked by the per-turn environment read, and
  silently acked by transports that do not implement it.
ccVersion: 2.1.257
-->
@internal Replaces the custom system prompt (the --system-prompt / initialize systemPrompt slot) from the next turn on. Applied only when the model request is accepted; must be non-empty (there is no revert-to-built-in form); re-send the current model for a prompt-only update. The CLAUDE_CODE_SYSTEM_PROMPT_GB_FEATURE per-turn read, where configured, still wins. Transports that do not implement it, and older builds, ack success without applying it.
