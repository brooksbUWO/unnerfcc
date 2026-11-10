<!--
name: 'Tool Description: Reuse another artifact''s published files'
description: >-
  Explains how to copy another artifact's published files via the files
  parameter, which types copy server side, and that an HTML or XML document must
  be read and republished as its own file.
ccVersion: 2.1.321
-->
. Another artifact's published files are reused through `files` instead: Claude maps a path to {"artifact": "<its url>", "path": "<its published path>"} and that file is copied into the new version server side with its type. Script, style, data, font and image files copy this way, SVG images among them; an HTML or XML document does not, so Claude reads it with `path` and publishes it as its own file
