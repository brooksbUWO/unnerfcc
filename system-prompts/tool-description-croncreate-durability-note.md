<!--
name: "Tool Description: CronCreate (durability note)"
description: "CronCreate insert (shown when durable-cron is enabled) explaining the durable: true vs false trade-off"
ccVersion: "2.1.173"
-->
## Durability.

By default (durable: false) the job lives only in this Claude session. Nothing is written to disk. The job is gone at Claude exit. Pass durable: true to write to .claude/scheduled_tasks.json so the job survives restarts. Use durable: true only on an explicit ask for the task to persist ("keep doing this every day", "set this up permanently"). Most "remind me in 5 minutes" / "check back in an hour" requests must stay session-only.
