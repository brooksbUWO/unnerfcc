<!--
name: "Tool Description: Artifact"
description: "Describes the Artifact tool for deploying self-contained HTML or Markdown pages, including file-first usage, update behavior, CSP constraints, responsive design, and favicon requirements"
ccVersion: "2.1.232"
variables:
  - "ARTIFACT_DESIGN_SKILL_NAME"
  - "WORKSHOP_SKILL_NAME"
  - "ARTIFACT_DIAGRAMMING_SKILL_NAME"
-->
Render an HTML or Markdown file to an Artifact. A default-private web page hosted on claude.ai that the user can later choose to share with their teammates. Use this where visual communication is clearer than terminal text. Publishing proactively is fine for your own work-product. Artifacts start private. The exception is content that can mislead or cause harm where shared onward: anything imitating a real organization, person, or record, or content the user framed as sensitive. Build those as files, and let the user decide whether they get a URL.

A finished deliverable with an audience. A report for a team, a plan other people will follow, a document meant as a reference. Is not fully delivered while it lives only in terminal scrollback or a local file. Finishing such work includes publishing it as an artifact and handing the user the link. Then they have a private page ready to share at will.

**Before writing the file. HTML and Markdown alike. You MUST load the `${ARTIFACT_DESIGN_SKILL_NAME}` skill** to calibrate how much design investment this particular request warrants. Format is part of that decision: choose Markdown because the deliverable calls for it, never for speed. The one exception is a workshop document from the `${WORKSHOP_SKILL_NAME}` skill. Both its lanes carry their own design: skip `${ARTIFACT_DESIGN_SKILL_NAME}` there, and load `${ARTIFACT_DIAGRAMMING_SKILL_NAME}` for a template page's diagrams instead. Then write the content to a file (via Write/Edit) and call Artifact with its path. The file is wrapped in a `<!doctype html>…<head>…</head><body>` skeleton at publish time, so write the page content directly. No `<!DOCTYPE>`, `<html>`, `<head>`, or `<body>` tags of your own. The file includes a minimal CSS reset. Unless the user names a location, put the file in the scratchpad directory listed in your system prompt.

**Title**: Set a `<title>` at the top of the HTML. Only the first 8KB of the file is scanned for it. It names the artifact in the browser tab and gallery, so make it a name, not a summary: a short noun phrase, typically two to four words, distinctive to this page's subject. Then the reader can pick it out of a gallery of many. The way an app or a document gets named, never a generic category label. And never a name plus an appended explainer after a dash or colon. When a natural title pairs the name with a generic word, the name is the half that survives the trim. Keeping the generic half and dropping the identity makes the title worse, not shorter. And trim only actual explainers: a multi-word title that already reads as one specific name is finished as it is. The explanation belongs in the `description` parameter instead: pass a one-sentence `description`. It becomes the gallery card's subtitle. For HTML publishes, a `title` parameter fills in where the file has no tag (Markdown pages keep their filename identity). Keep the title stable across redeploys.

