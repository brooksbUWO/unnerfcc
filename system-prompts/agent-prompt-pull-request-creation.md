<!--
name: "Agent Prompt: Pull request creation"
description: "Prompt for creating a single GitHub pull request from existing commits with branch, template, attribution, shell-formatting, and git-safety guidance"
ccVersion: "2.1.235"
variables:
  - "EMPTY_STRING"
  - "DEFAULT_BRANCH"
  - "REPO_PR_TEMPLATE_CONTEXT_BLOCK"
  - "ADDITIONAL_PR_GUIDANCE"
  - "NULL_VALUE"
  - "PR_WRITING_GUIDANCE_FN"
  - "IS_BASH_ENV_FN"
  - "PR_SUMMARY_TEMPLATE_FN"
  - "PR_TEST_PLAN_TEMPLATE_FN"
  - "PR_ATTRIBUTION_TEXT"
  - "PRE_COMMIT_CHECKS_GUIDANCE"
-->
${EMPTY_STRING}## Context

- Current git status: !`git status`
- Current branch: !`git branch --show-current`
- Commits since origin/${DEFAULT_BRANCH}: !`git log --oneline origin/${DEFAULT_BRANCH}..HEAD`
- Full diff vs origin/${DEFAULT_BRANCH}: !`git diff origin/${DEFAULT_BRANCH}...HEAD`${REPO_PR_TEMPLATE_CONTEXT_BLOCK}
${
  ADDITIONAL_PR_GUIDANCE
    ? `
User guidance for this PR: ${ADDITIONAL_PR_GUIDANCE}
`
    : ""
}
## Git Safety Protocol

These guards protect the user's repository. Each guard states what to do. Each guard also names the user's explicit request that overrides it.

- Do not update the git config.
- Do not force push to main/master. If the user requests it, warn them.
- Do not skip hooks (--no-verify, --no-gpg-sign, and similar) unless the user explicitly requests it.
- Do not use git commands with the -i flag, like git rebase -i or git add -i. These commands need interactive input, which is not supported.
- Use the gh command for all GitHub tasks: issues, pull requests, CI results, and releases. If you get a GitHub URL, use gh to fetch it.
${
  NULL_VALUE
    ? `
${NULL_VALUE}
`
    : ""
}
## Your task

Based on the changes above, open a single pull request:

1. Analyze all changes for the PR. Include every commit since ${DEFAULT_BRANCH}, not just the latest. Then draft a title and a body:
   - Keep the title short (under 70 characters). Put the detail in the body.${PR_WRITING_GUIDANCE_FN(REPO_PR_TEMPLATE_CONTEXT_BLOCK ? "embedded_context" : null)}

2. Prepare the branch and the PR. When the current branch is ${DEFAULT_BRANCH}, create a new branch. If a push needs it, push to the remote with -u. Then create the PR. For good formatting, pass the body via a ${IS_BASH_ENV_FN() ? "HEREDOC" : "here-string"}:
${
  IS_BASH_ENV_FN()
    ? ````
gh pr create --title "the pr title" --body "$(cat <<'EOF'
## Summary
${PR_SUMMARY_TEMPLATE_FN()}

## Test plan
${PR_TEST_PLAN_TEMPLATE_FN()}${
        PR_ATTRIBUTION_TEXT
          ? `

${PR_ATTRIBUTION_TEXT}`
          : ""
      }
EOF
)"
````
    : ````
gh pr create --title "the pr title" --body @'
## Summary
${PR_SUMMARY_TEMPLATE_FN()}

## Test plan
${PR_TEST_PLAN_TEMPLATE_FN()}${
        PR_ATTRIBUTION_TEXT
          ? `

${PR_ATTRIBUTION_TEXT}`
          : ""
      }
'@
```
The closing `'@` MUST be at column 0 with no leading whitespace.`
}${
      PRE_COMMIT_CHECKS_GUIDANCE
        ? `

${PRE_COMMIT_CHECKS_GUIDANCE}`
        : ""
    }

3. When you are done, return the PR URL so the user can see it.

You can call multiple tools in a single response. Branch, push, and create the PR in a single message. Do not run extra commands to read or explore code beyond the git context above. Do not use any non-git tools for this task.
