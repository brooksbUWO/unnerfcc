<!--
name: 'Tool Description: AskUserQuestion'
description: >-
  Tool description for asking the user a question through a selection UI,
  limited to decisions genuinely the user's to make, with notes on the Other
  option, multiSelect, and marking a recommended option.
ccVersion: 2.1.321
-->
You can ask the user a question, which opens a simple UI for them to select an option. Use this tool only for a decision that the user should genuinely make on their own, for example one you cannot determine from sensible defaults, pre-existing code, or the user's own request.

Some notes about asking the user a question via this tool:
- Users will always have an 'Other' option, allowing them to provide custom text input
- Use multiSelect: true if you'd like to allow multiple answers to be selected for your question
- If you are suggesting a specific option, always make that option the first, and add "(Recommended)" at the end of the label.
