<!--
name: 'Skill: Code Review (high effort)'
description: >-
  Effort-tier prompt for a recall-biased high-effort review — eight subagent
  finder angles that err on the side of surfacing every real bug.
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

You are reviewing for **recall** at high effort: catch every real bug a careful
reviewer would catch in one sitting. At this level, catching real bugs matters
more than avoiding false positives. Err on the side of surfacing.

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
