<!--
name: "Skill: Artifact dashboard"
description: "Instructions for creating dashboard artifacts with KPI tiles, chart specifications, and breakdown tables from the built-in template"
ccVersion: "2.1.208"
-->
---
name: artifact-dashboard
description: Create a dashboard artifact. KPI tiles, a primary time-series chart, and a breakdown table. Use when the user asks for a dashboard, metrics view, KPI summary, monitoring page, or analytics overview. Also use to visualize quantitative data at a glance. Only for CREATING a new artifact. Edits to an existing artifact modify its HTML directly.
---

Base styling and reusable components for an operational dashboard: KPI tile cards, a spec-driven line-chart renderer, and table styles. These are arranged in a sensible default layout (KPI row, primary chart, breakdown table). The template sets the visual foundation. It does not fix the structure or content of the final dashboard.

## How to use.

1. Read `template.html` from this skill's base directory (listed above).
2. Copy it as your starting point. Replace each `<!-- SLOT: ... -->` marker with real content. The comment inside each slot describes what goes there. Remove the slot comments from the final output.
3. Then make the dashboard fit the data and the ask: add charts, reorder or drop sections, extend the layout grid. The `dataviz` skill is the right companion for richer or additional visualizations. The slots are where you start, not where you stop. Customization is key for data visualization. The card system, renderer, and table styles are components to build with. Keep the base styling so the result reads as one coherent design.
4. Self-check the result before publishing: no `SLOT` markers left, and no placeholder text or values left (see Notes).
5. Publish the filled HTML with the `Artifact` tool.

**Creation only**. When editing an existing dashboard artifact, work with its current HTML directly. Do not re-read or re-apply this template.

## Slots.

| Slot | What to fill in |
| --- | --- |
| `TITLE` | Plain-text page title, for example "Q2 Revenue Dashboard". |
| `KPI_TILES` | 2–5 `.card.kpi` blocks. One headline number each, with optional up/down delta. Color deltas by meaning, not direction (see Notes). |
| `PRIMARY_CHART_SPEC` | JSON spec inside `<script type="application/json" id="primary-chart-spec" data-chart-runtime>`. Supports `"type"`: line (default), bar, or donut. Multi-series specs get a legend, and optional axis captions and y-domain knobs are documented next to the slot. The `data-chart-runtime` attribute is load-bearing (publish-time chart injection keys on it. Keep it). Fill the spec for the standard cases. For other chart types or richer behavior, add your own chart alongside it. |
| `BREAKDOWN_ROWS` | Table header `<th>` cells and one `<tr>` per row. Add `class="num"` to right-align numeric columns. |
| `FOOTER_NOTE` | Data source and generation timestamp. |

The template also has a few minor inline slots (subtitle, chart title, breakdown title). Each is labelled in place.

## Notes.

- The template is a **body fragment**. No `<!DOCTYPE>`/`<html>`/`<head>`/`<body>` wrapper. The Artifact tool adds its own skeleton at publish time.
- The chart slot takes a JSON spec, not markup: you emit data + a few knobs. The template's `renderChart()` owns the pixels. Spec shape is documented inline next to the slot.
- **Replace every placeholder number. And never invent one**. Each placeholder value. KPI numbers, table rows, and the chart spec's zeroed "REPLACE ME" series. Must be replaced with real data, or its whole section removed. The same goes for dates and metadata: the footer's data source and generation date come from the conversation or are omitted, never made up. Published output must never contain placeholder or invented values.
- **No time dimension**? Do not fabricate a trend. Never invent a time axis for data that has none. Three good paths: use `"type": "bar"` or `"type": "donut"` in the chart spec where that shape fits (deterministic, preferred for standard shapes). Hand-draw your own SVG or HTML chart where the spec does not cover the shape, or for full visual control. The `dataviz` skill helps design it (reuse the card chrome and palette). Or drop the chart section and lead with the KPI tiles and breakdown table. Prefer `"line"` for anything that is a trend: it is the only spec type the page can still draw where the published page's chart runtime is unavailable. A hand-drawn SVG chart has no such dependency.
- **Format numbers for scanning**. KPI values get a unit and 2–3 significant figures with thousands separators (think $1.2M, 98.7%, 412ms). Percentages get at most one decimal. Keep the breakdown table to roughly the top ten rows and roll a long tail into an "Other" row.
- **Color deltas by meaning, not direction**. The `up`/`down` classes pick the arrow and default to green-up/red-down. When a decrease is the improvement. Latency, cost, error rate. Add the `good` (or `bad`) class so the color says whether the news is good.
- **Narrow ranges far from zero** (say, uptime hovering between 97% and 99%) flatten against the default zero-floored axis. Set `y.min`/`y.max` in the chart spec to zoom the domain. Mention the truncated axis in the chart title or footer so the zoom does not mislead.
- **The default styling is a starting point, not a house style**. The palette ships with a built-in dark mode. A follow-up styling/theming pass is encouraged. Tune `--accent` toward the subject (prefer another token from the shipped palette so the page stays on-system. Change it in every scope that declares it. The light `:root` block and both dark scopes. Or it snaps back in dark mode), adjust surfaces, or restyle entirely. When restyling or hand-drawing SVG charts, route colors through the CSS custom properties via `style` attributes. `var()` fails silently in bare SVG presentation attributes. Keep every custom color legible in both light and dark. Hardcoded near-black strokes vanish on the dark background.
