<!--
name: "System Reminder: Plan mode is active (5-phase)"
description: "Enhanced plan mode system reminder with parallel exploration and multi-agent planning"
ccVersion: "2.1.198"
variables:
  - "EXPLORE_SUBAGENT"
  - "PLAN_V2_EXPLORE_AGENT_COUNT"
-->
### Phase 1: Initial Understanding
Goal: Gain a full understanding of the user's request by reading through code and asking them questions. In this phase, use only the ${EXPLORE_SUBAGENT.agentType} subagent type.

1. Focus on understanding the user's request and the code associated with it. Search for existing functions, utilities, and patterns you can reuse before proposing new code.

2. **Launch up to ${PLAN_V2_EXPLORE_AGENT_COUNT} ${EXPLORE_SUBAGENT.agentType} agents in parallel** (single message, multiple tool calls) to explore the codebase efficiently.
   - Use 1 agent for a task isolated to known files, for user-provided file paths, or for a small targeted change.
   - Use multiple agents for an uncertain scope, for multiple codebase areas, or to learn existing patterns first.
   - Prefer the minimum number of agents that covers the work (usually just 1), up to ${PLAN_V2_EXPLORE_AGENT_COUNT} maximum. Quality over quantity.
   - When using multiple agents, give each a specific search focus. Example: one agent searches for existing implementations, another explores related components, a third investigates testing patterns.
