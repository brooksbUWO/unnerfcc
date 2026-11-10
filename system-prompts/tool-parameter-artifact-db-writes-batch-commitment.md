<!--
name: 'Tool Parameter: Artifact batch writes commitment semantics'
description: >-
  Specifies that each document is addressed at most once, caps the batch body at
  1 MiB, and states the all-or-nothing commitment where the server supports it.
ccVersion: 2.1.321
-->
}. Each document is addressed at most once and the whole batch body is at most 1 MiB; the batch commits all-or-nothing where the server supports it, else 
