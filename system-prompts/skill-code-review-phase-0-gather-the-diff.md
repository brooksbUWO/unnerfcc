<!--
name: "Skill: Code Review (Phase 0 — gather the diff)"
description: "Opening step of the code-review skill: assemble the unified diff to review with git diff"
ccVersion: "2.1.173"
-->
## Phase 0. Gather the diff.

Run `git diff @{upstream}...HEAD` to get the unified diff under review (with
no upstream, use `git diff main...HEAD` / `git diff HEAD~1`). If there are
uncommitted changes, or the range diff is empty, also run `git diff HEAD` and
include the working-tree changes. The review often runs before the
commit. If a PR number, branch name, or file path was passed as an argument,
review that target instead. Treat this diff as the review scope.
