<!--
name: "Tool Description: TaskCreate"
description: "Tool description for TaskCreate tool"
ccVersion: "2.1.84"
variables:
  - "CONDITIONAL_TEAMMATES_NOTE"
  - "CONDITIONAL_TASK_NOTES"
-->
Use this tool to create a structured task list for your current coding session. This helps you track progress, organize complex tasks, and demonstrate thoroughness to the user.
It also helps the user understand the progress of the task and overall progress of their requests.

## When to Use This Tool

Use this tool proactively in these scenarios:

- Complex multi-step tasks. A task requires 3 or more distinct steps or actions.
- Non-trivial and complex tasks. A task requires careful planning or multiple operations.${CONDITIONAL_TEAMMATES_NOTE}
- Plan mode. In plan mode, create a task list to track the work.
- User explicitly requests a todo list. The user directly asks you to use the todo list.
- User provides multiple tasks. The user gives a list of things to do (numbered or comma-separated).
- New instructions. Capture user requirements as tasks at once.
- You start a task. Mark it in_progress BEFORE you begin work.
- You finish a task. Mark it completed and add any new follow-up tasks that you found.

## When NOT to Use This Tool

Skip this tool in these cases:
- There is only a single, straightforward task.
- The task is trivial, and tracking gives no organizational benefit.
- The task takes fewer than 3 trivial steps.
- The task is purely conversational or informational.

NOTE: do not use this tool for only one trivial task. In this case, do the task directly.

## Task Fields

- **subject**: A brief, actionable title in imperative form (for example, "Fix authentication bug in login flow").
- **description**: What needs to be done.
- **activeForm** (optional): Present continuous form shown in the spinner for an in_progress task (for example, "Fixing authentication bug"). If you omit it, the spinner shows the subject instead.

All tasks start with status `pending`.

## Tips

- Create tasks with clear, specific subjects that describe the outcome.
- After you create tasks, use TaskUpdate to set dependencies (blocks/blockedBy) as needed.
${CONDITIONAL_TASK_NOTES}- Check TaskList first to avoid duplicate tasks.
