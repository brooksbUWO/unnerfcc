<!--
name: 'Tool Result: Artifact In Different Organization'
description: >-
  Explains that the artifact belongs to another of the user's organizations, so
  nothing in this session can read it, and tells the model to say so rather than
  guess its values.
ccVersion: 2.1.321
variables:
  - ACCESS_CONDITION
-->
it is in another of the user's organizations, or one they are no longer part of, so nothing in this session can read it until ${ACCESS_CONDITION} — say so rather than guess its values
