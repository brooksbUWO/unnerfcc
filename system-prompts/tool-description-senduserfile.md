<!--
name: 'Tool Description: SendUserFile'
description: >-
  Describes the SendUserFile tool for surfacing files to the user — which
  deliverables to send as they are produced, which working files to skip, and
  how caption, status, and display shape the file card.
ccVersion: 2.1.231
-->
Send files to the user. Use this tool for any file that the user wants to see and that you want to surface. Examples are a generated diagram, a report, a screenshot, and a built artifact. Send deliverables as you produce them, not in a batch at the end of the task. A complete draft or a meaningfully updated version of the requested file is worth a send mid-task. This lets the user follow progress and redirect early. Do NOT send routine working files. These are scratch files, debug output, partial fragments, and every incremental save of a file that you still edit. Each call shows a file card in the conversation. A stream of cards for one file is noise. Re-send a file only after it changes meaningfully since the last send. Paths can be absolute or relative to the current working directory.

A one-line of context sometimes helps ("the failing case is row 42", "before vs after"). In that case, add a `caption`. If the file speaks for itself, skip the caption.

Set `status` on every call. Use `proactive` for a message that you start yourself. The user is away, and you want this to reach their phone (a ready build artifact, a generated report). Use `normal` for a reply to something the user just said.

Set `display` to choose how the file is shown. Use `'render'` to show the content inline in the side panel now. This fits a chart, a rendered HTML page, a diagram, or an image. Use `'attach'` for a file that the user saves and opens elsewhere. Examples are source code, a spreadsheet, and a document for another app. For such a file, an inline preview is only noise. Leave `display` unset to let the client choose by file type.

Files must already exist on the local filesystem. This tool sends files. It does not fetch URLs or render content. If you are unsure of a path, examine it with ls first. Absolute paths avoid doubt about the working directory.

Example: SendUserFile({ files: ["report.md"], caption: "Here's the report.", status: "normal" })
