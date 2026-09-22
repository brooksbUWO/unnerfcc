<!--
name: 'Tool Description: Load design skill before writing artifact'
description: >-
  Requires loading the design skill before writing an artifact file, including a
  skill-instructed .md, so design effort is calibrated and Markdown is not used
  to skip the design pass.
ccVersion: 2.1.280
variables:
  - DESIGN_SKILL
-->
**Before writing the file, Claude must load the `${DESIGN_SKILL}` skill**, including for a `.md` file that a skill told Claude to write. The skill sets how much design effort the request deserves; the Format rule above settles the format, and Claude never writes Markdown to get around the design pass.
