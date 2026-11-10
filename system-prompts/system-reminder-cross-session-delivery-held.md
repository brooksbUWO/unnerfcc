<!--
name: 'System Reminder: Cross-session delivery held for approval'
description: >-
  Notifies the sending session that its cross-session message is held by the
  recipient session and undelivered, explains the permission-mode cause, and
  tells it not to wait for a reply or resend while held.
ccVersion: 2.1.321
variables:
  - MESSAGE_REFERENCE
  - RECIPIENT_REFERENCE
  - RECIPIENT_SESSION_DESCRIPTION
  - MESSAGE_SUBJECT
-->
[Cross-session delivery notice] ${MESSAGE_REFERENCE} ${RECIPIENT_REFERENCE} held by that session${RECIPIENT_SESSION_DESCRIPTION}. NOT delivered: its Claude has not seen ${MESSAGE_SUBJECT}. Do not report ${MESSAGE_SUBJECT} as delivered, do not wait for a reply, and do not resend while held. The usual cause is that the two sessions run in different permission modes: a terminal session then asks its user to approve, but a Claude Desktop or non-interactive session cannot ask, so there the hold expires undelivered unless the modes come to match. A session can also be set to hold every message. Another notice follows on release, denial or expiry. Tell your user what is held and why, or choose another approach.
