<!--
name: Agent Proxy Environment Note
description: >-
  Concise agent-proxy/TLS guidance injected into the <env> 'useful information
  about the environment' context block the model reads, now also covering
  cut-off transfers and never disabling TLS verification or unsetting
  HTTPS_PROXY.
ccVersion: 2.1.257
variables:
  - AGENT_PROXY_CA_BUNDLE_PATH
  - STATUS_CHECK_PREFIX_CLAUSE
  - TRAILING_PROXY_NOTE
-->
Outbound HTTPS goes through a pre-configured agent proxy (CA bundle: ${AGENT_PROXY_CA_BUNDLE_PATH}). If a tool fails TLS verification, gets 403/405/407 from the proxy, or a transfer is cut off (connection reset, unexpected disconnect, RPC failed), ${STATUS_CHECK_PREFIX_CLAUSE}run curl -sS "$HTTPS_PROXY/__agentproxy/status" for per-tool fixes and proxy state; never disable TLS verification or unset HTTPS_PROXY.${TRAILING_PROXY_NOTE}
