<!--
name: 'Tool Result: Artifact comment notification scope clause'
description: >-
  Explains when comments sent to Claude reach this session based on the
  artifact's status row, and that plain comments never notify.
ccVersion: 2.1.280
variables:
  - STATUS_ROW_VALUE
-->
; a comment on it sent to Claude reaches this session while this artifact's status row says ${STATUS_ROW_VALUE}, and plain comments never notify — read them with 
