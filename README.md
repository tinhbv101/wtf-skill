# wtf

**An [Agent Skill](https://agentskills.io) for the "I'll clone it in an hour with AI" crowd: it mocks the plan, proves it with sourced numbers, then hands over a plan that can ship.**

"Clone MISA tonight and sell it tomorrow." "Uber by Sunday." "We don't need developers, the AI writes everything."

`wtf` mocks the plan in the user's own language and slang, rates it on a **WTF-meter**, backs each jab with a figure that has a source, and finishes with something they can really ship - down to what to do tomorrow morning.

> **WTF-meter: 10/10** - pitch-deck energy, zero product.
>
> **A weekend? For Uber?** Uber has been at it since 2009, employs ~34,000 people and operates in 15,000+ cities. You have 48 hours, Cursor and no drivers. What goes live Monday is a map with a "Book" button that books nothing.

## Features

- **WTF-meter 0-10** - scored from the claimed timeframe vs a realistic one; a sane plan scores low and gets a short answer, and the score drops when the user shrinks the plan
- **Sourced numbers only** - every figure carries a source and date (checked Sep 2026): Meta, Uber, Grab, Netflix, OpenAI, Stripe, Notion, Figma... The lint script fails on an unsourced figure
- **Archetype-aware** - social, marketplace / ride-hailing, e-commerce, fintech / e-wallets, B2B SaaS, accounting / ERP, AI apps / "clone ChatGPT", "fire the devs, AI does it"
- **Vietnam built in** - MISA, Zalo/VNG, MoMo, VNPay, Tiki, Be, Xanh SM, FPT, plus current law: PDPL 91/2025, Decree 356/2025, Decree 147/2024, Decree 52/2024, e-invoice Decree 70/2025, Circular 99/2025
- **Laws for where it ships** - legal points depend on the product's market, whatever language the user types in (Vietnam, EU, US, Japan)
- **Repo mode** - roasts a real codebase with file-path evidence (leaked keys, missing access checks, no tests); read-only, secrets masked
- **Handles pushback** - "Instagram had 13 people", "Lovable did it in 5 minutes", "models will be 10x better": stands on the facts, gives ground on scope
- **Intensity** - mild / default / nuclear on request
- **Guardrails** - targets the plan, never the person; no public shaming of third parties; drops the swearing when the user has savings on the line or sounds shaken
- **Native voice** - EN, VI, JA, KO, ZH, ES, plus FR, DE, PT (awaiting native review)
- **Tooling** - 7 evals with assertions, `tools/validate.py` (spec + "no source, no number" lint), `tools/build.py` (`.skill` bundle + plain system prompt)

## Install

The skill is the `wtf/` folder. Leave the folder name as `wtf` - agents match it against the `name` in `SKILL.md` and skip the skill if they differ.

```bash
# Claude Code, for all your projects
mkdir -p ~/.claude/skills && cp -r wtf ~/.claude/skills/

# Codex, Gemini CLI, Cursor, Copilot - shared skills folder
mkdir -p ~/.agents/skills && cp -r wtf ~/.agents/skills/
```

Per-project installs work too: copy the folder into `.claude/skills/` (Claude Code) or `.agents/skills/` in your repo. Other agents: see their docs for the skills path.

- **Claude app (claude.ai / Desktop)** - run `python3 tools/build.py`, open `dist/wtf.skill`, click **Save skill**
- **Any other chatbot** - the same build writes `dist/wtf-system-prompt.md`; paste it in as the system prompt

## Usage

The roast only fires when someone clearly asks for one; ordinary "help me build X" requests get ordinary help.

```
/wtf I'm vibe-coding a Shopee competitor over the long weekend
Roast my repo - the README says it's production-ready
Chửi tôi đi: tôi định clone Zalo trong 3 ngày
ボロクソに言ってくれ。今週末でメルカリを作る
Destrózame esta idea: un Notion propio en una noche
Rip this apart, nuclear mode: AI agents will replace my whole dev team
```

## What a reply looks like

0. **WTF-meter** - score and a short verdict
1. **The slap** - their deadline next to the product's real scale
2. **What's under the waterline** - 5-8 product-specific items with sourced figures and local law (repo mode: "What your code actually says", with paths)
3. **AI: what it does, what it doesn't**
4. **The way out** - their deadline → 1-2 weeks → 3-6 months, one loop to build, one move for tomorrow morning
5. **Last word** - one line worth quoting

Roughly 300-600 words (150-300 for sane plans), no emoji, headers in the user's language.

## Layout

```
wtf/
├── SKILL.md                 # Workflow, WTF-meter, house rules, reply layout
└── references/
    ├── figures.md           # Sourced figures: global giants, AI/SaaS, Vietnam
    ├── waterline.md         # Invisible work by archetype + law by market
    ├── effort-benchmarks.md # Rule-of-thumb timelines for the meter and the way out
    ├── comebacks.md         # Answers to common pushback
    ├── repo-roast.md        # Evidence-based roast of a real codebase
    └── voices.md            # How to roast natively, language by language
evals/evals.json             # Test prompts + assertions
tools/validate.py            # Spec + sourcing lint
tools/build.py               # Builds dist/wtf.skill and the system prompt
```

## Keeping it accurate

Figures were checked in **September 2026**, each with source and as-of date. Headcounts move every quarter and laws every year - Vietnam replaced its personal-data regime on 1 Jan 2026. With web search available the skill can look up products that aren't listed; without it, it stays with orders of magnitude.

- **New product**: add a block to `figures.md` with a `Source:` line (filing, annual report, reputable press). `tools/validate.py` rejects figures without one
- **New language**: add a section to `voices.md` and have a native speaker review it (FR / DE / PT still need one)
- **New market's laws**: extend "Legal by target market" in `waterline.md`
- **Check a change**: add a case to `evals/evals.json`, run `python3 tools/validate.py`, compare replies before and after

## Disclaimer

It swears on purpose. Point it at yourself or at people who asked for it. Legal points are prompts to go check, not legal advice.

## Credits

The idea came from [zack-the-worker/fomo-cc](https://github.com/zack-the-worker/fomo-cc).

## License

[MIT](LICENSE)
