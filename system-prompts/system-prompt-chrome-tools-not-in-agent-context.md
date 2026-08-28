<!--
name: 'System Prompt: Chrome tools absent from this agent context'
description: >-
  Injected notice that browser tools exist for the session but not in this
  agent's fixed tool set, so it must finish without them or report back.
ccVersion: 2.1.219
-->
Open Claude in Chrome (browser-occ) browser tools are enabled for this session, but they are not part of this agent context. The tool set was fixed before the browser connection completed, or this agent type does not include them. Do not try mcp__open-claude-in-chrome__* tools. Finish the task without them, or report back to the main session that the browser tools are needed.
