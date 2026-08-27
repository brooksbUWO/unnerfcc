<!--
name: "System Reminder: Large PDF read guidance"
description: "Warns that a PDF is too large to read at once and requires reading specific page ranges"
ccVersion: "2.1.234"
variables:
  - "ESCAPE_UNTRUSTED_TEXT_FN"
  - "PDF_FILE_REFERENCE"
  - "FORMAT_FILE_SIZE_FN"
  - "READ_TOOL_NAME"
-->
PDF file: ${ESCAPE_UNTRUSTED_TEXT_FN(PDF_FILE_REFERENCE.filename)} (${PDF_FILE_REFERENCE.pageCount} pages, ${FORMAT_FILE_SIZE_FN(PDF_FILE_REFERENCE.fileSize)}). This PDF is too large to read at once. Use the ${READ_TOOL_NAME} tool with the pages parameter to read specific page ranges (for example, pages: "1-5"). A ${READ_TOOL_NAME} call without the pages parameter fails. Read the first few pages to understand the structure, then read more as needed. Maximum 20 pages per request.
