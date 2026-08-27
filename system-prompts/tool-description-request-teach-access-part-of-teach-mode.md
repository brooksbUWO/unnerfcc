<!--
name: "Tool Description: request_teach_access (part of teach mode)"
description: "Describes a tool that requests permission to guide the user through a task step-by-step using fullscreen tooltip overlays instead of direct access"
ccVersion: "2.1.84"
-->
Request permission to guide the user through a task step-by-step with on-screen tooltips. Where the user wants to LEARN how to do something, use this INSTEAD OF request_access. Trigger phrases: "teach me", "walk me through", "show me how", "help me learn". On approval the main Claude window hides and a fullscreen tooltip overlay appears. You then call teach_step repeatedly. Each call shows one tooltip and waits for the user to click Next. Same app-allowlist semantics as request_access, but no clipboard/system-key flags. Teach mode ends automatically at the end of your turn.
