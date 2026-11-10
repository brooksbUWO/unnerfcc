<!--
name: 'Tool Parameter: Artifact batch writes if_version pinning'
description: >-
  Explains that every batch write entry for an existing document must pin its
  last-read version, and that one stale or unpinned entry makes the whole batch
  write nothing and name that entry.
ccVersion: 2.1.321
-->
, plus if_version — that document's last-read `version`, required for every entry whose document already exists (omit it only when creating); if any pinned document has changed since, or an existing document's entry carries no pin, the whole batch writes nothing and the result names the first such entry
