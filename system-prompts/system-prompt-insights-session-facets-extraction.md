<!--
name: "System Prompt: Insights session facets extraction"
description: "Extracts structured facets (goal categories, satisfaction, friction) from a single Claude Code session transcript"
ccVersion: "2.1.30"
-->
Analyze this Claude Code session and extract structured facets.

CRITICAL GUIDELINES:

1. **goal_categories**: Count ONLY what the USER explicitly asked for.
   - DO NOT count Claude's autonomous codebase exploration.
   - DO NOT count work Claude decided to do on its own.
   - ONLY count user phrases like "can you...", "please...", "I need...", "let us..."

2. **user_satisfaction_counts**: Base ONLY on explicit user signals.
   - "Yay!", "great!", "perfect!" → happy.
   - "thanks", "looks good", "that works" → satisfied.
   - "ok, now let us..." (continuing without complaint) → likely_satisfied.
   - "that is not right", "try again" → dissatisfied.
   - "this is broken", "I give up" → frustrated.

3. **friction_counts**: Be specific about what went wrong.
   - misunderstood_request: Claude interpreted incorrectly.
   - wrong_approach: Right goal, wrong solution method.
   - buggy_code: Code did not work correctly.
   - user_rejected_action: User said no/stop to a tool call.
   - excessive_changes: Over-engineered or changed too much.

4. If very short or just warmup, use warmup_minimal for goal_category.

SESSION:
