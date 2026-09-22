<!--
name: 'Tool Result: Remote output file location'
description: >-
  Notes that the command's full output was saved to a file on the attached
  machine that cannot be read from here, and to re-run the command there with
  head, tail or grep.
ccVersion: 2.1.280
variables:
  - MACHINE_NAME
  - READ_INSTRUCTION
-->
(the full output was saved to a file on ${MACHINE_NAME} that was not sent and cannot be read from here — re-run the command there with head, tail or grep if that is safe, ${READ_INSTRUCTION})
