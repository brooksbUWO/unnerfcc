<!--
name: 'Tool Description: Monitor WebSocket Source'
description: Monitor tool ws source documentation injected into the model's context.
ccVersion: 2.1.219
-->

**ws source**: open a WebSocket and stream each incoming text frame as an event. There is no shell and no polling. The server pushes, and you get a notification.

  Monitor({
    ws: {url: 'wss://events.example.com/stream', protocols: ['v1']},
    description: 'deploy events',
  })

Each text frame becomes one notification (multiline frames stay as one event). This tool reports a binary frame as `[binary frame, N bytes]` and does not pass it through. A socket close ends the watch and surfaces the close code. Errors are surfaced before the close. The rate limiting is the same as bash. A firehose is suppressed and then stopped. For this reason, subscribe to a filtered feed where one exists.

Use this tool instead of `command: 'websocat wss://…'`. It avoids the extra process and line-buffering pitfalls. Use bash to transform or filter frames with shell tools before they become events.
