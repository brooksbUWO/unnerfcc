<!--
name: "Skill: Artifact components"
description: "Catalogs reusable Artifact components and supplies the exact scripts, styles, tokens, markup contract, and composition limits for embedding interactive decision blocks"
ccVersion: "2.1.234"
-->
---
name: artifact-components
description: "Embed reusable artifact components in any HTML artifact — first entry: the workshop decision component (clickable option rows backed by a machine-readable record the session reads back). Use when a non-workshop artifact must carry decisions the reader answers from the published page. Also use to look up a component's exact scripts, styles, markup contract, and composition limits. Read this before embedding."
---

Catalog of components an HTML artifact can embed. Each entry ships the exact
bytes the publish verifier holds a carrying page to: fixed scripts, carved
styles, and a markup skeleton with its invariants stated at each slot.

**Composition limits (today)**. Two independent constraints:

1. **Script pinning under the workshop record name**. A page carrying the
   ws-decisions island is held to full workshop-page rules: every executable
   script must hash-match the blessed set, so any custom script. Including a
   custom element implementing this same component. Refuses as
   `script-not-blessed` (and a non-workshop island schema under that id
   refuses as `island-grammar`).
2. **One JSON island per such page**. The verifier admits exactly one JSON
   script element — the ws-decisions island. And refuses any other as
   `unknown-data-island`, even where the other component's executable scripts
   are individually blessed. (A decision page plus a chart-spec island refuses
   on the island, not the scripts).

**The escape hatch and its cost**: a component using its OWN island id (not
the workshop's) publishes in the ordinary author-HTML lane. There custom
scripts are allowed and neither constraint applies. But the session's
`read_page_data` workshop-decisions schema does not read such an island. So
decisions recorded there need their own read-back path. A script in that
lane that writes reader-typed text into its island must never splice the
raw string: `</` inside a JSON string value ends the script element and
executes what follows for every later viewer. Encode free text (the pinned
decisions script stores it as canonical base64). Or refuse the write where
the serialized island contains `<`, `>`, `&`, `'`, or a backslash, like the
pinned script. Compose by choosing
one island-bearing component per verified page, or by leaving the verified
lane entirely.

## Decision component (from the workshop skill).

Option rows the reader clicks on the published page. Picks accumulate in a
sticky footer whose single Confirm republishes the page with the choices
recorded in the ws-decisions island. The session reads them back with the
Artifact tool's `read_page_data` action (schema `workshop-decisions`).
Any author-HTML page carrying the island is held to FULL workshop-page rules
at publish. Embedding in a non-workshop artifact is sanctioned. Deviation
refuses with a named rule.

Files in this skill's `decision/` directory:

- `skeleton.html` — fill-in markup for one decision plus its island entry,
  invariants noted per slot. Start here.
- `theme-script.html` and `decisions-script.html`. The two fixed script
  elements, copied byte-identical from the workshop-page template. The
  publish allowlist admits inline scripts by sha256 of the script element's
  text content. The shipped blocks hash to
  `cc92acd07b10a4a892834a8661cb4a69a299224a830e01b1e68f2b29c1c0c15b` (theme) and
  `08eafa73e8186c16026df60706aee612fc18689696a638759098aaa70834379d` (decisions).
  Never edit, reindent, or reformat them. Any byte difference refuses as
  `script-not-blessed`. The publish verifier's blessed set is the source of
  truth for these hashes. The literals here are documentation, held to the
  template by this skill's pin tests.
- `component.css` — the component's presentation rules, carved verbatim from
  the workshop-page template. Requires these CDS custom properties (embed
  `tokens.css` below, or define them yourself): `--border`,
  `--border-strong`, `--border-stronger`, `--fill-accent`,
  `--fill-control`, `--gap-md`, `--gap-sm`, `--gap-xs`, `--page-bg`,
  `--radius`, `--shadow-sm`, `--surface-0`, `--text-accent`,
  `--text-primary`, `--text-secondary`.
- `tokens.css` — the template's vendored CDS token block, carved verbatim
  and drift-pinned like the scripts. It defines all of the above plus the
  palette and dark-mode overrides they reference. Embed once, before
  `component.css`.

## How to embed.

1. Read the files above from this skill's base directory.
2. Build the page: `theme-script.html` early in the head, right after
   `<title>`. It mirrors the stored theme to `data-mode` before first
   paint (the template ships it there). `tokens.css` then `component.css`
   with your own styles. One filled `skeleton.html` block per decision. The
   island (one per page, entries in lockstep with the markup). Then
   `decisions-script.html`, unmodified, last.
3. Publish with `capabilities: {"artifact": {}}` so readers can decide from the
   page. Without it the page still publishes and renders. Rows stay inert
   with an explanatory tooltip.
4. Read decisions back with `read_page_data`. Apply them and republish.

Rules that bite during hand-assembly:
full workshop-page rules refuse `<link>`, `<form>`, `<iframe>`,
`<object>`, `<embed>`, `<base>`, `<noscript>`, `<frameset>`/`<frame>`.
They also refuse every `on*` event-handler attribute, `ping` and
`referrerpolicy` attributes, and an `opener` token in `rel`. Anchor
`target`s other than `_blank`/`_self` are refused too. A retrofitted host
page gives those features up.
The island's `id` attribute spelling can appear nowhere else in the page
bytes, prose included (refuses as `island-sentinel-ambiguity`). A banner
element carrying `data-ws-state` must match the island-derived state. Any
open decision derives `in-progress` (refuses as `banner-state-mismatch`).
The decision id
`get-started` is reserved for the kickoff block, never an ordinary
decision. This is largely unenforced at publish. A misused one renders wrong.
Option-row CLASSES (`option`, `option-label`, `badge`, `why`,
`custom-answer`, `option-input`) are not verifier-enforced. But the decisions
script and CSS key on them. Drift breaks the UI silently, so copy the
skeleton rather than retype it. `component.css`'s selectors are not scoped
to the component: it styles generic page-wide class names, and those are reserved (`option`,
`options`, `call-item`, `call-body`, `custom-answer`, `option-input`,
`confirm-btn`, `clear-btn`, `confirm-hint`, `footer-note`, `note-live`).
A host page reusing one for its own elements gets silently restyled. The sticky footer's left padding assumes a centered 76ch content
column (the workshop layout). In a host page with a different column the
Confirm button still works but will not align with the content.
