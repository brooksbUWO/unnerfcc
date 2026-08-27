<!--
name: "Skill: Data Visualization"
description: "Skill instructions for producing accessible, brand-neutral charts, graphs, dashboards, and data visualizations using a validated method"
ccVersion: "2.1.210"
-->
---
name: Data Visualization
description: >
  Produce a chart, graph, dashboard, or any data visualization that reads as one
  system. Make it elegant, accessible, consistent in light and dark, and
  BRAND-NEUTRAL. It ships a placeholder palette to swap for your own. Read
  this BEFORE you generate ANY chart (bar, line, area, heatmap, scatter,
  sparkline, donut). Also read it before you choose chart colors or build a
  stat tile / meter / KPI row. And before you lay out a dashboard. Teaches a design-system-AGNOSTIC method: a form
  heuristic, a color formula with a runnable check script, mark specs, and interaction
  rules. The method is invariant. A design system plugs in its own ramps and
  surfaces. A pre-checked default palette is documented in `references/palette.md`
  — swap that file's values for your brand's. Triggers on: "chart", "graph", "plot", "data viz", "dashboard",
  "analytics", "visualize data", "categorical colors", "sequential / diverging
  palette", "stat tile", "sparkline", "heatmap", "legend", "axis", "tooltip",
  "chart colors", "color by series".
---

# Data Visualization.

A chart is **read by people and executed by you**. This skill turns "make it look
good" into a procedure with checks. Thus the result is right by construction rather
than by taste.

**The method here is design-system-agnostic**. Nothing in the procedure, the form
heuristic, the six checks, or the mark specs is specific to one product. A design
system supplies a small set of *parameters*. Examples: its ramps, a categorical
order, a diverging pair, a status palette, a texture, its surfaces, its filter
components. The method consumes them unchanged. A **pre-checked default palette** is the
reference instance, fully specified in `references/palette.md`. To target your
brand, read that file's structure and substitute its values. Touch nothing else.

> The single most important habit: **the color part is computable, so compute it**.
> Never eyeball whether a palette is colorblind-safe. Run `scripts/validate_palette.js`.

## The procedure. Do these in order.

Color comes LAST. Most bad charts pick colors first.

1. **Pick the form**. What is the data's job. Magnitude, identity, polarity, a
   single headline, change-over-time? The job picks the chart type, and sometimes
   the answer is *not a chart* (a stat tile or hero number). → `references/choosing-a-form.md`.
2. **Assign color by the job it does**. Categorical (identity), sequential
   (magnitude), diverging (polarity), or status (state). Each has one rule.
   Assign categorical hues in fixed order, never cycled. → `references/color-formula.md`.
3. **CHECK the palette. Run the script, do not reason about ΔE**.
   `node scripts/validate_palette.js "<hex,hex,…>" --mode light` (relative to
   this skill's base directory. Or load it as `<script type="module">` in the
   chart's own page. There it reads
   `data-palette` off `<body>` and logs a `console.table` report). It returns
   pass/fail on the lightness band, chroma floor, adjacent-pair CVD separation,
   the normal-vision floor, and contrast. Fix anything that FAILs before continuing. Re-run for
   `--mode dark` with that mode's surface.
4. **Apply mark specs & spacers**. Thin marks, 4px rounded data-ends anchored to
   the baseline, 2px lines, ≥8px markers. Add a 2px surface gap between fills (stacked
   segments and adjacent bars alike) and a 2px ring on overlapping marks.
   Use selective direct labels. → `references/marks-and-anatomy.md`.
5. **Add the hover layer. By default**. An HTML/SVG chart *is* interactive. Ship
   a crosshair+tooltip on line/area and a per-mark hover tooltip on bar/dot/cell.
   The only form that skips it is a bare stat tile with no plot. Hit targets bigger
   than the mark. Filters in one row above the charts. → `references/interaction.md`.
6. **Final accessibility pass**. For ≥ 2 series a legend is always present, and ≤ 4
   are also direct-labeled. Thus identity is never color-alone (a single
   series needs no legend box. The title names it). A table view exists. Dark mode is **selected**. Its own
   steps from the same ramps, checked against the dark surface, not an automatic
   flip. Texture is available for the CVD/print/forced-colors case.
7. **Render it and look at it**. The check script covers color, not layout. Open or
   screenshot the output and eyeball it for label collisions, geometry, and overflow
   before calling it done.

Then check the result against **`references/anti-patterns.md`**. It is the catalog
of what goes wrong. If your chart matches an entry, it is wrong.

## Non-negotiables (true in every design system).

- **Assign categorical hues in fixed order, never cycled**. A 9th series is never a
  generated hue — it folds into "Other," small multiples, or composite encoding.
- **One axis**. Never a dual-axis chart (two y-scales). Two measures of different
  scale → two charts, small multiples, or indexed to a common base. *(This is the.
  #1 chart mistake. See anti-patterns.)*
- **Color follows the entity, never its rank**. A filter that changes the series
  count must not repaint the survivors.
- **Sequential = one hue, light→dark. Diverging = two hues + a neutral gray
  midpoint**. Never a rainbow. Never a hue at the diverging midpoint.
- **Run the check script before shipping any categorical palette**. CVD ΔE ≥ 8 is the
  target (OKLab ×100). 6–8 is a floor that is legal ONLY with secondary encoding. A
  normal-vision floor below 15 is a hard FAIL. Full-color readers cannot tell the
  pair apart. Re-step it on the adjacent pairlist (secondary encoding does not excuse
  this one). Under `--pairs all` cut series or facet instead. See check 4. A contrast WARN
  obligates visible labels or a table view. It is not dismissable.
- **Thin marks. A legend always present for ≥ 2 series (none for one). Add
  selective direct labels (never a number on every point). Recessive grid/axes**.
- **Text wears text tokens, never the series color**. Values, labels, and legends
  stay in primary/secondary/muted ink. A colored mark beside them carries identity.
- **Status colors are reserved** (good/warning/serious/critical) and never reused
  for "series 4". They ship with an icon + label, never color alone.

## Plugging in a design system.

The method is invariant. Only these parameters change per system. The reference
instance — every value filled in. Is `references/palette.md`.

| Parameter | What the system provides |
|---|---|
| **Ramps** | the hue scales (named steps) the palette draws from |
| **Categorical theme** | the fixed hue order (a named theme). Default + alternates |
| **Sequential hue** | the default single hue for magnitude |
| **Diverging pair** | two warm/cool poles + a neutral midpoint |
| **Status palette** | good / warning / serious / critical. Steps distinct from categorical |
| **Texture fill** | one directional hand-drawn fill, used at 45° / 135° |
| **Surfaces** | light & dark chart-surface colors (the validator needs these) |
| **Filter controls** | date-range & dimension controls (behavioral spec in `interaction.md`) |

To onboard a new system: fill those rows and feed its ramps to the check script. Let
it snap each slot to the nearest passing step. Structure and rules stay as written.

## Reference files.

| File | What it answers |
|------|-----------------|
| `references/choosing-a-form.md` | Which chart type / is it even a chart? |
| `references/color-formula.md` | The four jobs, the six checks, snap-to-passing |
| `references/marks-and-anatomy.md` | Mark specs, spacers, labels, figures, hero number |
| `references/interaction.md` | Tooltips & hover, filters & time ranges |
| `references/components.md` | The pieces a chart is made of. Build each in plain HTML |
| `references/anti-patterns.md` | **What goes wrong. Check every chart against this** |
| `references/palette.md` | **The reference palette instance**. Every parameter, filled in. Swap for your brand's |
| `scripts/validate_palette.js` | Runnable six-checks validator (run it. Do not eyeball) |
