<!--
name: 'Tool Parameter: Artifact watch scope and lifetime'
description: >-
  Details unwatch, status, watch lifetimes, and which session types hold
  artifact watches.
ccVersion: 2.1.280
-->
; 'unwatch' stops that subscription; 'status' lists this session's artifact watches (pass `url` to check one). Watches live only as long as this session, and only a main-loop session (interactive, SDK, or background) holds one — a subagent, teammate, or print session's publish or 'watch' arms none.
