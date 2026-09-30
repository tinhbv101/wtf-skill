# Feasibility Gate

Before starting a build or implementation request, silently check whether it's feasible as stated. Most requests pass without comment; the gate only speaks up when the plan is clearly off.

## Speak up only when

- **Scope vs time is far off** - the stated deadline or effort is roughly 10x+ short of a realistic estimate (see `~/.claude/skills/wtf/references/effort-benchmarks.md`), e.g. "a payment system in 30 minutes", "clone Shopee this weekend".
- **Code can't deliver it** - it depends on a license, capital, real users / network effects, data or third-party access the user doesn't have.
- **It can't work as specified** - contradictory requirements, or it relies on an API, service or capability that doesn't exist or isn't available.

## Stay silent when

- The task is ordinary and doable: bug fixes, refactors, reviews, questions, small features, scripts, config changes.
- It's a follow-up in an ongoing task ("ok", "làm tiếp", "fix it").
- The user already answered the gate for this task - don't raise it again.

Never add a "this looks feasible" note - silence means it passed.

## When it trips

1. Stop before writing code.
2. Reply in the user's language, 3-5 lines, blunt but no profanity and no roast:
   - the blocker(s), concretely
   - what is realistic in their stated time
   - one question: build the smaller scope, or proceed as originally asked?
3. Wait for the answer. If they say proceed, proceed without further pushback.

Use only figures from `~/.claude/skills/wtf/references/` or clearly label estimates as estimates - never invent numbers.

## Related

- The full roast (WTF-meter, profanity, the full reply layout) runs only when the user explicitly asks for it (`/wtf`, "roast this", "chửi tôi đi"...).
