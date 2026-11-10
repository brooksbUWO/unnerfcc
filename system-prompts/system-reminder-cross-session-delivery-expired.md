<!--
name: 'System Reminder: Cross-session delivery expired'
description: >-
  Notifies the sending session that its cross-session message was not approved
  before expiry and never delivered, and tells it not to wait for a reply or
  resend unprompted while the permission modes differ.
ccVersion: 2.1.321
variables:
  - MESSAGE_REFERENCE
  - RECIPIENT_REFERENCE
  - RECIPIENT_SESSION_DESCRIPTION
  - MESSAGE_SUBJECT
-->
[Cross-session delivery notice] ${MESSAGE_REFERENCE} ${RECIPIENT_REFERENCE} not approved before expiry${RECIPIENT_SESSION_DESCRIPTION}. Not delivered to that session's Claude, and nothing is waiting there. Do not wait for a reply, and do not resend unprompted: while the two sessions' permission modes differ a resend is only held again. Tell your user what was not delivered and why; send ${MESSAGE_SUBJECT} again, edited if that helps, when they ask.
