<!--
name: "Agent Prompt: CLAUDE.md creation"
description: "Instructs the /init command to analyze a codebase and create or improve a CLAUDE.md file"
ccVersion: "2.1.235"
variables:
  - "IS_IMPORT_ENABLED_FN"
  - "IMPORT_OFFER_NOTE"
-->
Please analyze this codebase and create a CLAUDE.md file. Future instances of Claude Code get this file to operate in this repository.

What to add:
1. Commands that will be commonly used, such as how to build, lint, and run tests. Include the necessary commands to develop in this codebase, such as how to run a single test.
2. High-level code architecture and structure so that future instances can be productive more quickly. Focus on the "big picture" architecture that requires reading multiple files to understand.

Usage notes:
- If there is already a CLAUDE.md, suggest improvements to it.
- When you make the initial CLAUDE.md, do not repeat yourself and do not include obvious instructions. Examples: "Provide helpful error messages to users" or "Write unit tests for all new utilities". Also "Never include sensitive information (API keys, tokens) in code or commits".
- Avoid listing every component or file structure that can be easily discovered.
- Do not include generic development practices.
- If Cursor rules exist (in .cursor/rules/ or .cursorrules) or Copilot rules exist (in .github/copilot-instructions.md), include the important parts.
- If there is a README.md, make sure to include the important parts.${
        IS_IMPORT_ENABLED_FN()
          ? `
- You can find an OpenAI Codex config (`~/.codex/config.toml` or `./.codex/`). Or you can find a Gemini CLI config (`~/.gemini/settings.json`, `./.gemini/`, or a `GEMINI.md`). In that case, ${IMPORT_OFFER_NOTE}`
          : ""
      }
- Do not make up information that other files you read do not expressly include. Examples of made-up sections: "Common Development Tasks", "Tips for Development", "Support and Documentation".
- Be sure to prefix the file with the following text:

```
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.
```
