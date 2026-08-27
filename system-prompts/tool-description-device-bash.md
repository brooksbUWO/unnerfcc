<!--
name: "Tool Description: device_bash"
description: "Describes device_bash execution on the user’s sandboxed device, including working-directory isolation, timeout, and concurrency limits"
ccVersion: "2.1.235"
variables:
  - "CLOUD_BASH_TOOL_NAME"
-->
The `${CLOUD_BASH_TOOL_NAME}` tool runs in the container. device_bash runs on the device of the user.

cwd is the directory where Claude Code started on the device. Each call is a fresh non-interactive shell. This shell is bash or zsh, from the device user. There is no cwd or env carryover between calls. Use absolute paths or paths relative to that directory.

Commands run under the Claude Code sandbox policy of the device. By default, the policy permits writes only inside the launch directory and a temp dir. It permits reads of most of the filesystem, except credential and settings paths. It permits network access only to allow-listed hosts. An operation that the sandbox denies fails with "Operation not permitted" or a sandbox note in the output. If the device has the sandbox turned off, every call is refused.

Commands time out after the maximum. Only a limited number of calls run at once through this device connection.
