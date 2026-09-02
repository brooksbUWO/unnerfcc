<!--
name: 'Tool Result: DesignSync Needs Login (Non-Interactive)'
description: >-
  Tells the model DesignSync needs design-system authorization that
  /design-login cannot obtain in this non-interactive session, and how the user
  can authorize from an interactive session or seed the project instead.
ccVersion: 2.1.257
-->
DesignSync needs design-system authorization, and /design-login cannot run in this non-interactive session. Ask the user to run /design-login once from an interactive Claude Code session on this machine — headless and SDK runs here then reuse that authorization. If this is claude.ai/code, ask them instead to use Claude Design's "Send to Claude Code Web" (which seeds the project into the workspace) or to provide the project files directly.
