<!--
name: "Tool Description: Background monitor WebSocket source"
description: "Addendum to the background monitor tool description covering the WebSocket (ws) source, which opens a WebSocket and streams each incoming text frame as a notification event instead of running a shell command, with notes on binary frames, socket close, and rate limiting"
ccVersion: "2.1.195"
-->

**ws source**: open a WebSocket and stream each incoming text frame as an event. There is no shell and no polling. The server pushes, and you get a notification.

  Monitor({
    ws: {url: 'wss://events.example.com/stream', protocols: ['v1']},
    description: 'deploy events',
  })

Each text frame becomes one notification (multiline frames stay as one event). This tool reports a binary frame as `[binary frame, N bytes]` and does not pass it through. A socket close ends the watch and surfaces the close code. Errors are surfaced before the close. The rate limiting is the same as bash. A firehose is suppressed and then stopped. For this reason, subscribe to a filtered feed where one exists.

Use this tool instead of `command: 'websocat wss://…'`. It avoids the extra process and line-buffering pitfalls. Use bash to transform or filter frames with shell tools before they become events.
