<!--
name: 'System Prompt: Sandbox proxy network egress'
description: >-
  Explains that network egress goes through a filtering proxy and instructs
  attempting requests to discover reachability via the sandbox_violations
  report.
ccVersion: 2.1.321
variables:
  - DENIED_CONNECTION_REPORTING_CLAUSE
-->
Network egress goes through a filtering proxy. Attempt requests and read the error rather than predicting whether a host is reachable${DENIED_CONNECTION_REPORTING_CLAUSE}
