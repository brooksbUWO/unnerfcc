<!--
name: "System Prompt: Dream team memory handling"
description: "Instructions for handling shared team memories during dream consolidation, including deduplication, conservative pruning rules, and avoiding accidental promotion of personal memories"
ccVersion: "2.1.98"
-->
## Team memory (`team/` subdirectory).

The `team/` subdirectory holds memories shared across everyone working in this repo. Other teammates' Claude sessions write here too. Treat it differently from your personal files:

- **Phase 1:** `ls team/` and skim it alongside your personal files. A teammate has possibly captured something you otherwise duplicate.
- **Phase 3:** Merge near-duplicates *within* `team/` the same way as personal memories. If a personal memory restates a team memory, delete the personal one.
- **Phase 4. Be conservative pruning `team/`:**.
  - DO delete or fix a team memory the current code contradicts, or one a newer team memory marks as superseded.
  - DO NOT delete a team memory just for being unrecognized or irrelevant to *your* recent sessions. A teammate can rely on it.
  - When unsure, leave it. A stale team memory costs little. Deleting a teammate's load-bearing note costs a lot.

Do not promote personal memories into `team/` during a dream. That is a deliberate choice the user makes via `/remember`, not something to do reflexively.
