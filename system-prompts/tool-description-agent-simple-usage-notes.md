<!--
name: "Tool Description: Agent (simple usage notes)"
description: "Simplified usage notes for the Agent tool, including when to delegate, fork behavior, resumption, worktree isolation, background execution, parallel launches, and context restrictions"
ccVersion: "2.1.235"
variables:
  - "TOOL_BASE_DESCRIPTION"
  - "HAS_PRO_RESTRICTION_NOTE"
  - "IS_DEFAULT_SUBAGENT_STEERING_MODE"
  - "FORK_CONTEXT_NOTE"
  - "CAN_RUN_BACKGROUND_AGENTS"
  - "SEND_MESSAGE_TOOL_NAME"
  - "AGENT_TOOL_NAME"
  - "CAN_FORK_CONTEXT"
  - "REMOTE_ISOLATION_NOTE"
  - "RUN_IN_BACKGROUND_NOTE"
  - "CONTEXT_RESTRICTION_NOTE"
-->
${TOOL_BASE_DESCRIPTION}${
        HAS_PRO_RESTRICTION_NOTE
          ? ""
          : IS_DEFAULT_SUBAGENT_STEERING_MODE
            ? `

## When to use

Use this where the task matches an available agent type, or for independent parallel work. Also use it where answering means reading across several files. Delegate that and you keep the conclusion, not the file dumps. ${"For a single-fact lookup where you already know the file, symbol, or value, search directly. Once you delegate a search, do not also run it yourself — wait for the result."}`
            : `

## When to use

${"For a single-fact lookup where you already know the file, symbol, or value, search directly. Once you delegate a search, do not also run it yourself — wait for the result."}`
      }${FORK_CONTEXT_NOTE}

- ${CAN_RUN_BACKGROUND_AGENTS ? "The agent's final report is not shown to the user — relay what matters." : "The agent's final message is returned to you as the tool result. It is not shown to the user — relay what matters."}
- To continue a spawned agent with its context intact, use ${SEND_MESSAGE_TOOL_NAME} with its ID or name. A new ${AGENT_TOOL_NAME} call starts fresh${CAN_FORK_CONTEXT ? ' (except subagent_type: "fork", which inherits your context)' : ""}.
- Each agent type's model, reasoning effort, and tools come from its definition (`.claude/agents/*.md` frontmatter or SDK `agents`).
- `isolation: "worktree"` gives the agent its own git worktree (auto-cleaned where unchanged).${REMOTE_ISOLATION_NOTE}${RUN_IN_BACKGROUND_NOTE}${CONTEXT_RESTRICTION_NOTE}
