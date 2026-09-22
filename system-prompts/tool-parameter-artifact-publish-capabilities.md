<!--
name: 'Tool Parameter: Artifact publish capabilities'
description: >-
  Describes the runtime capabilities object passed on publish and the skill that
  must be loaded before passing it.
ccVersion: 2.1.280
variables:
  - CAPABILITIES_SKILL_NAME
-->
publish: the runtime capabilities this page declares, as {name: config}. Claude loads the `${CAPABILITIES_SKILL_NAME}` skill before passing it. On a redeploy Claude omits the field to keep what the page has, and {} clears it.
