<!--
name: 'Tool Description: Artifact publish action'
description: >-
  Describes the publish action for creating an artifact or updating an existing
  one in place, and the parameters it takes.
ccVersion: 2.1.280
variables:
  - PUBLISH_PARAMS_NOTE
-->
- **publish** (the default): takes `file_path`, plus `icon` on a first publish and an optional one-sentence `description`, and with `url` updates that existing artifact in place${PUBLISH_PARAMS_NOTE}.
