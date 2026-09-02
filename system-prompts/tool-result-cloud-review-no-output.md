<!--
name: 'Tool Result: Cloud review produced no output'
description: >-
  Tells the model the cloud review returned nothing and to have the user retry
  /code-review ultra or fall back to a plain local /code-review.
ccVersion: 2.1.257
variables:
  - CLOUD_REVIEW_FAILURE_REASON
  - TRAILING_DETAIL_CLAUSE
  - TRAILING_HINT_CLAUSE
-->

Cloud review did not produce output (${CLOUD_REVIEW_FAILURE_REASON}). Tell the user to retry /code-review ultra, or use plain /code-review for a local review instead.${TRAILING_DETAIL_CLAUSE}${TRAILING_HINT_CLAUSE}
