# FareTally · 航价笔记

[简体中文](README.zh-CN.md) · English

A free, open-source flight-research skill that compares airports, flexible dates and real trip costs through conversation.

**Find a lower fare that fits the traveler.** The skill first asks about dates and times, nearby airports, stays, baggage, budget airlines, connections and special requirements. It then researches approved combinations, verifies whole-itinerary prices and explains the tradeoffs.

## What makes it useful

- Earlier **and** later dates, inclusive endpoints and return dates are part of a recorded search matrix.
- Multi-city and open-jaw fares are verified as whole bookings, not reconstructed from unrelated single-leg prices.
- Required bags, airport transport and extra lodging are separated from the airfare. Unknown costs stay unknown.
- Midnight arrivals, paid hotel nights and local arrival deadlines are checked explicitly.
- Query coverage, failed pages, historical prices and final-versus-stage quotes are visible.
- Chinese and English prompts and reports are supported; Ctrip is optional, not assumed universally cheapest.

## Requirements

A Codex installation that supports local skills, plus working live web/browser tools or a suitable authorized flight-search connector. The skill itself does not provide inventory, a browser, an API key or a booking account. Python 3.10+ is optional for the offline coverage helper. This release contains no live booking connector.

## Install

### Ask Codex to install from GitHub

Send this to Codex to install from the published repository:

```text
$skill-installer Install the skill from https://github.com/DaySense/fare-tally/tree/main/skills/fare-tally
```

That is a **Codex chat prompt**, not a terminal command. If the skill installer is unavailable, use the manual method.

[Download the single-skill ZIP](https://github.com/DaySense/fare-tally/releases/download/v0.1.2/fare-tally-skill-v0.1.2.zip) · [Latest release](https://github.com/DaySense/fare-tally/releases/latest)

### Manual installation, no terminal required

Download/extract the repository, then copy the **entire** `skills/fare-tally` folder into the skills directory your Codex installation uses. Current official Codex documentation uses `~/.agents/skills/` for user skills or `.agents/skills/` inside a project. Verify this final structure:

```text
<skills-directory>/fare-tally/SKILL.md
<skills-directory>/fare-tally/agents/openai.yaml
<skills-directory>/fare-tally/references/...
<skills-directory>/fare-tally/scripts/...
```

Do not copy just SKILL.md or nest the whole repository inside the skills directory. If the installed skill is not visible on the next turn, restart Codex and check the location. A standalone GitHub repository is not automatically installed in ordinary ChatGPT chat. See [official local skill guidance](https://learn.chatgpt.com/docs/build-skills) and [manual skill directory examples](https://developers.openai.com/api/reference/cli).

## Use

```text
Use $fare-tally to find a low-cost return flight. I can shift my dates by two days. Please ask about nearby airports, baggage and connection preferences before searching.
```

```text
用 $fare-tally 帮我查低价机票，日期可以前后调整两天。请先问清周边机场、行李和中转偏好，再开始查价。
```

You do not need to know airport codes. If Ctrip or another source needs an account, the agent explains why and asks you to log in in the relevant browser yourself. Never send passwords, OTPs or passport numbers in the chat. It researches fares; it does not automatically book or pay.

## Optional coverage helper

From the installed skill folder:

```bash
python3 scripts/search_matrix.py plan examples/search-space.json --out /path/to/private-research/plan.json
python3 scripts/search_matrix.py audit /path/to/private-research/plan.json /path/to/private-research/ledger.json
```

The sample is fictional. These commands plan/audit departure-date queries **offline**; they do not search airlines, generate prices or establish hotel-stay feasibility. See [the schema and exit codes](skills/fare-tally/references/coverage.md). Incomplete audits intentionally return exit code 1.

## Project and name

[Publishing guide (中文)](docs/publish.zh-CN.md) · [Name research and limits](docs/name-check-2026-11-09.md) · [Validation](docs/validation.md)

FareTally / 航价笔记 is the new working name, replacing FareMosaic to reduce association with existing Mosaic products in aviation. Public name screening found no directly same-named project; China and Singapore trademark clearance is **not complete**. The Chinese display name was subsequently changed from 票价有数 to 航价笔记; see the [Chinese name update](docs/chinese-name-check-2026-11-09.md). The earlier research record retains its historical queries and scope. There is no affiliation with airlines, OTAs or similarly named products. No private traveler records, browser sessions or credentials are included. Keep real research in a private directory outside this repository; use fictional data in contributions/issues.

MIT licensed; see [LICENSE](LICENSE). Fares change; the reported result is the lowest verified within the disclosed scope, not a market-wide guarantee.
