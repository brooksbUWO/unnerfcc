<!--
name: "Tool Description: Bash (prefer dedicated tools)"
description: "Warning to prefer dedicated tools over Bash for find, grep, cat, etc."
ccVersion: "2.1.71"
variables:
  - "READ_ONLY_SEARCHING_BASH_COMMANDS"
-->
IMPORTANT: Do not use this tool to run ${READ_ONLY_SEARCHING_BASH_COMMANDS} commands. There are two exceptions. The user gives you an explicit instruction to do so. Or you make sure first that no dedicated tool can do your task. In all other cases, use the correct dedicated tool. A dedicated tool gives a much better experience for the user:
