<!--
name: "Data: SendMessage ambiguous recipient display"
description: "Builds the user-facing display message for an ambiguous SendMessage recipient, covering exact-name confirmation, multiple matches, unavailable session sources, truncated search, and pinned-identity warnings"
ccVersion: "2.1.235"
variables:
  - "AMBIGUOUS_RECIPIENT_RESOLUTION"
  - "SEND_MESSAGE_INPUT"
  - "HAS_UNAVAILABLE_SESSION_SOURCES"
  - "UNAVAILABLE_SESSION_SOURCES_SUMMARY"
  - "FIRST_RECIPIENT_CANDIDATE"
  - "RECIPIENT_CANDIDATES_DISPLAY"
  - "SEARCH_TRUNCATION_NOTE"
  - "PINNED_IDENTITY_WARNING"
-->
${AMBIGUOUS_RECIPIENT_RESOLUTION.total === 1 ? (AMBIGUOUS_RECIPIENT_RESOLUTION.matchedBy === "prefix" ? `Not sent — no agent is named '${SEND_MESSAGE_INPUT.to}' exactly${HAS_UNAVAILABLE_SESSION_SOURCES ? ` among the sessions that could be checked (${UNAVAILABLE_SESSION_SOURCES_SUMMARY})` : ""}; asked Claude to confirm it means '${FIRST_RECIPIENT_CANDIDATE.name}'.` : AMBIGUOUS_RECIPIENT_RESOLUTION.pinnedIdentityClaimedLocally ? `Not sent — '${SEND_MESSAGE_INPUT.to}' needs a confirm before this send.` : HAS_UNAVAILABLE_SESSION_SOURCES ? `Not sent yet — '${SEND_MESSAGE_INPUT.to}' matches '${FIRST_RECIPIENT_CANDIDATE.name}', but ${UNAVAILABLE_SESSION_SOURCES_SUMMARY}; asked Claude to confirm.` : `Not sent — '${SEND_MESSAGE_INPUT.to}' needs a one-time confirm before this send; asked Claude to confirm it means '${FIRST_RECIPIENT_CANDIDATE.name}'.`) : AMBIGUOUS_RECIPIENT_RESOLUTION.matchedBy === "prefix" ? `Not sent — '${SEND_MESSAGE_INPUT.to}' matches ${AMBIGUOUS_RECIPIENT_RESOLUTION.total} agents by prefix (${RECIPIENT_CANDIDATES_DISPLAY}${AMBIGUOUS_RECIPIENT_RESOLUTION.total > AMBIGUOUS_RECIPIENT_RESOLUTION.candidates.length ? ", …" : ""}); asked Claude to pick one.` : `Not sent — ${AMBIGUOUS_RECIPIENT_RESOLUTION.total} agents are named '${SEND_MESSAGE_INPUT.to}' (${RECIPIENT_CANDIDATES_DISPLAY}${AMBIGUOUS_RECIPIENT_RESOLUTION.total > AMBIGUOUS_RECIPIENT_RESOLUTION.candidates.length ? ", …" : ""}); asked Claude to pick one.`}${HAS_UNAVAILABLE_SESSION_SOURCES && AMBIGUOUS_RECIPIENT_RESOLUTION.total !== 1 ? ` Note: ${UNAVAILABLE_SESSION_SOURCES_SUMMARY}.` : ""}${SEARCH_TRUNCATION_NOTE}${PINNED_IDENTITY_WARNING}
