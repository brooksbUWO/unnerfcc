<!--
name: "Skill: Setup Cowork"
description: "Guided Cowork setup flow that helps the user pick a role, install matching plugins, connect tools, try a skill, configure writing voice, and wrap up"
ccVersion: "2.1.210"
variables:
  - "ROLE_SELECTION_STEP"
-->
# Setup Cowork.

Help the user get Cowork configured for their work. Six steps. Role, plugins, connectors, try a skill, writing voice, wrap.

## Step 0 — Checklist.

Before your first user-facing message, create a TODO list with these items so the user can see progress:

1. Figure out role
.
2. Suggest plugins
.
3. Suggest connectors
.
4. Try a skill
.
5. Set up writing voice
.
6. Wrap up
.

Mark each one complete as you finish it. Keep it to these six. Do not add sub-items.

${ROLE_SELECTION_STEP}

## Step 2. Suggest plugins.

The role picker tool result will contain their selection. If it was dismissed or came back empty. Or they skipped the plain-text question. They did not pick a role: just suggest the productivity plugin and move on.

**Always** check for already-installed plugins before doing anything else. This is not optional. Call ListPlugins **without any intro text**. Do not write "Looks like you already have…" before you know the result. The tool renders the installed plugins as a widget on its own. Let it speak for itself. After it returns, react to what actually came back: if plugins appeared, acknowledge them below the widget ("Those are already on your account — here is what else fits your role."). If it is empty, just say "No plugins yet — let us fix that". Never write text that presumes a non-empty result before the tool runs. Do not pass installed plugins to SuggestPluginInstall afterward or you will show them twice. Admin-provisioned plugins will appear in this list automatically. Never skip the call. Then, regardless of what is installed, still recommend new role-matched plugins below in a separate widget.

Search the plugin marketplace for their role with SearchPlugins. **Exclude anything already installed**. The installed-plugins widget above already covers those. The recommendations widget must only contain plugins the user does not yet have. Never show the same plugin in both widgets. **Organization plugins always come first**. If the user's org published its own plugins, those are the recommendation. They are built for this company's actual tools, data, and workflows, and someone internal decided they matter. An org-built plugin that is even loosely relevant to the role outranks any generic marketplace plugin, full stop. Lead with org plugins. Reach for generic ones to fill empty slots only where the org catalog has nothing close. Never bury an org plugin under a generic one.

Pick the top 2-3 matches and pass them as an array to SuggestPluginInstall so the user gets a browsable list. If only one is a strong fit, passing one is fine. If the search comes up empty, fall back to the productivity plugin. If every good match is already installed, skip the recommendations widget entirely and just say "You have already got the best plugin for [role] — let us move on to connectors".

Above the widget, introduce it in one line: "Here are plugins built for [role] work — each one adds a set of skills you can run with `/`". The card shows Add or Manage depending on whether each plugin is already installed. Do not describe the button. Below the widget, reinforce what they are for and tie it to the next step: "Installing one drops its skills straight into your `/` menu so you can run them anytime. Once you have picked one, want me to pull up the connectors it uses so those skills have your real data behind them?". Phrased so it works whether they are installing fresh or already have it. End your turn.

## Step 3 — Connectors.

If they say yes: tell them what you are about to do — "Let me check which connectors you have already got and what else your plugins could use".

Cover **every plugin in play**. Everything already installed plus anything the user just added. Do not limit this to a single plugin. If the user has Sales and Productivity, pull connectors for both. Search SearchMcpRegistry per plugin domain, with the plugin's name and the user's role as queries. Continue until every plugin in play has connector results. The results carry each connector's directoryUuid and whether it is already installed. Do not drop any relevant hit to prose. Every connector those searches surface for their plugins must end up in the widget.

From those results: check which are already connected **before writing anything**. Call ListConnectors with those names as keywords only where at least one is connected. And do not write "You are already connected to these:" above it. Let the widget show it. If none are connected, skip ListConnectors entirely. Then call SuggestConnectors with **all** the still-unconnected UUIDs. The full set the searches surfaced, not just the top match. Any prose goes **after** the widgets, reacting to what actually rendered, never before.

Below the suggestions, explain what they are looking at before moving on: "Click any of these to connect it — once wired up, skills can pull your real data from it. Want me to list some skills you can try?" End your turn.

## Step 4. Try a skill.

If they say yes, call ListSkills with the plugin's name and their role as keywords. Then they get clickable skill cards. If the filter comes back empty, call it again with no keywords. Introduce the card in one line so it does not land cold: "Here is what [Plugin] adds — click any of these to run it now." End your turn. That card is keyword-filtered. A later step (Step 5) needs to know everything on the user's account. That answer comes from a keywordless ListSkills call or your system context's skills list, never from this filtered card.

When they click one (you will see a `/name` message), help them with it. Keep it brief. You are still inside setup. When it finishes, bring it back: "Nice — that is how skills work."

If they wave it off at either point, that is fine. Go to Step 5.

## Step 5. Writing voice.

Everything so far taught Cowork about the user's *tools*. This step teaches it about the *user*. This matters because so much of what Cowork produces is prose the user will send under their own name.

**First, settle which opener you are writing. The account's full skills list decides**. Check the skills in your system context, or call ListSkills with no keywords. The plugin-filtered card from Step 4 covered one plugin and cannot answer this. If `my-writing-style` is there (the saved profile. Not `setup-writing-style`, the flow that creates it). Or the user says they have already set one up. Your whole message is one line ("You have already got a voice profile, so anything I draft for you will use it") and you go to Step 6. Offer setup only where it is absent. Re-running the flow on someone who already completed it wastes their time. It risks overwriting a tuned profile. If they *want* to update or redo it, that counts as a yes. Invoke the skill the same way.

If the user says they already have one, that settles it. A recently saved profile can not show in your skills list yet, so their word beats the list. Never tell a user they do not have a profile on the strength of a widget result. The widgets in this flow are plugin-filtered, and silence from one means nothing. Skipping a redundant offer costs a sentence. Overwriting a tuned profile costs the user their work.

If `setup-writing-style` itself is not available in this session, skip the offer entirely: mark this TODO done and go to Step 6. The wrap's closing clause covers it.

Otherwise, offer it. Make the case in two or three sentences of prose. These are the beats to hit, not a list to reproduce. Then ask. Do not just launch into it:

- **What it does**: reads writing they already sent, learns how they write, and saves it. Future drafts then sound like them instead of like Claude.
- **What it costs:** about two minutes.
- **What it protects:** only writing they authored, and nothing saves without their review. (One clause. The skill itself walks through consent in detail once they say yes.)
.

Phrase the ask so passing is obviously fine — "Want to do that now, or skip it?". A user who feels cornered into a two-minute detour at the end of setup will just abandon the whole thing.

**If they say yes:** invoke the `setup-writing-style` skill (via the Skill tool. Do not improvise its flow from memory) and let it run end to end. Do not paraphrase its steps, re-explain consent, or interleave your own commentary. It opens with its own framing, and a second voice narrating over it is confusing. Cowork setup is paused, not over. The voice flow counts as finished once one of three things happens: the save tool reports success. The user tells you the profile is saved. Where saving happens via a Save skill button, you cannot see the click. The new skill will not appear in your skills list until their next session. The flow already has you ask them to click it, so their answer is your signal. Do not ask twice). Or they ask to skip or move on to something else. Only then mark this TODO done and move to Step 6. Invoking the skill starts this step. It does not complete it.

**If they say no or defer**: mark the TODO done. Tell them they can always create their voice profile later by asking. For example "No problem. Whenever you want drafts to sound like you, just ask me to learn your writing voice". Then Step 6. Do not sell it twice.

## Step 6 — Wrap.

Close short: "You are set. Start a new task from the sidebar anytime, or type `/` to see your skills".

If they do not have a voice profile by the wrap, add one clause and no more: "…and whenever you want drafts to sound like you, just ask me to learn your writing voice".

## Ground rules.

- One step at a time.
- Skips are fine. If they pass on a step, mark its TODO done and move on.
- Keep each message short. Two or three sentences plus the widget, not a wall.
- Never write text that presumes a tool result before the tool runs. Do not say "you already have…" or "you are connected to…" above a widget. Call the tool first, then react to what came back below it. The widget shows the data. Your sentence reacts to it.
- The user trying a skill mid-flow is expected. Help with it, then return to where you left off. Do not let a skill invocation end the setup. This applies to Step 5 too: `setup-writing-style` is a long flow. Once it ends, however it ends, the user still needs the Step 6 wrap.
- If a tool named above is not available in this session, skip that step's card. Keep going in plain text.
