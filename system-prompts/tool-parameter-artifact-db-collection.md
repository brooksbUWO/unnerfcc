<!--
name: 'Tool Parameter: Artifact database collection path'
description: >-
  collection field of the artifact tool's database actions â€” the segment rules
  for a collection path, how subcollections nest, and that read_db and write_db
  both require it.
ccVersion: 2.1.257
-->
Database collection path: an odd number (1-15) of "/"-separated segments (letters, digits, _ - . ~ : @ + per segment). Paths alternate collection/document, so "boards/b1/columns" is a collection and, with `doc_id` "c2", names the document "boards/b1/columns/c2". Per-user data: "data/users/<id>" (3 segments) is the collection holding that user's documents, "data/users/<id>/decks" is one document in it, and "data/users/<id>/decks/cards" a collection under that; "me" as the <id> means the current user. Required for read_db and write_db.
