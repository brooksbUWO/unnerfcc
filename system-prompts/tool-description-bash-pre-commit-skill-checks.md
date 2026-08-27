<!--
name: "Tool Description: Bash (pre-commit skill checks)"
description: "Requires applicable verification, simplification, and code-review skills to be visibly reported and run before nontrivial git commits"
ccVersion: "2.1.225"
variables:
  - "EACH_SKILL_PREFIX"
  - "FORMATTED_PRE_COMMIT_SKILLS_LIST"
  - "SKILL_REFERENCE_PRONOUN"
  - "VERIFY_NO_RUNTIME_SURFACE_SKIP_NOTE"
  - "EMPTY_STRING"
  - "MISSING_PROJECT_VERIFY_SKILL_NOTE"
-->
Do this immediately before `git commit` on a completed change. Write one visible sentence. In it, name each skill by its literal name, for ${EACH_SKILL_PREFIX}${FORMATTED_PRE_COMMIT_SKILLS_LIST}. State for each one whether it RAN or NOT RUN this session. Your own tests, typecheck, e2e, or any "equivalent" do not count as a run. Only a call to the skill counts. A material change is any non-comment source line that changed since the skill ran. If ${SKILL_REFERENCE_PRONOUN} already ran this session and the diff has no material change since, do not run it again. If a skill is NOT RUN, run it before you commit. Token budget, background mode, and autonomy level are not valid reasons to skip a skill. A user request to ship or to open a PR does not waive this rule. Skip a skill only after the user tells you not to run it. In that case, say so in the sentence and quote the user's words. One exception exists. Skip these skill runs for a trivial commit that does not touch product behavior. A trivial commit is one of these classes only: dotfiles or personal-config sync, lockfile or formatting changes, comment or doc edits, and version bumps. For a trivial commit, say in the sentence that you skipped because the change is trivial. Any change that touches product behavior is not trivial, whatever its size.${VERIFY_NO_RUNTIME_SURFACE_SKIP_NOTE}${EMPTY_STRING}${MISSING_PROJECT_VERIFY_SKILL_NOTE}
