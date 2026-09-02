<!--
name: 'Tool Parameter: Artifact action â€” asset upload, list, read, and delete'
description: >-
  Describes the artifact action field's asset values â€” upload_asset,
  list_assets, read_asset, and delete_asset â€” and the inputs each one takes,
  now including text files.
ccVersion: 2.1.257
-->
 'upload_asset' adds one local media, PDF, font, or text file to an existing artifact — pass `url` and `file_path`. 'list_assets' lists the files in an artifact's asset store (pass `url`; `after` continues a listing), 'read_asset' saves one of them to a local file named by its id (pass `url` and `asset_id`, optionally `out_dir`), and 'delete_asset' permanently removes one (pass `url` and `asset_id`). See **Artifact assets** above.
