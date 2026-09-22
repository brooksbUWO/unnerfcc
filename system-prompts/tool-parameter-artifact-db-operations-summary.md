<!--
name: 'Tool Parameter: Artifact database operations summary'
description: >-
  Summarizes the artifact database read and write actions and the parameters
  each one takes.
ccVersion: 2.1.280
-->
Reads: 'get' (one document: `collection` + `doc_id`), 'list' (a page of a collection: `collection`, with optional `query.limit`/`query.cursor`), 'query' (filtered: `collection` + `query`). Writes: 'set' (replace) or 'update' (merge) with `collection`, `doc_id`, and either `data` or `file_path`;
