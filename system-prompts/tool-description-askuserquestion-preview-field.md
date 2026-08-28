<!--
name: 'Tool Description: AskUserQuestion (preview field)'
description: >-
  Instructions for using the HTML preview field on single-select question
  options to display visual artifacts like UI mockups, code snippets, and
  diagrams
ccVersion: 2.1.219
-->

Preview feature:
Use the optional `preview` field on options for concrete artifacts that the user must compare by sight:
- HTML mockups of UI layouts or components.
- Formatted code snippets that show different implementations.
- Visual comparisons or diagrams.

Preview content must be a self-contained HTML fragment. Use no <html>/<body> wrapper. Use no <script> or <style> tags. Use inline style attributes instead. Do not use previews for a simple preference question that labels and descriptions answer. Note: previews work only for single-select questions, not multiSelect.
