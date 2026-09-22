<!--
name: 'Tool Parameter: Artifact asset upload parameter description'
description: >-
  Explains uploading local media, font, and text assets to an artifact's asset
  store with asset: true, several files in one call, and referencing them by the
  returned url verbatim.
ccVersion: 2.1.280
variables:
  - MAX_ASSET_FILES
  - ASSET_REFERENCE_NOTE
-->
. With `url`, `file_path` and `asset: true`, it instead uploads that local image, video, PDF, font or text file to the artifact's asset store; `file_paths` in place of `file_path` uploads up to ${MAX_ASSET_FILES} image, video, PDF, font, stylesheet or script files in one call under one approval (a text file goes in a call of its own), and the result gives each one's `url`. The page must declare the `assets` capability, and the `artifact-capabilities` skill has the limits. Claude references the uploaded file from the page by the `url` in the result, exactly as given${ASSET_REFERENCE_NOTE}
