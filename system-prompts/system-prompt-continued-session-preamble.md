<!--
name: Continued Session Compaction Preamble
description: >-
  Preamble telling the model this session continues a conversation that ran out
  of context and that the summary below covers the earlier portion.
ccVersion: 2.1.280
variables:
  - CONVERSATION_SUMMARY
-->
This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.

${CONVERSATION_SUMMARY}
