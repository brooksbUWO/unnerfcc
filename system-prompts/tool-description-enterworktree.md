<!--
name: "Tool Description: EnterWorktree"
description: "Creates a new isolated worktree or enters an existing one only when explicitly requested, with eligibility, switching, lifecycle, and cleanup rules"
ccVersion: "2.1.203"
-->
Use this tool ONLY where explicitly instructed to work in a worktree. Either by the user directly, or by project instructions (CLAUDE.md / memory). This tool creates an isolated git worktree and switches the current session into it.

## When to Use.

- The user explicitly says "worktree" (for example "start a worktree", "work in a worktree", "create a worktree", "use a worktree").
- CLAUDE.md or memory instructions direct you to work in a worktree for the current task.

## When NOT to Use.

- The user asks to create a branch, switch branches, or work on a different branch. Use git commands instead.
- The user asks to fix a bug or work on a feature. Use normal git workflow unless worktrees are explicitly requested by the user or project instructions.
- Never use this tool unless "worktree" is explicitly mentioned by the user or in CLAUDE.md / memory instructions.

## Requirements.

- Must be in a git repository, OR have WorktreeCreate/WorktreeRemove hooks configured in settings.json.
- Must not already be in a worktree session where you create a new worktree (`name`). Switching into another existing worktree via `path` is allowed.

## Behavior.

- In a git repository: creates a new git worktree inside `.claude/worktrees/` on a new branch. The base ref is governed by the `worktree.baseRef` setting: `fresh` (default) branches from origin/<default-branch>. `head` branches from your current local HEAD.
- Outside a git repository: delegates to WorktreeCreate/WorktreeRemove hooks for VCS-agnostic isolation.
- Switches the session's working directory to the new worktree.
- Use ExitWorktree to leave the worktree mid-session (keep or remove). On session exit, where still in the worktree, the user will be prompted to keep or remove it.

## Entering an existing worktree.

Pass `path` instead of `name` to switch the session into a worktree that already exists. For example, one you just created with `git worktree add`. On first entry from the launch directory, the path must appear in `git worktree list` for the repository that owns it. The current repository or, in a multi-repo workspace, a repository nested inside it. Paths registered by neither are rejected. ExitWorktree will not remove a worktree entered this way. Use `action: "keep"` to return to the original directory.

Switching with `path` also works where the session is already in a worktree. The previous worktree is left on disk, untouched, and only the new one is tracked for exit-time cleanup. The switch also works from agents whose working directory was pinned at launch (subagent isolation or explicit cwd). In both cases the target must be a worktree under `.claude/worktrees/` of the same repository. From a pinned agent the switch only affects this agent, not the parent session. After a further switch, previously-visited worktrees are no longer writable. Re-issue EnterWorktree with `path` to return to one.

## Parameters.

- `name` (optional): A name for a new worktree. If neither `name` nor `path` is provided, a random name is generated.
- `path` (optional): Path to an existing worktree to enter instead of creating one. Of the current repository, or (on first entry from the launch directory) of a repository nested inside it. Mutually exclusive with `name`.
