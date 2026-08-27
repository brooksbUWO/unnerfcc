<!--
name: "System Reminder: Ultrareview launch acknowledgement"
description: "Instructs Claude to briefly acknowledge an already-visible cloud review launch, remember --fix intent, and relate later findings to an optional review note"
ccVersion: "2.1.235"
variables:
  - "SHOULD_APPLY_REVIEW_FIXES"
  - "REVIEW_NOTE"
  - "TRUNCATE_CONTENT_FN"
  - "REVIEW_NOTE_MAX_CHARS"
-->
The output above is already visible to the user. Briefly acknowledge it without repeating the target, URL, or billing note. Findings will arrive via task-notification.${SHOULD_APPLY_REVIEW_FIXES ? " The user passed --fix: when the findings arrive, apply them to the local working tree." : ""}${REVIEW_NOTE ? ` The user's argument was interpreted as a review note, not a base branch: "${TRUNCATE_CONTENT_FN(REVIEW_NOTE, REVIEW_NOTE_MAX_CHARS)}". The cloud review runs its standard pass over the branch diff and does not see the note; when the findings arrive, prioritize and relate them to the user's request.` : ""}
