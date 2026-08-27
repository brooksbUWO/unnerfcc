<!--
name: "Skill: Run CLI tool example"
description: "Example file for the Run app skill showing how to document building, invoking, and testing a CLI tool"
ccVersion: "2.1.145"
-->
# Example: CLI tool.

CLIs are the simplest case. There is usually no background process to
manage, no ports, no lifecycle. The skill focuses on **installation**,
**representative invocations**, and **testing**.

## What matters.

- **How to get the binary on `PATH`**. Installed globally? Run via
  `npx`/`uv run`? Built to `./target/release/foo`? Be explicit.
- **Two or three example invocations** that cover the main use cases.
  Include expected output so a reader can tell it worked.
- **Exit codes**, where meaningful (for example linter returns 1 on findings).
- **Stdin behavior**, for a tool that reads from stdin.

## Example snippet.

> ---
> name: run-mytool
> description: Build, install, and run mytool. Use when asked to run mytool, test it, or verify it is installed correctly.
> ---
> 
> ## Setup.
> 
> ```bash
> pip install -e .
> ```
> 
> This puts `mytool` on PATH. Verify:
> 
> ```bash
> mytool --version
> # → mytool 0.3.1
> ```
> 
> ## Run.
> 
> Process a single file:
> 
> ```bash
> mytool process input.json
> # → Processed 42 records, wrote output.json
> ```
> 
> Read from stdin, write to stdout:
> 
> ```bash
> cat input.json | mytool process -
> ```
> 
> Lint a directory (exits non-zero on problems):
> 
> ```bash
> mytool lint ./src
> echo $?  # 0 if clean, 1 if issues found
> ```
> 
> ## Test.
> 
> ```bash
> pytest
> ```

## Keep it short.

A CLI's run skill can be very compact. Do not pad it with every flag —
the `--help` output covers that. Just show enough that an agent can
(a) build it, (b) verify it works, (c) run the tests.
