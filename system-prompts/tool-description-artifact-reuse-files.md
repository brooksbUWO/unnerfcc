<!--
name: 'Tool Description: Artifact reuse files'
description: >-
  Explains how to reuse another artifact's published files through the files map
  and which file types can be copied that way.
ccVersion: 2.1.321
-->
 Another artifact's published files are reused through a publish instead: in `files`, Claude maps a path to `{"artifact": "<its url>", "path": "<its published path>"}` and the server copies that file into the new version with its type. Script, style, data, font and image files copy this way, SVG images among them; an HTML or XML document does not, so Claude reads it with `read_file` and publishes it as its own file.
