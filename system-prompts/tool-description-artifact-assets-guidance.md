<!--
name: "Tool Description: Artifact assets guidance"
description: "Explains how to upload, list, read, reference, and permanently delete files in an existing Artifact asset store"
ccVersion: "2.1.234"
-->


**Artifact assets**: use this to put a local image, video, PDF, or font file into an existing artifact: the page must declare the `assets` capability. Pass `action: "upload_asset"` with the artifact's `url` and the `file_path`. Then reference the file from the page by the relative `url` in the result ("_blob/{id}"). `action: "list_assets"` (with `url`) lists what the store holds. Ids, types, sizes. Including files people added through the page. `action: "read_asset"` (with `url` and `asset_id`, optionally `out_dir`) saves one to a local file named by its id. `action: "delete_asset"` (with `url` and `asset_id`) removes one permanently. Delete only a file nothing references any more. Do it only on the user's ask, or to replace one you uploaded. The results and the `artifact-capabilities` skill carry the limits and details.
