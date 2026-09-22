<!--
name: 'Tool Result: Artifact type listing page unreadable with older pages'
description: >-
  Reports that no row on the newest page of a type's artifact listing could be
  read and that older pages exist, so the model should ask the user for the link
  or carry on without one.
ccVersion: 2.1.280
variables:
  - TYPE_NAME
-->
None of the rows on the one page this listing of Artifacts made from the type ${TYPE_NAME} reads (the newest) were readable, and there are more than that page: ask the user for the link if they have one in mind, else carry on without one.
