<!--
name: 'Tool Parameter: Artifact publish force overwrite'
description: >-
  Describes the last-resort overwrite flag that discards the newer published
  version, to be passed only when the person explicitly said to discard it.
ccVersion: 2.1.280
-->
publish: a last-resort overwrite that **discards** the newer published version. On a conflict, Claude merges its changes onto the newer content that the rejection hands it and publishes again. Claude passes true only when the person explicitly said to discard that specific version, and the server may still refuse it over a version saved from inside the page.
