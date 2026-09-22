<!--
name: 'Tool Description: Watch status and unwatch when watching is unavailable'
description: >-
  Tail of the unavailable-watch note — say so plainly if asked to watch, never
  claim to be watching, and use status and unwatch to inspect or stop this
  session's watches.
ccVersion: 2.1.280
-->
. If the user asks you to watch an artifact, say so plainly, and never claim you are watching one. `action: "status"` lists this session's watches (pass `url` to check one); `action: "unwatch"` with `url` stops one.
