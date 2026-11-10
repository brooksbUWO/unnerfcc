<!--
name: 'Task Notification: Receipt may arrive after auto-replies resumed'
description: >-
  Clause telling the model this receipt reaches it on a later turn, and that a
  turn which is the user's own typed message has already resumed auto-replies.
ccVersion: 2.1.321
variables:
  - RESUMED_AUTO_REPLIES_PRONOUN
  - ALREADY_RESUMED_EXTRA_NOTE
  - ARTIFACT_REFERENCE
  - RESUME_TRIGGER_EXTRA_NOTE
  - UNPROMPTED_PUBLISH_NOTE
  - COMMENT_TIMING_NOTE
  - STOP_FOR_GOOD_NOTE
-->
this receipt reaches you with a later turn: if that turn is the user's own typed message it has already resumed ${RESUMED_AUTO_REPLIES_PRONOUN}${ALREADY_RESUMED_EXTRA_NOTE}, otherwise the user's next message resumes ${RESUMED_AUTO_REPLIES_PRONOUN} (so does a publish of ${ARTIFACT_REFERENCE} the user asks for${RESUME_TRIGGER_EXTRA_NOTE}; ${UNPROMPTED_PUBLISH_NOTE})${COMMENT_TIMING_NOTE}; ${STOP_FOR_GOOD_NOTE}
