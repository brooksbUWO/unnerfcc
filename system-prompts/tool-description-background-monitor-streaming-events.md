<!--
name: 'Tool Description: Background monitor (streaming events)'
description: >-
  Opening of the Monitor tool description explaining that each stdout line of a
  long-running script becomes a notification event that arrives independently of
  the user.
ccVersion: 2.1.280
variables:
  - SINGLE_NOTIFICATION_OPTION_LINE
-->
Start a background monitor that streams events from a long-running script. Each stdout line is an event — you keep working and notifications arrive in the chat. Events arrive on their own schedule and are not replies from the user, even if one lands while you're waiting for the user to answer a question.

Pick by how many notifications you need:
${SINGLE_NOTIFICATION_OPTION_LINE}
- **One per occurrence, 
