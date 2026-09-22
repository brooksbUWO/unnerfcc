<!--
name: 'Tool Result: Start new Artifact from type instructions'
description: >-
  Explains how to create an Artifact from a type with a title and no files
  first, when to pass auto_open, and how the create result says to fill it.
ccVersion: 2.1.280
-->
, a `title` (what the user called it, or a short descriptive name) and no files first (passing `auto_open: "after_first_write"` when your next step publishes files to it or writes its store, never for a type whose content you write through a connector, such as a Claude Docs document); the create result carries the new Artifact's `url` and the type's instructions, and says how to fill it — documents written to its own store, or data files published to that `url`.
