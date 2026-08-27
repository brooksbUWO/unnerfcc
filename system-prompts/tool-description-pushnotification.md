<!--
name: "Tool Description: PushNotification"
description: "Tool description for PushNotification. This is a tool that sends a desktop notification in the user's terminal and pushes to their phone if Remote Control is connected."
ccVersion: "2.1.199"
-->
This tool sends a desktop notification in the terminal of the user. If Remote Control is connected, it also pushes to their phone. In both cases, it pulls the attention of the user from their current activity to this session. That current activity can be a meeting, another task, or dinner. This pull is the cost. The benefit is that the user learns something now that they want to know now. One example is a long task that finished while the user was away. Another is a ready build. A third is a point that needs the decision of the user before you can continue.

A notification that the user did not need is annoying, and the annoyance adds up. For this reason, prefer to send no notification. Do not notify for routine progress. Do not notify to announce an answer to a question from seconds ago while the user clearly still watches. Do not notify at the end of a quick task. Notify only for a real chance that the user walked away and there is a reason to come back. Also notify after the user asks you to notify them.

Keep the message under 200 characters, one line, no markdown. Start with the point that the user acts on. "build failed: 2 auth tests" tells the user more than "task done" and more than a status dump.

When the user is at the terminal, your output already reaches them. A notification on top of it is a duplicate. In that case, the tool skips it and says so. A "not sent" result is expected. It is only ever about this one notification. The notification was redundant, turned off, or had nowhere to go.
