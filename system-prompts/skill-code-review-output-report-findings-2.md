<!--
name: 'Code Review: ReportFindings Output Instructions'
description: >-
  Tells the code review pass to report findings most-severe first through a
  single ReportFindings call with the required entry fields, never also as text.
ccVersion: 2.1.321
variables:
  - REPORT_FINDINGS_TOOL_NAME
  - MIN_FINDINGS_TARGET
-->
, most-severe first, in one
${REPORT_FINDINGS_TOOL_NAME} call with `{level, findings}` — each entry has
`file`, `line`, `summary`, `short_summary` (≤60 characters), and
`failure_scenario`.
Target at least min(files_changed, ${MIN_FINDINGS_TARGET}) findings — if you see fewer, widen to other hunks in the same diff before stopping. If fewer than ${MIN_FINDINGS_TARGET} genuine findings exist, report what you have. Do not also print the findings as text.
