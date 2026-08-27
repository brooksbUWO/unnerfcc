<!--
name: "Data: Thin-client diff dialog schema"
description: "Internal data description for workspace git diff payloads used by the thin-client diff dialog"
ccVersion: "2.1.198"
-->
@internal Workspace git diff for the thin-client /diff dialog. The diff field is null in two cases: the workspace is not a git repo, or it is in a transient git state (merge, rebase, cherry-pick). A path in skippedLarge has no hunks entry at all. Its membership alone marks it as too large. An empty hunks array with a non-empty perFileStats is not a failure signal by itself. This is the normal shape in two cases. In the first case, all changes are untracked. For untracked files, git diff emits no hunks, so you get stats only. In the second case, every file was withheld. This shape can also occur after the hunks fetch failed one time and only stats are available.
