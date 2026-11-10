<!--
name: 'Tool Parameter: Artifact database query options'
description: >-
  options field of the artifact database read — limit and cursor paging bounds,
  the where and order_by clauses for a query, and the single-page behavior of an
  ordered query.
ccVersion: 2.1.321
-->
Options for db_op 'list' and 'query': `limit` (1-1000, default 100) and `cursor` (from a prior result's `next_cursor`) page through a collection; `where` clauses ([field, operator, value] triples) and `order_by` filter and order a 'query' only. A query with `order_by` is a single page: it returns at most `limit` documents in that order and never a `next_cursor`, so pass the `limit` you mean (up to 1000), or drop `order_by` and page with `cursor` to read a whole collection.
