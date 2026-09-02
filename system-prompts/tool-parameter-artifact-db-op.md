<!--
name: 'Tool Parameter: Artifact database operation'
description: >-
  db_op field of the artifact tool â€” which operations belong to read_db and
  which to write_db, including batch, and that it is required for both database
  actions and meaningless for every other action.
ccVersion: 2.1.257
variables:
  - MAX_BATCH_WRITES
-->
Database operation: 'get', 'list' or 'query' for read_db; 'set', 'update' or 'delete' for write_db, or 'batch' to send up to ${MAX_BATCH_WRITES} of those in `writes` under one approval. Required for both database actions; meaningless for every other action.
