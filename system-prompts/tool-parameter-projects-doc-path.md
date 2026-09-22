<!--
name: 'Tool parameter: Projects doc path'
description: >-
  Describes the path parameter for the Projects tool's read, write, delete and
  memory-read methods, including the claude/ namespacing of new bare filenames.
ccVersion: 2.1.280
-->
project_read/project_write/project_delete: doc path. project_write: an existing path is replaced in place; a new bare filename (no "/") is namespaced to "claude/<name>". project_memory_read: memory file path as listed by project_memory_list.
