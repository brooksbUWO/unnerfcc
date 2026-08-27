<!--
name: "Skill: Code Review (Angle B — removed-behavior auditor)"
description: "Code-review finder angle that, for each deleted or rewritten line, names the behavior it guaranteed and confirms the new code still guarantees it"
ccVersion: "2.1.173"
-->
### Angle B. Removed-behavior auditor.

For every line the diff DELETES or replaces, name the invariant or behavior it
enforced. Then search the new code for where that invariant is re-established.
If you cannot find it, that is a candidate: a removed guard, a dropped error
path, a narrowed validation, a deleted test that was covering a real case.
