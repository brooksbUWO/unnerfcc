<!--
name: 'Tool Result: Cloud review findings'
description: >-
  Introduces the findings a cloud review produced, followed by the rendered
  findings and any fix or posting-status instructions.
ccVersion: 2.1.280
variables:
  - FINDINGS_LIST
  - FIX_INSTRUCTIONS
  - PR_POST_STATUS_NOTE
-->

The cloud review produced the following findings:

${FINDINGS_LIST}${FIX_INSTRUCTIONS}${PR_POST_STATUS_NOTE}
