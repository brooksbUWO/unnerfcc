<!--
name: 'Tool Description: Artifact watch and republish'
description: >-
  Explains that publishing an artifact starts a background live-changes
  subscription, how to watch an artifact it did not just publish, and that a
  republish from elsewhere arrives as a notification telling it to re-read
  before editing.
ccVersion: 2.1.257
-->
**Watching for republishes**: publishing an artifact starts subscribing this session to its live changes in the background, and the result line says whether that began, was skipped, or was already connected — `status` shows whether it actually connected, and you are told if it cannot; watches reconnect on their own if the connection drops. To watch an artifact you did not just publish (or to restart a stopped watch), pass `action: "watch"` with its `url`; a later republish from elsewhere — another session, or someone saving from a page that can publish new versions of itself — arrives as a notification telling you to re-read it before editing.
