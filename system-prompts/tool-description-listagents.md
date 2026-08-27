<!--
name: "Tool Description: ListAgents"
description: "Describes the ListAgents tool, which lists agents you can message — in-process subagents, other local and cloud Claude sessions, and remote bridge sessions"
ccVersion: "2.1.232"
variables:
  - "SEND_MESSAGE_TOOL_NAME"
-->
Lists agents you can ${SEND_MESSAGE_TOOL_NAME} to. In-process subagents you spawned, and other local Claude sessions on this machine. With cloud access, also your Claude sessions running in the cloud. A cloud session receives your message but cannot message any session back yet. Do not ask it to reply, read its answer in its own transcript. With Remote Control connected here, also your account's other sessions: Remote Control sessions on other machines and cloud sessions. Each row is labeled by kind. Names are the address: send with `${SEND_MESSAGE_TOOL_NAME}({to: "<name>", message: "..."})`, copying the name exactly as a row prints it. Append a row's ` [ref]` only where the bare name is not enough. Two rows share it, or an error asks you to disambiguate.
