<!--
name: 'Tool Description: TaskCreate'
description: Tool description for TaskCreate tool
ccVersion: 2.1.219
variables:
  - CONDITIONAL_TEAMMATES_NOTE
  - CONDITIONAL_TASK_NOTES
-->
Use this tool to create the task list for the current session. The list makes your progress visible to the user: the current step, the completed steps, and the remaining work. Hidden progress is a silent failure, because the user cannot see a stalled or drifted plan.

## When to Use This Tool

Create the list at the start of any work that takes more than one step, and keep it current:

- Multi-step work - When the work takes two or more distinct steps or actions
- Work that needs planning - When the work needs investigation, several operations, or verification${CONDITIONAL_TEAMMATES_NOTE}
- Plan mode - When using plan mode, create a task list to track the work
- User requests - When the user asks for a todo list, or gives several tasks (numbered or comma-separated)
- New instructions - Record new requirements as tasks as soon as they arrive
- Start of a task - Mark it in_progress BEFORE you begin the work
- End of a task - Mark it completed as soon as it is done, and add any follow-up tasks you found

## When Not to Use This Tool

Skip the list only for a single action with an immediate result, or for a purely conversational or informational request. If you are not sure, create the list.

## Task Fields

- **subject**: A brief, actionable title in imperative form (e.g., "Fix authentication bug in login flow")
- **description**: What needs to be done
- **activeForm** (optional): Present continuous form shown in the spinner when the task is in_progress (e.g., "Fixing authentication bug"). If omitted, the spinner shows the subject instead.

All tasks are created with status `pending`.

## Tips

- Create tasks with clear, specific subjects that describe the outcome
- After creating tasks, use TaskUpdate to set up dependencies (blocks/blockedBy) if needed
${CONDITIONAL_TASK_NOTES}- Check TaskList first to avoid creating duplicate tasks
