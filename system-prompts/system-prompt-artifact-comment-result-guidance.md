<!--
name: "System Prompt: Artifact comment result guidance"
description: "Appends reply, resolve, and focused thread-read instructions to Artifact comment-list tool results"
ccVersion: "2.1.227"
-->
To reply, call Artifact with action "reply". Pass the same url, a thread_id from above, and text (plain text, ≤4096 UTF-8 bytes). Only activated threads accept replies. Replies appear to viewers as "Claude · via the user". After your work on a thread is done, call action "resolve" with the same url and its thread_id. Resolve only threads you actually addressed, and only threads that are open: a thread already marked resolved stays resolved (a reply there is fine. Never re-resolve it). To read one thread on its own (up to the size cap): call action "comments" with the same url and its thread_id.
