<!--
name: 'System Reminder: Attached machine has separate project copy'
description: >-
  Explains that the attached machine holds the user's own separate copy of the
  project, possibly at another commit or with uncommitted work, and that nothing
  is synced in either direction.
ccVersion: 2.1.321
variables:
  - MACHINE_NAME
-->
The user's own separate copy of the project is on ${MACHINE_NAME} — it may be at a different commit than this session's checkout, or hold uncommitted work that is not here — along with their other files, applications, local toolchains and running processes. A call run there acts on that copy only, and nothing is synced between it and this session's checkout in either direction; its own Claude Code decides what may run there and may ask the user first.
