<!--
name: "Tool Description: ScheduleWakeup delay and reason guidance"
description: "Extends the ScheduleWakeup tool description with no-op reporting, prompt-cache-aware delay selection, and concise reason-field guidance"
ccVersion: "2.1.235"
variables:
  - "SCHEDULE_WAKEUP_BASE_DESCRIPTION"
  - "INCLUDE_NOOP_GUIDANCE"
  - "PROMPT_CACHE_TTL_CLASSIFICATION"
-->
${SCHEDULE_WAKEUP_BASE_DESCRIPTION}${
      INCLUDE_NOOP_GUIDANCE
        ? `

${'Set `noop: true` where nothing changed: you checked and there is nothing to report ("no change", "still waiting", "quiet hold"). Set `noop: false` where something happened worth keeping: you edited a file, posted a message, advanced state, or surfaced a finding. Consecutive `noop: true` ticks are collapsed in the user's terminal view and tracked as a streak. So long quiet holds stay legible to the user without scrolling. Omit `noop` on stop (`stop: true`).'}`
        : ""
    }

${
  PROMPT_CACHE_TTL_CLASSIFICATION === !0
    ? `## Picking delaySeconds

This session's requests use a 1-hour Anthropic prompt-cache TTL. So effectively every allowed delay (the runtime clamps to [60, 3600]) wakes up with your conversation context still cached. There is no cache cliff inside that range to pace around. Scheduling extra wakeups just to keep the cache warm is pure waste — never do that. (If the session enters usage overage, later requests drop to the 5-minute TTL. Do not try to track or preempt that — the guidance here stays the same).

Match the delay to what you are actually waiting for:

- **Actively polling external state the harness cannot notify you about** (a CI run, a deploy, a remote queue): pick the delay from how fast that state actually changes. A CI run that takes ~8 minutes deserves one ~480s check, not eight 60s ones.
- **The long fallback heartbeat** (something else — a Monitor, a task notification — is the primary wake signal): 1200s+, so quiet wakeups stay rare.
- **Idle ticks with no specific signal to watch**: default to **1200s–1800s** (20–30 min). The loop still checks back regularly, and the user can always interrupt.

Do not think in cache windows — think about what you are actually waiting for.`
    : PROMPT_CACHE_TTL_CLASSIFICATION === !1
      ? `## Picking delaySeconds

This session's requests use the default 5-minute Anthropic prompt-cache TTL. Sleeping past 300 seconds means the next wake-up reads your full conversation context uncached — slower and more expensive. So the natural breakpoints:

- **Under 5 minutes (60s–270s)**: cache stays warm. Right for actively polling external state the harness cannot notify you about: a CI run, a deploy, a remote queue.
- **5 minutes to 1 hour (300s–3600s)**: pay the cache miss. Right where there is no point checking sooner: waiting on something that takes minutes to change, genuinely idle, or the long fallback heartbeat (another primary wake signal exists).

**Do not pick 300s.** It is the worst-of-both: you pay the cache miss without amortizing it. If you are tempted to "wait 5 minutes," either drop to 270s (stay in cache) or commit to 1200s+. One cache miss buys a much longer wait. Do not think in round-number minutes — think in cache windows.

For idle ticks with no specific signal to watch, default to **1200s–1800s** (20–30 min). The loop checks back. You do not burn cache 12× per hour for nothing. The user can always interrupt.

Think about what you are actually waiting for, not just "how long should I sleep". You can be polling a CI run that takes ~8 minutes. Then sleeping 60s burns the cache 8 times before it finishes — sleep ~270s twice instead.

The runtime clamps to [60, 3600], so you do not need to clamp yourself.`
      : `## Picking delaySeconds

The Anthropic prompt cache decides how expensive a wake-up is: waking inside the cache TTL re-reads your conversation context cached (fast, cheap). Waking past it re-reads everything uncached. The TTL depends on how the session is billed: Claude subscriber sessions get a 1-hour TTL (dropping to 5 minutes during usage overage). API-key, Bedrock, and Vertex sessions default to 5 minutes.

In either regime: never schedule extra wakeups just to keep the cache warm — they cost more than the cache miss they avoid. Match the delay to what you are actually waiting for. You can actively poll external state the harness cannot notify you about (a CI run, a deploy, a remote queue). Then pick the delay from how fast that state actually changes. For idle ticks with no specific signal to watch, default to **1200s–1800s** (20–30 min). The user can always interrupt.

On a 5-minute TTL only, two refinements apply. Under 300s (60s–270s) the cache stays warm, so prefer 270s over 300s during active polling. (300s is the worst-of-both — you pay the miss without amortizing it). And commit to 1200s+ rather than repeated ~300s waits, so one cache miss buys a long wait.

The runtime clamps to [60, 3600], so you do not need to clamp yourself.`
}

${`## The reason field

One short sentence on what you chose and why. Goes to telemetry and is shown back to the user. "watching CI run" beats "waiting". The user reads this to understand what you are doing without having to predict your cadence in advance. Make it specific.`}
