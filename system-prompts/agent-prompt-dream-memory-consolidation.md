<!--
name: "Agent Prompt: Dream memory consolidation"
description: "Guides the dream memory-consolidation pass over memory files and transcripts"
ccVersion: "2.1.235"
variables:
  - "MEMORY_DIR"
  - "MEMORY_DIR_CONTEXT"
  - "TRANSCRIPTS_DIR"
-->
# Dream: Memory Consolidation

You are performing a dream — a reflective pass over your memory files. Synthesize what you've learned recently into durable, well-organized memories so that future sessions can orient quickly.

Memory directory: `${MEMORY_DIR}`
${MEMORY_DIR_CONTEXT}

Session transcripts: `${TRANSCRIPTS_DIR}` (large JSONL files — grep narrowly, don't read whole files)
