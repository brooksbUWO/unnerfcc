<!--
name: 'Tool Result: Artifact unknown content type for extension'
description: >-
  Validation error for a file whose extension maps to no servable content type,
  telling the model to rename it or declare an explicit contentType under
  `files`.
ccVersion: 2.1.280
variables:
  - FILE_EXTENSION
  - KNOWN_EXTENSIONS_CLAUSE
  - TRAILING_DETAIL_CLAUSE
-->
 (${FILE_EXTENSION}) — nothing was published. ${KNOWN_EXTENSIONS_CLAUSE} Rename a text or data file to one of these (.txt .json .csv), or make another file the `file_path` and list this one under `files` with contentType "text/plain". ${TRAILING_DETAIL_CLAUSE}
