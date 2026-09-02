<!--
name: 'Tool Parameter: Feedback report body'
description: >-
  body field of the feedback-draft tool — the labeled bullet format (what
  happened, what the user said, repro, evidence, optional verified cause) the
  report must be written in.
ccVersion: 2.1.257
-->
Labeled bullets, in order: **What happened:** (observed vs. expected, exact error text if short); **What the user said:** (quoted, or "User didn't comment; observed by the model."); **Repro:** (minimal steps); **Evidence:** (request IDs, timestamps, paths, versions; omit if none); optionally a final **Cause:** only if verified in-session. One to three lines per bullet. No narrative paragraphs, no speculation, no secrets.
