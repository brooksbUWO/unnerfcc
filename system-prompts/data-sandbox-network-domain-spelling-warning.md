<!--
name: "Data: Sandbox network domain spelling warning"
description: "Formats the sandbox diagnostic for unreliable network domain spellings and explains conservative enforcement until entries are corrected"
ccVersion: "2.1.229"
variables:
  - "FORMAT_SANDBOX_DOMAIN_WARNINGS_FN"
  - "SANDBOX_DOMAIN_WARNINGS"
-->
Found: ${FORMAT_SANDBOX_DOMAIN_WARNINGS_FN(SANDBOX_DOMAIN_WARNINGS)}. IPv6 literals must be bracketed, with any port 1-65535 and no leading zeros ("[::1]", "[::1]:443"). Non-IPv6 entries must not contain wildcards in brackets, extra colons, "@", or path/query characters, and must use their canonical spelling (lowercase, no trailing dot, punycode). Until fixed, enforcement is conservative: a denied entry denies at least what any parseable reading denies (an entry with no parseable reading denies nothing). An allowed entry never allows more than written and can be removed entirely. Bracketed IPv6-glob entries apply to in-process checks only, not the sandbox proxy.
