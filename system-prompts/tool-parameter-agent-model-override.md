<!--
name: 'Tool Parameter: Agent Model Override'
description: >-
  Optional model override for a spawned agent — how it outranks the agent
  definition's frontmatter and the configured default subagent model, what it
  falls back to when omitted, and that fork subagents always inherit the parent
  model.
ccVersion: 2.1.257
-->
Optional model override for this agent. Takes precedence over the agent definition's model frontmatter and the configured default subagent model. If omitted, uses the agent definition's model, else the default (inherits from the parent unless a default subagent model is configured). Ignored for subagent_type: "fork" — forks always inherit the parent model.
