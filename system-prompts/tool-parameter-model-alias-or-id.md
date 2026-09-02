<!--
name: 'Tool Parameter: Model alias or full model ID'
description: >-
  model field accepting a model alias or full model ID, where 'inherit' selects
  the main model and omission falls back to the configured default subagent
  model and then the main model.
ccVersion: 2.1.257
-->
Model alias (e.g. 'fable', 'opus', 'sonnet', 'haiku') or full model ID (e.g. 'claude-fable-5'). 'inherit' uses the main model; if omitted, uses the default subagent model when one is configured, else the main model
