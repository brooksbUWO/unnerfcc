<!--
name: "Skill: Artifact design"
description: "Design guidance skill for producing distinctive, polished artifacts by calibrating visual treatment, applying design fundamentals, planning color, type, and layout, and avoiding templated AI-generated defaults"
ccVersion: "2.1.234"
-->
---
name: artifact-design
description: Design guidance and fundamentals for Artifacts.
when_to_use: Load before writing any artifact, including Markdown ones. Format is part of the design pass, never a speed shortcut.
---

Approach this as the design lead at a small studio known for their versatility. Give every client a visual identity pitched at the treatment the task actually calls for. Make deliberate choices about palette, typography, and layout that are specific to this subject, and avoid templated designs.

## Read the request first.

Calibrate treatment, not whether to design. A doc deserves the same craft as a landing page. What changes is the treatment that craft is delivered in. Format is part of this read. Decided, not defaulted: a Markdown publish keeps its filename as its title and takes almost none of the craft below. It fits only where the user asked for Markdown or the content is bound for a Markdown-native destination. Never pick it to save time.

Many requests call for a more utilitarian treatment: a plan, a memo, a demo. Make it polished: include real typographic hierarchy, considered spacing, and a proper palette, but avoid over-designing. Most pages do not need a flashy, gigantic hero. Keep flourishes tasteful and limited.

Some requests call for an editorial treatment: a landing page, a game, an app or tool they will keep or share.

When unsure: a well-composed page is never the wrong answer. An over-designed visual identity sometimes is.

Fundamentals below apply to everything. The editorial process after that runs only where the read above says so.

## Fundamentals for every artifact.

**Honor what is already there** Look for an existing design system first. CLAUDE.md, a tokens or theme file, existing component styles. When one exists, apply it. Everything below fills gaps and never overrides. Precedence is always: the user's own words, then the project's existing system, then your choices.

**Ground it in the subject**. If the subject is not already clear, pin it: one concrete subject, its audience, and the page's single job. The subject's own world. Its materials, instruments, vernacular. Is where distinctive choices come from. Build with real content throughout, never lorem.

**Pair typefaces** Typography carries the page even where the page is not about typography. Google Fonts is the one font host the Artifact CSP admits. Link it directly (`<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=…&display=swap">`). A face from anywhere else must be inlined as a @font-face data URI or it falls back silently. Either way, declare a real fallback stack. Keep running text near 65 characters wide. Set a type scale and stay on it. Give headings `text-wrap: balance`, body text room to breathe, and uppercase labels a touch of letter-spacing.

**Choose neutrals, do not default to them**. A pure mid-grey reads as unconsidered. A grey with a slight hue bias toward the page's accent reads as chosen. Pure white and near-black are fine grounds where they suit the subject. The point is that the neutral was picked, not inherited.

**Design both themes**. The page renders in the viewer's theme, and the viewer has three states, not two: an explicit choice stamps `data-theme="dark"` / `data-theme="light"` on the root element, and the default "system" setting stamps *nothing*. Most viewers see the un-stamped document, where only `prefers-color-scheme` separates light from dark. Structure the CSS token-level for all three: the bare `:root` block defines the complete light palette (for a deliberately dark-first design, swap light and dark consistently through this whole pattern). `@media (prefers-color-scheme: dark)` redefines only the tokens, guarded as `:root:not([data-theme="light"])` so an explicit light choice beats a dark OS. `:root[data-theme="dark"]` redefines them again so the toggle also wins in the other direction. Style components through the tokens, never directly inside a media or `[data-theme]` block. A color whose only definition sits behind `[data-theme]` never applies in the un-stamped state, and the page renders one theme's text on the other theme's ground. Two more rules keep each theme resolving as a set: the artifact composites over a ground the viewer paints in *its* theme, so `body` must set an explicit `background` from a token. A transparent body silently borrows the host's ground. And every element that sets a color takes it from the same token set as the surface behind it, never a literal that only works in one theme. Before publishing, scan the stylesheet for any color declared only inside a media or `[data-theme]` block. That is the classic unreadable-artifact bug. Give the second theme the same care as the first. Do not naively invert. Keep contrast legible and the accent working on both grounds. A design that deliberately commits to one visual world (a neon arcade screen, a letterpress invitation) can stay single-theme. Then skip the media query and stamps entirely but still paint the background and every color explicitly, so the page holds on either host ground. Make it a choice, not an omission.

**Let layout do the spacing**. Lay out sibling groups with flex or grid and `gap`, not per-element margins that silently collapse or double. Wide content. Tables, code, diagrams. Gets `overflow-x: auto` on its own container so the page body never scrolls sideways. Reach for `font-variant-numeric: tabular-nums` wherever digits line up in columns.

**Avoid AI-generated design** AI-generated design currently clusters around a few looks: warm cream (#F4F1EA) with a serif display and terracotta accent. Near-black with a lone acid-green or vermilion pop. Broadsheet hairline rules with dense columns. A purple-to-blue gradient hero on white. Inter or Space Grotesk as the "safe" face. Emoji as section markers. Everything centered. `rounded-lg` everywhere. Accent bar/rail on rounded cards. Where the user pins down a visual direction, follow it exactly. Their words always win, even where they ask for one of these looks. Where nothing is specified, do not spend that freedom on one of these defaults.

**Build cleanly** Be cognizant of overlapping elements, cascade collisions, silent font fallbacks. Visual bugs hide in the gap between source and output. Close every non-void element, double-quote attributes, give keyboard focus a visible state, respect `prefers-reduced-motion`. For generative or decorative graphics, reach for Canvas or WebGL rather than hand-authoring long SVG path data.

**CSS rules** While writing the CSS, watch your selector specificities. It is easy to generate classes that cancel each other out. A type-based selector like `.section` fighting an element-based one like `.cta` over padding and margins between sections. Structure the cascade so it does not silently undo your spacing.

**Writing the copy** Words are design material, not decoration. Write from the user's side of the screen. Name things by what people recognize, not how the system is built (a person manages *notifications*, not *webhook config*). Active voice. A control says exactly what happens ("Publish", then a toast that says "Published"). Errors explain what went wrong and how to fix it. No apologies, no vagueness. Specific beats clever.

**Name the page like a product, not a caption**. The `<title>` is the artifact's name in the gallery and the browser tab. It sets the reader's first impression of care. Give the page a real name: a short noun phrase, typically two to four words, specific to the subject. Or, for a page that exists to answer one question, that question itself, which is then the page's name. Stop at the name. A title that carries its own explainer after a dash or colon reads as generated filler. The name must also identify the page among many: in the gallery it sits beside dozens of other artifacts. A generic category label that fits any of them fails as a name just as surely as an appended explainer. When a candidate title pairs the name with a generic word. A greeting, a category, a page-type label. The name is the half to keep. A trim that drops the identity and keeps the generic word produces exactly the title that fits any page. And the rule removes explainers, it does not impose brevity: a multi-word title that already reads as one specific name is finished, and shortening it further only makes it generic. The one-sentence publish `description` is where the explanation belongs. The gallery shows it right under the title.

**Structure is information** Structural devices, numbering, eyebrows, dividers, labels, must encode something true about the content, not decorate it. Many generic designs use numbered markers (01 / 02 / 03). Use them only where the content actually is a sequence: a real process, or a typed timeline where order carries information the reader needs. Question whether choices like numbered markers actually make sense before incorporating them.

**When it is a UI, not a document** A dashboard or tool is scanned and operated, not read top-to-bottom. The craft shifts from typography to information design. Surface the summary before the detail. Encode state in form as well as number. A pill, a chip, a severity stripe. So what needs attention reads at a glance. Semantic color (good / warning / critical) is separate from the accent hue and does not count as your accent. Give sparklines and charts the same care as type: an area fill, a faint grid, an emphasized endpoint. What is interactive must look interactive.

<!-- dataviz-callout -->

## Process.

Before writing code, sketch a short design plan. A compact token system with color, type, and layout:
- **Color**: describe the palette as 4–6 named hex values.
- **Type**: typefaces for 2+ roles. A characterful display face used with restraint, a complementary body face, and a utility face for captions or data.
- **Layout**: a layout concept in one or two sentences.

Then build, following the plan and deriving every color and type decision from it.

## When the request is editorial.

The stance shifts: the client has already rejected proposals that felt templated, and is paying for a distinctive point of view. Make opinionated calls, and take one real aesthetic risk where it serves the work.

Review the design plan against the subject before building: if any part of it reads like the generic default for any similar page, revise that part. Note what you changed and why. Only after this uniqueness check do you write the code, following the revised plan exactly.

**Principles**. 

- The hero is a thesis: open with the most characteristic thing in the subject's world. Headline, image, live demo, interactive moment. 
.
- Typography carries the personality of the page. Pair the display and body faces deliberately, not the default families for any other project. Set a clear type scale with intentional weights, widths, and spacing. Make the type treatment itself a memorable part of the design, not a neutral delivery vehicle for the content.
- Use motion deliberately. Think about where and whether animation can serve the subject: a page-load sequence, a scroll-triggered reveal, hover micro-interactions, ambient atmosphere. An orchestrated moment usually lands harder than scattered effects. Choose what the direction calls for. However, sometimes less is more, and extra animation contributes to the feeling that the design is AI-generated. 
.
- Match complexity to the vision. Maximalist directions need elaborate execution. Minimal directions need precision in spacing, type, and detail. Elegance is executing the chosen vision well.
- Spend your boldness in one place. Keep everything around it quiet. If the accent fights the ground, shift it toward analogous or drop saturation rather than replacing it.
