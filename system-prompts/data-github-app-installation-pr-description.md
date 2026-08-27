<!--
name: "Data: GitHub App installation PR description"
description: "Template for PR description when installing Claude Code GitHub App integration"
ccVersion: "2.1.113"
-->
## 🤖 Installing Claude Code GitHub App

This PR adds a GitHub Actions workflow. The workflow turns on Claude Code integration in our repository.

### What is Claude Code?

[Claude Code](https://claude.com/claude-code) is an AI coding agent that can help with:
- Bug fixes and improvements
- Documentation updates
- New features
- Code reviews and suggestions
- Tests
- And more.

### How it works

After this PR is merged, you can call Claude. To call it, mention @claude in a pull request or an issue comment. The mention triggers the workflow. Claude then reads the comment and the context around it. Claude then does the request in a GitHub action.

### Important Notes

- **This workflow does not take effect until this PR is merged**.
- **@claude mentions do not work until after the merge is complete**.
- The workflow runs automatically each time someone mentions @claude in a PR or issue comment.
- Claude gets access to the whole PR or issue context. This context includes files, diffs, and earlier comments.

### Security

- Our Anthropic API key is stored as a GitHub Actions secret.
- Only users with write access to the repository can trigger the workflow.
- All Claude runs are stored in the GitHub Actions run history.
- Claude's default tools can read and write files. They can also make comments, branches, and commits in our repo.
- You can add more allowed tools to the workflow file, like this:

```
allowed_tools: Bash(npm install),Bash(npm run build),Bash(npm run lint),Bash(npm run test)
```

The [Claude Code action repo](https://github.com/anthropics/claude-code-action) has more information.

After you merge this PR, mention @claude in a comment on any PR to get started.
