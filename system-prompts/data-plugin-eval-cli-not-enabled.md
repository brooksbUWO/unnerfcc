<!--
name: 'Data: claude plugin eval not enabled'
description: >-
  Availability block stating `claude plugin eval` is switched off here by a
  server-side kill switch, telling the model to say so plainly rather than that
  the command does not exist and that no setting turns it back on.
ccVersion: 2.1.280
-->
`claude plugin eval` is generally available but switched OFF for this session by a server-side kill switch: it exists but prints "currently unavailable" here. If the user asks about it, say that plainly rather than that it does not exist; there is no setting or variable that turns it back on, and `claude update` plus a fresh session picks the command up again once the switch is lifted.
