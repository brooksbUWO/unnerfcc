<!--
name: 'Tool Parameter: Artifact type query filter'
description: >-
  Filter parameter for list_types that narrows the listing to the best-matching
  types, and when to omit it because a narrowed listing is not the whole
  catalog.
ccVersion: 2.1.280
-->
list_types only: narrow the listing to the types whose title or description match this text best (case-insensitive); a type that matches less well is left out, so a narrowed listing is not the whole catalog. Omit it when choosing a type for a request, unless a listing made without it says more types exist than it shows.
