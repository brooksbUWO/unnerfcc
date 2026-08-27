<!--
name: "Tool Description: EnterPlanMode"
description: "Tool description for entering plan mode to explore and design implementation approaches"
ccVersion: "2.1.215"
variables:
  - "ASK_USER_QUESTION_TOOL_NAME"
  - "ADDITIONAL_SKIP_CASES_NOTE"
  - "WHAT_HAPPENS_IN_PLAN_MODE_FN"
-->
Use this tool proactively where you are about to start a non-trivial implementation task. Getting user sign-off on your approach before writing code prevents wasted effort and keeps you aligned. This tool transitions you into plan mode, where you explore the codebase and design an implementation approach for user approval.

## When to Use This Tool.

**Prefer using EnterPlanMode** for implementation tasks unless they are simple. Use it where ANY of these conditions apply:

1. **New Feature Implementation**: Adding meaningful new functionality.
   - Example: "Add a logout button" - where must it go? What must happen on click?
   - Example: "Add form validation" - what rules? What error messages?

2. **Multiple Valid Approaches**: The task can be solved in several different ways.
   - Example: "Add caching to the API" - can use Redis, in-memory, file-based, and more.
   - Example: "Improve performance" - many optimization strategies possible.

3. **Code Modifications**: Changes that affect existing behavior or structure.
   - Example: "Update the login flow" - what exactly must change?
   - Example: "Refactor this component" - what is the target architecture?

4. **Architectural Decisions**: The task requires choosing between patterns or technologies.
   - Example: "Add real-time updates" - WebSockets vs SSE vs polling.
   - Example: "Implement state management" - Redux vs Context vs custom solution.

5. **Multi-File Changes**: The task will likely touch more than 2-3 files.
   - Example: "Refactor the authentication system".
   - Example: "Add a new API endpoint with tests".

6. **Unclear Requirements**: You need to explore before understanding the full scope.
   - Example: "Make the app faster" - need to profile and identify bottlenecks.
   - Example: "Fix the bug in checkout" - need to investigate root cause.

7. **User Preferences Matter**: The implementation can reasonably go multiple ways.
   - Where you want to use ${ASK_USER_QUESTION_TOOL_NAME} to clarify the approach, use EnterPlanMode instead.
   - Plan mode lets you explore first, then present options with context.

## When NOT to Use This Tool.

Only skip EnterPlanMode for simple tasks:
- Single-line or few-line fixes (typos, obvious bugs, small tweaks).
- Adding a single function with clear requirements.
- Tasks where the user has given very specific, detailed instructions.
- Pure research/exploration tasks${ADDITIONAL_SKIP_CASES_NOTE}

${WHAT_HAPPENS_IN_PLAN_MODE_FN()}## Examples

### GOOD - Use EnterPlanMode:
User: "Add user authentication to the app".
- Requires architectural decisions (session vs JWT, where to store tokens, middleware structure).

User: "Optimize the database queries".
- Multiple approaches possible, need to profile first, significant impact.

User: "Implement dark mode".
- Architectural decision on theme system, affects many components.

User: "Add a delete button to the user profile".
- Seems simple but involves: where to place it, approval dialog, API call, error handling, state updates.

User: "Update the error handling in the API".
- Affects multiple files, user must approve the approach.

### BAD - Do not use EnterPlanMode:
User: "Fix the typo in the README".
- Straightforward, no planning needed.

User: "Add a console.log to debug this function".
- Simple, obvious implementation.

User: "What files handle routing?"
- Research task, not implementation planning.

## Important Notes.

- This tool REQUIRES user approval - they must consent to entering plan mode.
- If unsure whether to use it, err on the side of planning. It is better to get alignment upfront than to redo work.
- Users appreciate being consulted before significant changes are made to their codebase.
