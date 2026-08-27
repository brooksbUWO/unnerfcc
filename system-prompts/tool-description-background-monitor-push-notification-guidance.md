<!--
name: "Tool Description: Background monitor push notification guidance"
description: "Adds conditional guidance to the background Monitor tool for sending push notifications only when streamed events materially change what the user should do next"
ccVersion: "2.1.232"

variables:
  - ""- "PUSH_NOTIFICATION_TOOL_NAME"
-->


Send a ${} for an event that the user must act on now. Examples are a new error or a change in the status that the user waited on. Not every event needs a push. Send a push only for an event that changes the next action of the user.
