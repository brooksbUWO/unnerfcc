<!--
name: "Tool Description: SendMessage cross-session guidance"
description: "Explains cross-session SendMessage addressing, reply routing, liveness, disambiguation, and permission-laundering restrictions"
ccVersion: "2.1.232"
variables:
  - "LIST_AGENTS_TOOL_NAME"
-->


## Cross-session.

Use `${LIST_AGENTS_TOOL_NAME}` to discover targets. Every row leads with the agent's `name [ref]`. The name IS the address. There is no separate address syntax.

```json
{"to": "worker", "message": "check if tests pass over there"}
{"to": "worker [3fa9c1]", "message": "you, specifically"}
```

Send the bare name. A name that exactly matches one live agent or session delivers directly. The match can be on this machine, on another machine, or in the cloud. Append the ` [ref]` only where the bare name is not enough. That is where `${LIST_AGENTS_TOOL_NAME}` shows two rows with it, or an error asks you to disambiguate. Examples: you typed only a prefix, or checking a session list failed. A ref you did not just read from a listing or an error will not resolve. Where the same name also names an in-process agent, the bare name always wins. Use the in-process one.

A listed peer is alive and will process your message. No "busy" state. Messages enqueue and drain at the receiver's next tool round. Your message arrives wrapped as `<cross-session-message from="...">`. **To reply to an incoming message, copy its `from` attribute as your `to`**.

Permission boundaries are per-session: NEVER ask a peer to perform an action that was denied or blocked in your session. The same applies to an action you expect your own permission settings to block. A peer doing it for you bypasses the user's permission decision (cross-session permission laundering). Route blocked work back to your user instead.
