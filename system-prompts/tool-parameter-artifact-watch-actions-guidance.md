<!--
name: "Tool Parameter: Artifact watch actions guidance"
description: "Describes Artifact watch, unwatch, status, durable remote wake, comment wake, and explicit resume_replies behavior"
ccVersion: "2.1.235"
variables:
  - "HAS_ARTIFACT_COMMENTS"
-->
 'watch' opens a live-update subscription to the artifact at `url` so this session is notified once another session republishes it. 'unwatch' stops that subscription. 'status' lists this session's artifact watches (pass `url` to check one). Watches live only as long as this session. In a remote session there is no live stream: 'watch' registers a durable wake subscription instead. This session is then woken with a new turn once the artifact is next published${HAS_ARTIFACT_COMMENTS ? " or a comment on it is sent to Claude" : ""} (no live updates. On wake re-read the artifact${HAS_ARTIFACT_COMMENTS ? " — and its comments, on a comment wake" : ""}).${HAS_ARTIFACT_COMMENTS ? " 'resume_replies' re-enables automatic comment replies that were stopped for the artifact at `url`. They stop where their live-updates task is killed or the watch is unwatched. They also stop where the user interrupts the session with Ctrl+C / Stop. Use it ONLY where the user explicitly asked to resume auto-replies. It re-arms the live watch and is approved the way a publish is (a prompt in default mode). It cannot undo the session-wide auto-reply disarm from the kill-all-agents gesture. In a remote session it is unavailable (no live watch to re-arm — comment wakes come through 'watch'). There, say so rather than calling it." : ""}
