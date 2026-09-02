<!--
name: 'Tool Result: Durable wake subscription arming'
description: >-
  Tells the model a durable wake subscription is still arming in the background,
  so it is not a subscription until `status` lists it.
ccVersion: 2.1.257
variables:
  - DURABLE_WAKE_BEHAVIOR
-->
Durable wake subscription: arming in the background — not registered yet, so this is not a subscription until `status` lists it (you are told if it cannot be registered). Once registered, ${DURABLE_WAKE_BEHAVIOR}.
