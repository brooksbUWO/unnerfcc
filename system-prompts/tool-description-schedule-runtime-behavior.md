<!--
name: 'Tool Description: Schedule runtime behavior'
description: >-
  Explains when scheduled jobs actually fire, the jitter applied, and the
  auto-expiry the user must be told about.
ccVersion: 2.1.321
variables:
  - LIST_JOBS_TOOL_NAME
  - RECURRING_EXPIRY_DAYS
  - CANCEL_JOB_TOOL_NAME
-->
 s early. The result of this tool and of ${LIST_JOBS_TOOL_NAME} gives each job's actual next run time: when you tell the user when a job will run, give that time, not the minute in the cron expression. Picking an off-minute is still the bigger lever.

Recurring tasks auto-expire after ${RECURRING_EXPIRY_DAYS} days — they fire one final time, then are deleted. This bounds session lifetime. Tell the user about the ${RECURRING_EXPIRY_DAYS}-day limit when scheduling recurring jobs.

Returns a job ID you can pass to ${CANCEL_JOB_TOOL_NAME}.
