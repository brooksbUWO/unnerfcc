<!--
name: "Tool Parameter: matched ask rule"
description: "Describes metadata identifying a user-configured permissions.ask rule that forced a tool approval prompt while preserving the tool-authored decision reason"
ccVersion: "2.1.213"
-->
Set when a user-configured ask RULE (permissions.ask) forced this prompt but the ask carries the tool's own decision_reason. The ask-rule substitution keeps the richer tool-minted ask, so the rule rides here instead of decision_reason_type 'rule'. Hosts that make policy on decision_reason_type (for example auto-deny safetyCheck) must treat asks with this field as rule-forced. So must hosts that run host-side auto-approval. The user's stated intent is a human prompt. Values are producer-authored but render-unsafe like decision_reason. Sanitize before display.
