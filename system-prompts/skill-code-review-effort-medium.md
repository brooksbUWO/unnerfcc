<!--
name: 'Skill: Code Review (medium effort)'
description: >-
  Effort-tier prompt for a precision-biased medium-effort review — eight
  subagent finder angles, each surfacing candidates with file, line, summary,
  and a concrete failure scenario.
ccVersion: 2.1.321
variables:
  - REVIEW_SCOPE_PREAMBLE
  - AGENT_TOOL_NAME
  - TEST_FILE_SCOPE_NOTE
  - CORRECTNESS_ANGLES
  - CLEANUP_ANGLES
  - VERIFY_PHASE
-->
`

You are reviewing for **precision** at medium effort: every finding you surface
should be one a maintainer would act on.

${REVIEW_SCOPE_PREAMBLE}
## Phase 1 — Find candidates (3 correctness angles + 3 cleanup angles + 1 altitude angle + 1 conventions angle, up to 6 each)

Run **8 independent finder angles** via the ${AGENT_TOOL_NAME} tool. Each
surfaces **up to 6 candidate findings** with `file`, `line`, a one-line
`summary`, and a concrete `failure_scenario`. ${TEST_FILE_SCOPE_NOTE}

${CORRECTNESS_ANGLES}
${CLEANUP_ANGLES}
Pass every candidate with a nameable failure scenario through — finders that
silently drop half-believed candidates bypass the verify step and are the
dominant cause of misses.

${VERIFY_PHASE}
