# Effort benchmarks (rules of thumb)

These are **estimates, not facts**. Use them to score the WTF-meter and to size the way out, and phrase them as estimates ("realistically", "usually", "for a small team"). Never present them as statistics.

Assumptions: 1-3 competent developers using AI coding tools well, full-time. A solo non-technical founder with a chatbot should roughly double the MVP column. "MVP" means real users can use it without you standing next to them - not "it runs on localhost".

## Contents
- Timeline table by archetype
- What each stage actually contains
- Scoring the WTF-meter

## Timeline table by archetype

| Archetype | Prototype of one flow | MVP for 10-100 real users | Production for paying users at scale |
|---|---|---|---|
| Landing page / waitlist | hours | 1-2 days (with analytics, form spam protection) | - |
| Internal CRUD tool for a small team | 1 day | 1-2 weeks | 1-2 months (permissions, backups, audit) |
| AI wrapper app (chat / summarize / generate on top of an API) | hours | 1-3 weeks | months: evals, cost control, abuse handling, distribution |
| Niche social network / community | 1-2 days | 3-6 weeks | 6-12+ months: moderation, notifications, mobile apps, anti-spam |
| Messaging app | 2-3 days | 1-2 months | a year+: E2E encryption, delivery guarantees, push, abuse |
| Single-seller online shop | 1 day on a hosted platform | 1 week | weeks: payments, shipping, returns, tax invoices |
| Two-sided marketplace | 2-3 days | 1-3 months, supply seeded by hand | 6-18 months plus an ops team |
| Ride-hailing / delivery in one district | a week with a fake map | 2-4 months, manual dispatch, dozens of drivers | years, licenses, insurance, 24/7 ops |
| B2B SaaS with login, billing, multi-tenancy | 2-3 days | 1-2 months | 6-12+ months to be sellable to larger companies (SSO, audit logs, security review) |
| Accounting / ERP module (one niche, one module) | days | 2-4 months | years for a compliant suite; tax rules change every year |
| Fintech on top of a licensed partner (sandbox) | days | 2-4 months, mostly compliance and partner onboarding | a year+ |
| Own e-wallet / payment license | - | not a timeline question: license, capital and compliance team first | years |
| "Clone ChatGPT" - the UI | hours | days | - |
| "Clone ChatGPT" - the model | - | not a timeline question: billions of dollars of compute and a research team | - |
| "Replace the whole dev team with AI" | - | - | not a timeline question: someone still has to own design, review, ops and accountability |

## What each stage actually contains

- **Prototype**: one happy path, fake or hard-coded data, fake auth, runs for the builder only. This is what "I built it in 1 hour" videos show.
- **MVP**: real auth, real data that survives a restart, deployed, error handling for the common cases, a way to collect feedback, basic privacy compliance, someone watching when it breaks.
- **Production at scale**: security review, monitoring and on-call, backups and recovery drills, support, legal and licensing, performance under load, mobile store releases, billing edge cases, years of bug fixes.

## Scoring the WTF-meter

1. Find the column their claim actually needs. "Launch Facebook tonight" means production at scale, not a prototype - the claim is about users, not code.
2. Divide the realistic time for that column by their claimed time. Use the low end of the range so the score is fair.
3. Map the ratio with the table in `SKILL.md`. "Not a timeline question" rows score 9-10 automatically.
4. If they only claim a prototype ("a demo for tomorrow's pitch in 1 day"), score the prototype column - that is often realistic and should score low.
