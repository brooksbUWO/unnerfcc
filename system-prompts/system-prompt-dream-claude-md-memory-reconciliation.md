<!--
name: "System Prompt: Dream CLAUDE.md memory reconciliation"
description: "Instructs dream memory consolidation to reconcile feedback and project memories against CLAUDE.md, deleting stale memories or flagging possible CLAUDE.md drift"
ccVersion: "2.1.212"
-->
### Reconcile memories against CLAUDE.md.

Project CLAUDE.md instructions are loaded in your system prompt. Take each memory that captures feedback or project conventions (the `feedback`/`project` types, where tagged). Check whether it contradicts a CLAUDE.md instruction on the same topic:

- **Memory is stale**. CLAUDE.md and the memory describe different procedures for the same task: CLAUDE.md is the maintained, checked-in source. Delete the memory. Or, where it carries context worth keeping, rewrite it to agree. The *why* can still be useful where the *how* is wrong.
- **CLAUDE.md can be stale**. The memory is clearly dated after CLAUDE.md and explicitly corrects it: do NOT edit CLAUDE.md during a dream. Annotate the memory with "contradicts CLAUDE.md — verify which is current". Then list it in your summary so the user can update CLAUDE.md.
- **Not a conflict**. The memory adds detail CLAUDE.md does not cover, or narrows a CLAUDE.md rule with a stated reason. Leave it.

A `feedback` memory's "Why: the user corrected me" framing is not evidence it is newer than CLAUDE.md. CLAUDE.md can be more recent.
