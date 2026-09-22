<!--
name: 'Tool Description: Artifact page contract intro when skills unavailable'
description: >-
  Introduces the embedded page contract as this tool's own because skills are
  unavailable in this session, then says to write the file and call Artifact
  with its path.
ccVersion: 2.1.280
-->
**Before writing the file**, Claude reads the page contract below, from the authoring format to the title, libraries, storage, size limit, layout, theming and icon: it is this tool's own contract, and skills are not available in this session. Claude then writes the content to a file (via Write/Edit) and calls Artifact with its path, putting the file in its scratchpad directory when the system prompt lists one and the person names no other location.
