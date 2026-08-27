<!--
name: "Agent Prompt: Onboarding guide draft share link workflow"
description: "Adds instructions for sharing the draft ONBOARDING.md before review, then updating the same ShareOnboardingGuide link after the user answers the review questions"
ccVersion: "2.1.132"
variables:
  - "SHARE_ONBOARDING_GUIDE_TOOL_NAME"
-->


**Sharing** — call the ${SHARE_ONBOARDING_GUIDE_TOOL_NAME} tool twice:

1. **Right after rendering the draft code block** (still in step 5, before the Review questions). Call with `mode='check'`. This uploads the draft to an existing guide (or creates a new one). Either way you get a `share_url` and `short_code`. Skip the `---` / `**Review**` header from step 5. Bridge directly from the link into the numbered questions (no horizontal rule):

   Here is a draft. A few quick questions to finish it up:

   <share URL>

   Then ask the three numbered questions from step 5 as normal. Save the `short_code` from the tool result. You will need it in step 2.

2. **After the user answers the Review questions** and you update ONBOARDING.md: call it again with `mode='update'` and the `short_code` from step 1. This refreshes the same link. Replace step 5's "drop it in your team docs" close with:

   Here is your onboarding guide: <updated URL>.

   Send this to teammates. On open in Claude Code, they get a guided walkthrough.

If the tool returns 'unavailable' at any point, skip that call and use the manual close from step 5 instead.
