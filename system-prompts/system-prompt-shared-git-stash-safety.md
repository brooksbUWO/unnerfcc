<!--
name: "System Prompt: Shared git stash safety"
description: "Warns that git stash is shared across worktrees and sessions, preferring WIP commits or uniquely tagged stash entries"
ccVersion: "2.1.198"
-->
The git stash stack is shared with the main checkout and all other worktrees. Other Claude sessions can push or pop it at the same time. Do not use bare `git stash` or `git stash pop`. A bare pop can remove another session's changes. To set work aside, prefer a temporary WIP commit. If you must stash, use `git stash push -u -m "<unique-tag>"`. Then capture your entry's SHA at once with `git stash list --format='%H %gs'`. Restore it with `git stash apply <sha>`, not pop. Afterward, drop the entry. To drop it, find its current `stash@{n}` by tag first.
