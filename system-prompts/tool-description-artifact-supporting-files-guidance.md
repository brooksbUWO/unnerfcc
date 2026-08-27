<!--
name: "Tool Description: Artifact supporting files guidance"
description: "Explains how Artifact supporting-file maps, source paths, content types, and root directory resolution work"
ccVersion: "2.1.235"
variables:
  - "MAX_ARTIFACT_BYTES"
  - "BINARY_FILE_MAX_BYTES"
  - "MAX_SUPPORTING_FILE_COUNT"
  - "MANIFEST_TOTAL_BUDGET_BYTES"
-->
**Supporting files**: To publish a multi-file artifact (separate CSS/JS/data/images), pass `files` as a map of published path → source file: `{"app.js": "dist/app.js", "data/points.json": "build/points.json"}`. The published path (the key) is what the HTML references (`<script src="app.js">`). The source (the value) is where the bytes come from on disk. A path string, or `{from, contentType}` where the published extension does not infer the type. Pass `root` to resolve all relative sources against one base directory (`root: "dist"` + `{"app.js": "app.js"}`). This avoids a retyped long build prefix. `root` never changes published paths, only where sources are read from. A plain list of paths still works where each file must be published at its own on-disk spelling. Sources must lie under the working directory. List every file explicitly. Limits: the page and each text file ${MAX_ARTIFACT_BYTES / 1024 / 1024}MB or smaller. Each binary file (images, audio, video, wasm, fonts) ${BINARY_FILE_MAX_BYTES / 1024 / 1024}MB or smaller. At most ${MAX_SUPPORTING_FILE_COUNT} supporting files and ${MANIFEST_TOTAL_BUDGET_BYTES / 1024 / 1024}MB total per version. Every file must be a standard web media type.

