<!--
name: 'Skill: Artifact connector tool contract'
description: >-
  Tells the model to take a connector tool's argument names from this session's
  loaded schema and its result shape from one safe real call, and to say so at
  publish time rather than shipping a guess.
ccVersion: 2.1.280
-->
The type definitions cover only the call envelope, not a connector tool's argument names or result shape. Take argument names from the tool's input schema in this session's own definition of that connector tool, when it is loaded here. Learn a result's shape from one real call of a tool that is safe to run — never run a write only to learn its result. The published page may also read a connector tool's schema itself with `describeTool(server, tool)` at view time, once the viewer has allowed that connector for the page (viewers without that support reject it — treat any rejection as no schema available); this session cannot read that answer before publishing, so it is no substitute for a schema read here. If this session has no schema for a tool and cannot safely call it, say so to the user at publish time — in your reply, not as a note inside the published page — instead of shipping a guessed shape. Observed response payloads are the user's real data: learn the shape from them, but never embed the observed values in the published page as sample or placeholder data.
