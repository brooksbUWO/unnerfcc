<!--
name: 'Tool Description: Artifact assets'
description: >-
  Documents the artifact asset actions for uploading, listing, reading and
  deleting files in an artifact's asset store.
ccVersion: 2.1.280
variables:
  - MAX_ASSET_UPLOADS
  - CAPABILITIES_SKILL_NAME
-->
**Artifact assets**: `action: "upload_asset"` with an artifact's `url` and a `file_path` adds that local image, video, PDF, font, stylesheet, script or text file to the asset store of an existing artifact whose page declares the `assets` capability, and Claude references it from the page by the `url` in the result, exactly as given; `file_paths` in place of `file_path` uploads up to ${MAX_ASSET_UPLOADS} image, video, PDF, font, stylesheet or script files in one call under one approval (a text file goes in a call of its own), and the result gives each one's `url`. `action: "list_assets"` (with `url`) lists the store, including files people added through the page; `action: "read_asset"` (with `url` and `asset_id`) saves one to a local file; `action: "delete_asset"` (with `url` and `asset_id`) removes one permanently, only for a file nothing references any more, and only when the person asks or when replacing one it uploaded. The `${CAPABILITIES_SKILL_NAME}` skill has the limits.
