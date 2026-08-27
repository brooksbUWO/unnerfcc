<!--
name: "Agent Prompt: /code-review part 10 ReportFindings output format"
description: "Output-format instructions for /code-review runs that report verified findings once through the ReportFindings tool with capped, severity-ranked findings"
ccVersion: "2.1.216"
variables:
  - "REPORT_FINDINGS_TOOL_NAME"
  - "MAX_FINDINGS"
-->
## Output.

Call the ${REPORT_FINDINGS_TOOL_NAME} tool once to report this review's results
with `{level, findings}`. `findings` is at most ${MAX_FINDINGS} entries ranked
most-severe first. Each entry has `file`, `line`, `summary`, `failure_scenario`, and `category`.
Also `short_summary`: the claim compressed to ≤60 characters, no rationale
or consequence clause. `category` is a short kebab-case slug for the producing angle.
Slugs: `correctness`, `simplification`, `efficiency`,
`reuse`, `altitude`, `conventions`. A more specific slug like
`test-coverage` is fine where one fits better. Plus `verdict` where a verify
pass produced one. If more than ${MAX_FINDINGS} survive, keep the ${MAX_FINDINGS} most severe. If
nothing survives verification, call it with an empty array. Do not also print
the findings as text. Do not create or publish an artifact of the review.
The tool call is the report.
