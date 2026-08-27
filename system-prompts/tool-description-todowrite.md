<!--
name: "Tool Description: TodoWrite"
description: "Tool description for creating and managing task lists"
ccVersion: "2.1.84"
variables:
  - "EDIT_TOOL_NAME"
-->
Use this tool to create and manage a structured task list for the current coding session. It tracks progress, organizes complex work, and lets the user follow what is done and what remains.

## When to Use This Tool

When the work has structure worth tracking, use this tool:

1. The task takes three or more distinct steps or actions.
2. The task needs planning or several operations.
3. The user asks for a todo list, or gives several tasks (numbered or comma-separated).
4. New instructions arrive that are worth a record as tasks.
5. You start a task or finish one. Mark a started task in_progress. Mark a finished task completed and add any follow-ups that you found.

## When Not to Use This Tool

Skip this tool for work that tracking does not help. Examples are a single straightforward task, a task under three trivial steps, and a purely conversational or informational request. For one trivial task, do the task directly.

## Examples

<example>
User: I want to add a dark mode toggle to the application settings. Make sure you run the tests and build when you're done!
Assistant: Creates a todo list with these items. 1) Create dark mode toggle component in Settings. 2) Add dark mode state management. 3) Implement dark-theme styles. 4) Update existing components for theme switching. 5) Run tests and the build, and correct any failures. Then begins the first task.

<reasoning>
Dark mode is a multi-step feature. It covers UI, state, and styling. The user explicitly asked for tests and the build afterward. So those become tracked tasks.
</reasoning>
</example>

<example>
User: How do I print 'Hello World' in Python?
Assistant: In Python, you print "Hello World" with `print("Hello World")`.

<reasoning>
A single trivial task answered in one step needs no list.
</reasoning>
</example>

## Task States and Management

- States: pending (not started), in_progress (in progress now, keep exactly one at a time), completed (finished).
- Each task has two forms. The first is content, the imperative form (for example, "Run tests"). The second is activeForm, the present-continuous form shown during the run (for example, "Running tests"). Always give both.
- Update status in real time. Mark a task completed as soon as it is done, not in a batch. Complete the current task before you start the next one. Remove tasks that are no longer relevant.
- Mark a task completed only after it is fully accomplished. Keep a task in_progress in these cases: tests fail, the implementation is partial, errors are unresolved, or required files or dependencies are missing. When a task is blocked, create a new task that describes what must be resolved. A task reported done, but not actually done, is a silent failure.

## Task Breakdown

Create specific, actionable items with clear names, and break complex tasks into smaller steps. Both forms always apply, for example content "Fix authentication bug" and activeForm "Fixing authentication bug". To add a comment to a single function, use the ${EDIT_TOOL_NAME} tool directly rather than tracking it here.
