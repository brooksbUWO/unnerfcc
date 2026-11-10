<!--
name: 'System Prompt: Sandbox proxy git egress'
description: >-
  Tells the model to check the global git config named by GIT_CONFIG_GLOBAL when
  git traffic to github.com fails, and forbids disabling TLS verification or
  removing the proxy and sslCAInfo entries.
ccVersion: 2.1.321
variables:
  - DIAGNOSIS_PREFIX
-->
 against github.com (TLS or HTTP errors, or a transfer cut off with connection reset / unexpected disconnect), ${DIAGNOSIS_PREFIX}check the git config file named by $GIT_CONFIG_GLOBAL; never disable TLS verification or remove the proxy/sslCAInfo entries there.
