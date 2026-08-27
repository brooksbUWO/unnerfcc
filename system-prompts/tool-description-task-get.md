<!--
name: "Tool Description: Task Get"
description: "Retrieve a task by ID with full details and comments"
ccVersion: "2.1.173"
-->
Use this tool to retrieve a task by its ID from the task list.

## When to Use This Tool

- Use it to get the full description and context before you start work on a task.
- Use it to understand task dependencies (what it blocks, what blocks it).
- Use it after a task is assigned to you, to get the complete requirements.

## Output

Returns full task details:
- **subject**: Task title.
- **description**: Detailed requirements and context.
- **status**: 'pending', 'in_progress', or 'completed'.
- **blocks**: Tasks that wait on this one to complete.
- **blockedBy**: Tasks that must complete before this one can start.

## Tips

- After you fetch a task, make sure that its blockedBy list is empty before you start work.
- Use TaskList to see all tasks in summary form.
