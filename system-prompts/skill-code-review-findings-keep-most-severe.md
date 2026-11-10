<!--
name: 'Skill: Code Review findings keep most severe'
description: Instructs keeping the top findings by severity if exceeding the maximum.
ccVersion: 2.1.292
variables:
  - MAX_FINDINGS
-->
If more than ${MAX_FINDINGS} survive, keep the ${MAX_FINDINGS} most severe.
