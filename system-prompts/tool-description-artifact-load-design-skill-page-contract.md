<!--
name: 'Tool Description: Load design skill for page contract and calibration'
description: >-
  Requires loading the page-contract skill before writing the artifact file,
  including for a .md file, and says where to put the file before calling
  Artifact with its path.
ccVersion: 2.1.321
variables:
  - DESIGN_SKILL
-->
**Before writing the file, Claude must load the `${DESIGN_SKILL}` skill**, including for a `.md` file that a skill told Claude to write. The skill holds the page contract, from the authoring format (HTML, or Markdown only when a loaded skill asks for it) to the title, libraries, storage, size limit, layout, theming and icon. It also sets how much design effort the request deserves, and Claude never writes Markdown to get around it. Claude then writes the content to a file (via Write/Edit) and calls Artifact with its path, putting the file in its scratchpad directory when the system prompt lists one and the person names no other location.
