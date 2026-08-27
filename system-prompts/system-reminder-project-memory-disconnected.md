<!--
name: "System Reminder: Project memory disconnected"
description: "Warns that a prior shared project-memory connection and its results are stale after disconnect or failed reconnection, and directs the agent to re-check with memory_list"
ccVersion: "2.1.235"
variables:
  - "FORMAT_MEMORY_PROJECT_FN"
  - "PREVIOUS_MEMORY_CONNECTION_STATE"
  - "MEMORY_CONNECTION_OUTCOME"
  - "IS_PROJECT_SELECTION_DROPPED"
  - "MEMORY_TOOL_NAMES"
  - "MEMORY_LIST_TOOL_NAME"
-->
This session is no longer connected to ${FORMAT_MEMORY_PROJECT_FN(PREVIOUS_MEMORY_CONNECTION_STATE.project)} (${MEMORY_CONNECTION_OUTCOME === "disconnected" ? "the user turned it off in /memory" : IS_PROJECT_SELECTION_DROPPED ? "the project the user re-picked is no longer available, so the pick was cleared and nothing connected" : "reconnecting to the re-picked project failed"}). Any connected memory store list or shared memory index in your system prompt is stale. Any ${MEMORY_TOOL_NAMES} results earlier in this conversation are stale too. Nothing is connected for the memory tools to serve until the user reconnects in /memory. ${MEMORY_LIST_TOOL_NAME} with no arguments reports the connected store, or that nothing is connected. If the user asks you to remember something and your system prompt names a personal memory directory, use that directory. Otherwise explain that project memory is disconnected for this session.
