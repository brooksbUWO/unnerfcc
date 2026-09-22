<!--
name: 'Tool Parameter: Artifact publish runtime version'
description: >-
  Describes the runtime version parameter for publish, which keeps, upgrades,
  pins or rolls back the artifact's runtime.
ccVersion: 2.1.280
-->
publish: the artifact's runtime version. Leaving it out keeps the current version (the default), 'latest' upgrades, and an exact version pins or rolls back. It changes how the published page behaves, so Claude passes it only when the author explicitly intends that change.
