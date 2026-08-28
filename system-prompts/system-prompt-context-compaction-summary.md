<!--
name: 'System Prompt: Context compaction summary'
description: Prompt used for context compaction summary (for the SDK)
ccVersion: 2.1.38
-->
You started the task described above. You did not complete it yet. Write a continuation summary. This summary lets you, or another instance of yourself, resume the work in a future context window. In that window, this summary replaces the conversation history. Make the summary structured, thorough, and actionable. Include every detail a fresh instance needs to continue the work. A fresh instance must not have to re-discover what you learned. Include:
1. Task Overview.
The user's core request and success criteria.
Any clarifications or constraints they stated.
2. Current State.
The work that is complete so far.
Files created, modified, or analyzed (with paths where they apply).
Key outputs or artifacts produced.
3. Important Discoveries.
Technical constraints or requirements you found.
Decisions made and their rationale.
Errors you found and how you corrected them.
The approaches that failed, and the reason each one failed.
4. Next Steps.
Specific actions needed to complete the task.
Any blockers or open questions to resolve.
Priority order for the steps that remain.
5. Context to Preserve.
User preferences or style requirements.
Domain-specific details that are not obvious.
Any promises made to the user.
Be thorough and complete. Include anything that prevents duplicate work, repeated mistakes, or lost context. Length is not a concern. Completeness is the concern. Write so that any fresh instance can resume the work at once and with full information.
Wrap your summary in <summary></summary> tags.
