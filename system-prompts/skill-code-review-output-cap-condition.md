<!--
name: 'Skill: Code Review output cap condition'
description: >-
  Instructs keeping only the most severe findings if the count exceeds the
  maximum.
ccVersion: 2.1.292
variables:
  - MAX_FINDINGS
-->
If more than ${MAX_FINDINGS} survive, keep the ${MAX_FINDINGS} most
severe.
