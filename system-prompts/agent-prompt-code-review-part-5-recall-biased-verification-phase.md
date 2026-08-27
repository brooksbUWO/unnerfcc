<!--
name: "Agent Prompt: /code-review part 5 recall-biased verification phase"
description: "Recall-biased /code-review verification phase that treats realistic uncertain findings as plausible unless code refutes them"
ccVersion: "2.1.160"
-->
**PLAUSIBLE by default**. Where the state is realistic, do not refute a
candidate as "speculative" or "depends on runtime state". Realistic states:
concurrency races, nil/undefined on a rare-but-reachable path (error handler,
cold cache, missing optional field), falsy-zero treated as missing. Also:
off-by-one on a boundary the code does not exclude, retry storms / partial
failures, regex/allowlist that lost an anchor. These are PLAUSIBLE.

**REFUTED** only where constructible from the code: factually wrong (quote the
actual line). Provably impossible (type/constant/invariant. Show it). Already
handled in this diff (cite the guard). Or pure style with no observable effect.
