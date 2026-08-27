<!--
name: "Tool Description: TaskUpdate"
description: "Description for the TaskUpdate tool, which updates Claude's task list"
ccVersion: "2.1.173"
-->
Use this tool to update a task in the task list.

## When to Use This Tool

**Mark tasks as resolved:**
- You finished the work described in a task.
- A task is no longer needed, or another task superseded it.
- IMPORTANT: Always mark your assigned tasks resolved after you finish them.
- After you resolve a task, call TaskList to find your next task.

- ONLY mark a task completed after you FULLY accomplish it.
- For errors, blockers, or an unfinished task, keep the task in_progress.
- For a blocked task, create a new task that describes what must be resolved.
- Never mark a task completed in these cases:
  - Tests fail.
  - The implementation is partial.
  - You hit unresolved errors.
  - You cannot find necessary files or dependencies.

**Delete tasks:**
- A task is no longer relevant, or it was created in error.
- Status `deleted` removes the task permanently.

**Update task details:**
- The requirements change or become clearer.
- You set dependencies between tasks.

## Fields You Can Update

- **status**: The task status (see Status Workflow that follows).
- **subject**: Change the task title (imperative form, for example, "Run tests").
- **description**: Change the task description.
- **activeForm**: Present continuous form shown in the spinner for an in_progress task (for example, "Running tests").
- **owner**: Change the task owner (agent name).
- **metadata**: Merge metadata keys into the task (set a key to null to delete it).
- **addBlocks**: Mark tasks that cannot start until this one completes.
- **addBlockedBy**: Mark tasks that must complete before this one can start.

## Status Workflow

Status progresses: `pending` → `in_progress` → `completed`

Use `deleted` to permanently remove a task.

## Staleness

Before you update a task, read its latest state with `TaskGet`.

## Examples

To mark a task in progress at the start of work:
```json
{"taskId": "1", "status": "in_progress"}
```

To mark a task completed at the end of work:
```json
{"taskId": "1", "status": "completed"}
```

Delete a task:
```json
{"taskId": "1", "status": "deleted"}
```

To claim a task, set the owner:
```json
{"taskId": "1", "owner": "my-name"}
```

To set task dependencies:
```json
{"taskId": "2", "addBlockedBy": ["1"]}
```
