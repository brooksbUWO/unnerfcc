<!--
name: 'Tool Description: Agent (simple usage notes)'
description: >-
  Simplified usage notes for the Agent tool covering where an agent type's
  model, reasoning effort, and tools come from and what worktree isolation does.
ccVersion: 2.1.321
-->
Each agent type's model, reasoning effort, and tools come from its definition (`.claude/agents/*.md` frontmatter or SDK `agents`). Also take note that `isolation: "worktree"` gives the agent its own git worktree (auto-cleaned if unchanged).
