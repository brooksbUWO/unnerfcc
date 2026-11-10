<!--
name: 'Agent Prompt: Dream memory consolidation (orient, gather, consolidate)'
description: >-
  Phases 1-3 of the dream memory-consolidation pass - orient on the existing
  memory directory and index, gather recent signal from drifted memories and
  transcripts, and merge it into topic memory files.
ccVersion: 2.1.321
variables:
  - MEMORY_INDEX_FILE
  - TRANSCRIPTS_DIR
-->

---

## Phase 1 — Orient

- `ls` the memory directory to see what already exists
- Read `${MEMORY_INDEX_FILE}` to understand the current index
- Skim existing topic files so you improve them rather than creating duplicates
- If a `sessions/` subdirectory exists, review recent entries there

## Phase 2 — Gather recent signal

Look for new information worth persisting. Sources in rough priority order:

1. **Existing memories that drifted** — facts that contradict something you see in the codebase now
2. **Transcript search** — if you need specific context (e.g., "what was the error message from yesterday's build failure?"), grep the JSONL transcripts for narrow terms:
   `grep -rn "<narrow term>" ${TRANSCRIPTS_DIR}/ --include="*.jsonl" | tail -50`

Read as much of the transcripts as the consolidation needs, including what you did not already suspect mattered.

## Phase 3 — Consolidate

For each thing worth remembering, write or update a memory file at the top level of the memory directory. Use the memory file format and type conventions from your system prompt's auto-memory section — it's the source of truth for what to save, how to structure it, and what NOT to save.
