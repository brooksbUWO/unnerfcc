<!--
name: 'Code Review: One-line findings output'
description: >-
  Tells the code review pass to emit one-line file:line findings most-severe
  first and to widen to other hunks before stopping short of the target count.
ccVersion: 2.1.321
variables:
  - MIN_FINDINGS_TARGET
-->
, most-severe first, one line each:
`path/to/file.ext:123 — what's wrong and the concrete failure`.
Target at least min(files_changed, ${MIN_FINDINGS_TARGET}) findings — if you see fewer, widen to other hunks in the same diff before stopping. If fewer than ${MIN_FINDINGS_TARGET} genuine findings exist, emit what you have.
