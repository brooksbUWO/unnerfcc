<!--
name: "Data: Auto-compact inputs changed event schema"
description: "Schema description for worker-resolved auto-compaction state events used by thin clients to display the effective compaction countdown"
ccVersion: "2.1.227"
-->
@internal Worker-resolved auto-compact state. CCR workers emit it at boot and after a conversation reset. They also emit it whenever the resolved state changes (/autocompact, model switch, settings change). They re-check the state at each turn start. Thin clients adopt this state for the "% until auto-compact" indicator. The indicator then counts down to the worker's real compaction trigger. It does not re-resolve against client-local state. Turn-scoped divergence is accepted. A turn can run under a skill or command frontmatter model override. That turn compacts against the override model's window. The frame keeps the resting model's window. The local indicator has the same limit. From sessionState.onAutocompactInputsChanged.
