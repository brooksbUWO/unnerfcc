<!--
name: tool-description-todowrite-compact
description: ''
ccVersion: 2.1.235
-->
Create and update a task list for the current session. The list is shown to the user as your working plan.

- Each todo has `content`, `status` ("pending" | "in_progress" | "completed"), and `activeForm`. The `activeForm` is a present-tense label shown during progress.
- Send the full list each call. It replaces the previous list.
- Keep one item `in_progress` at a time. When the item is done, mark it `completed`.
