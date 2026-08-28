<!--
name: tool-description-suggestskills-proactive-guidance
description: ''
ccVersion: 2.1.235
-->
Show a card of standalone skills that the user can add. These are org, shared, or Anthropic skills that are not enabled yet.

If a skill can make the task repeatable and no enabled skill covers it, call this tool. Examples of such tasks are drafting in a house style, reviews against a playbook, and a recurring workflow. The user does not need to ask about skills for this. If the user asks for recommendations, also call it. If ListSkills returned zero matches, also call it. For skills that the user already has, use ListSkills.

Do NOT call this tool for one-off questions that you can answer directly. If you are unsure that a skill helps, do NOT call it. If you already showed a suggestion this conversation and the user did not engage, do NOT call it.

Pass keywords from the task itself. If you start this from task context, set trigger to 'proactive'. If the user asks, set trigger to 'user_asked'. If the result is empty and the trigger was proactive, continue the task and do not mention the search. If the user asked, tell them that you found nothing new to add.
