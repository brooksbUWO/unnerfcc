<!--
name: 'Tool Result: Disk full on the temporary-directory volume'
description: >-
  Reports that the volume holding Claude Code's temporary directory is nearly
  full, with the path, the free space, and what that blocks.
ccVersion: 2.1.321
variables:
  - TEMP_DIRECTORY_PATH
  - FREE_MEGABYTES
  - CONSEQUENCE_CLAUSE
  - REMEDY_CLAUSE
-->
Disk full: this computer's volume holding ${TEMP_DIRECTORY_PATH} (Claude Code's temporary directory) has ${FREE_MEGABYTES} MB free, ${CONSEQUENCE_CLAUSE} ${REMEDY_CLAUSE}
