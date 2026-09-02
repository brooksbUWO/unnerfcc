<!--
name: 'Tool Result: Reading another person''s artifact assets has no consent surface'
description: >-
  Tells the model the read needs a consent surface nobody can answer in this
  session, so it should raise the read with the user in chat instead of
  retrying.
ccVersion: 2.1.257
variables:
  - FOREIGN_ASSET_DESCRIPTION
-->
Reading or listing ${FOREIGN_ASSET_DESCRIPTION} needs a consent surface, and no one can answer the prompt in this session — raise the read with the user in chat; do not retry it in this session.
