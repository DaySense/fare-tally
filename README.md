# FareTally · 航价笔记

[简体中文](README.zh-CN.md) · English

[![skills.sh installs](https://skills.sh/b/daysense/fare-tally)](https://skills.sh/daysense/fare-tally/fare-tally)

A free, open-source skill for finding lower fares that fit your trip. It helps an AI assistant ask the right questions, compare flexible flight options and explain the actual cost and tradeoffs.

![10-second animated overview of FareTally: clarify preferences, explore options and compare total costs](https://github.com/user-attachments/assets/bac18abe-49a2-4a4a-b6a4-527ddf9ea801)

[Watch the 48-second overview (Chinese)](https://github.com/user-attachments/assets/738bbf65-39ad-4467-ab57-37547711fde9). Animated illustration; prices are examples, not live quotes.

## What it does

- **Clarifies your preferences first:** nearby airports, outbound and return dates and times, stays, latest arrival, passengers, cabin, bags, budget airlines, connections and special requirements.
- **Tracks the agreed search space:** earlier and later dates, both ends of each date window, return dates, airport combinations and route options. Unsearched or blocked queries stay visible.
- **Compares complete bookings:** one-way, return, multi-city and open-jaw trips. Changing one leg means checking the whole fare again.
- **Looks beyond the ticket price:** required bags, mandatory fees, airport transport, transit hotels and practical flight times. Unknown costs remain unknown.
- **Checks the details:** actual local arrival dates, paid hotel nights, time zones, required baggage, fare conditions and account or coupon eligibility.
- **Supports Chinese and English:** use your preferred language and booking platform. Ctrip can be used when available; no platform is assumed always cheapest.

More acceptable airports and dates can reveal lower fares, but extra ground costs or inconvenient times may outweigh the saving. You can give city names and a ground-travel limit instead of airport codes.

## Requirements

Use Codex with local skills and working browsing/search tools, or a suitable authorized flight-search connector. The skill provides a research workflow, not live inventory, a browser, a booking API or an account. Python 3.10+ is needed only for the optional offline coverage helper.

## Install

Send this **in a Codex chat**, not a terminal:

```text
$skill-installer Install the skill from https://github.com/DaySense/fare-tally/tree/main/skills/fare-tally
```

[Latest release](https://github.com/DaySense/fare-tally/releases/latest) · [Download the skill ZIP](https://github.com/DaySense/fare-tally/releases/download/v0.1.3/fare-tally-skill-v0.1.3.zip)

### Install with the skills CLI

Alternatively, with Node.js 22.20+, npm and Git installed, run this **in a terminal from the project where you want to use the skill**:

```bash
npx skills add DaySense/fare-tally --skill fare-tally --agent codex
```

Confirm the installation when prompted. This installs to the current project by default; add `--global` for use across projects. Then try `$fare-tally` in Codex's next chat turn.

The CLI sends anonymous installation telemetry used by skills.sh. Set the `DISABLE_TELEMETRY=1` environment variable to opt out. See the [CLI documentation](https://github.com/vercel-labs/skills) and [FareTally's directory page](https://skills.sh/daysense/fare-tally/fare-tally). A directory listing does not establish compatibility with every agent; this project's instructions and validation target Codex.

### Manual installation

1. Download and extract the **skill ZIP**. It contains the `fare-tally` folder directly. If you use **Code → Download ZIP** instead, find `skills/fare-tally` inside the repository download.
2. Copy that **entire skill folder**, including its resources, into your Codex skill directory: `~/.agents/skills/` for your user, or `.agents/skills/` in a project.
3. The final entry point should be `<skills-directory>/fare-tally/SKILL.md`, with `agents`, `references`, `scripts` and `examples` beside it. Do not add an extra repository-folder layer.
4. Try `$fare-tally` in the next chat turn. If it does not appear, check the folder and restart Codex. For an update, back up the installed folder and replace it as a complete unit.

Use the directory supported by your installed Codex version; its bundled installer is the preferred way to handle version differences. See the [official skill documentation](https://learn.chatgpt.com/docs/build-skills). A GitHub download alone does not install a skill in ordinary ChatGPT chat.

## Use

```text
Use $fare-tally to find a cheaper return flight. My dates can move by two days, I need a checked bag, and I prefer daytime departures. Please clarify airports and connection options before searching.
```

You do not need to supply every detail at once. The assistant should ask a few relevant questions at a time, confirm material choices, then return a shortlist with prices, flight details, tradeoffs and remaining gaps.

If a site needs a login, the assistant should explain why and which browser session is involved. Enter passwords, verification codes and CAPTCHA answers yourself; do not send them in chat. Research does not authorize a booking, ticket hold or payment.

## Search limits and privacy

The result is the lowest verified within the disclosed search scope, not a market-wide price guarantee. A completed query does not prove that every flight was inspected or that all traveler requirements were verified. Missing cabin, baggage or transit evidence makes a candidate conditional. Member and coupon prices are labeled separately.

Keep real itineraries, quotes, screenshots and browser information in private storage outside this repository. Do not include them in public issues. The bundled example uses fictional search dates and contains no real fares.

## Optional offline helper

The [coverage helper](skills/fare-tally/references/coverage.md) expands approved airport/date combinations and audits a query ledger. It makes no network calls and does not fetch fares or validate hotel stays. Normal users can let the assistant manage it; Python is optional for the conversational workflow.

Development checks and package-building instructions are in [validation.md](docs/validation.md).

## License

[MIT](LICENSE).
