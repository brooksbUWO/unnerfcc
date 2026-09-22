<!--
name: 'Tool Description: Starting from an Artifact type (third person)'
description: >-
  Third-person description of starting a new Artifact from a type by publishing
  its type_url and title with no files, and updating only its own files
  afterwards.
ccVersion: 2.1.280
-->
To start from a type, Claude publishes with its `type_url`, a `title` and no files. The result is an ordinary private Artifact that carries its `url`, the type's instructions and how to fill it (the type's own store, or Claude's data files published to that `url`). Claude updates it by its `url` as usual and changes only its own files, because the type's page and files stay fixed.
