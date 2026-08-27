<!--
name: "Tool Description: TaskList"
description: "Description for the TaskList tool, which lists all tasks in the task list"
ccVersion: "2.1.173"

variables:
  - ""
  - ""
  - ""- "TEAMMATE_TASKLIST_WHEN_TO_USE_NOTE"
  - "TASKLIST_ID_OUTPUT_LINE"
  - "TEAMMATE_WORKFLOW_BLOCK"
-->
Use this tool to list all tasks in the task list.

## When to Use This Tool

- Use it to see which tasks are available to work on (status: 'pending', no owner, not blocked).
- Use it to check overall progress on the project.
- Use it to find tasks that are blocked and need dependencies resolved.
${}- Use it after a task, to find newly unblocked work or to claim the next available task.
- When several tasks are available, **prefer tasks in ID order** (lowest ID first). Earlier tasks often set up the context for later ones.

## Output

Returns a summary of each task:
${}
- **subject**: Brief description of the task.
- **status**: 'pending', 'in_progress', or 'completed'.
- **owner**: Agent ID for an assigned task, empty for an available task.
- **blockedBy**: List of open task IDs that must be resolved first. You cannot claim a task with a blockedBy list until its dependencies resolve.

Use TaskGet with a specific task ID to view full details, such as the description and comments.
${}
