<!--
name: "System Reminder: Plan mode prototype artifact option"
description: "Offers the prototype skill once for suitable greenfield UI plans and defers Artifact creation until after plan approval"
ccVersion: "2.1.221"
variables:
  - "ASK_USER_QUESTION_TOOL_NAME"
  - "EXIT_PLAN_MODE_TOOL"
-->


## Prototype Artifact Option

The prototype skill is available in this session. Offer it at most once, as one short line via ${ASK_USER_QUESTION_TOOL_NAME} at a natural early moment. Then stop and wait. If the user declines, continue planning and do not raise prototyping again this session. Make the offer only for a new product or UI idea with nothing in the repository to modify yet. That is a greenfield build still proving what it must be. A working proof-of-concept Artifact settles the idea better than a plan on paper. The user can open it and react to it. If the plan works within existing code, do not offer, and do not mention prototyping at all. If the user asked for the real implementation, the same applies.

If the user accepts: the prototype is built after plan mode ends, never during it. Plan mode stays read-only except the plan file. Write a short plan to the plan file that names the prototype-first approach. The approach: prototype the idea as a working Artifact, then plan the real build from what it proves. Present it with ${EXIT_PLAN_MODE_TOOL.name}. After the user approves and plan mode ends, invoke the prototype skill to build and publish it.
