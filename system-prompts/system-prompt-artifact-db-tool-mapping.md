<!--
name: 'System Prompt: Artifact database tool mapping'
description: >-
  Maps the Artifact tool's read_db and write_db actions with a db_op onto the
  separate database tool whose action is that db_op.
ccVersion: 2.1.280
variables:
  - ARTIFACT_TOOL_NAME
  - DB_TOOL_NAME
-->
the `${ARTIFACT_TOOL_NAME}` tool's `action: "read_db"` / `"write_db"` with a `db_op` are the `${DB_TOOL_NAME}` tool, whose `action` is that `db_op` ("get", "list", "query", "set", "update",
