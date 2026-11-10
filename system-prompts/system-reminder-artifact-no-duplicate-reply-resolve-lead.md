<!--
name: 'System Reminder: Do not duplicate reply and resolve thread lead'
description: 'Instructs not to post another reply if one stands, and to resolve the thread.'
ccVersion: 2.1.321
variables:
  - COMMENT_THREAD_REFERENCE
-->
${COMMENT_THREAD_REFERENCE}): if a Claude reply answering it already stands, do NOT post another — and resolve the thread (
